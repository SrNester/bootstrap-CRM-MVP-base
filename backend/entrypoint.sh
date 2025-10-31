#!/bin/sh
set -e

echo "Esperando a PostgreSQL..."
python - <<'PY'
import time, os
import psycopg2

host=os.getenv('POSTGRES_HOST','db')
port=os.getenv('POSTGRES_PORT','5432')
user=os.getenv('POSTGRES_USER','postgres')
password=os.getenv('POSTGRES_PASSWORD','postgres')
dbname=os.getenv('POSTGRES_DB','crm')

attempts=0
while attempts < 30:
    try:
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname)
        conn.close()
        print('PostgreSQL listo')
        break
    except Exception as e:
        print('Aún no disponible, reintentando...')
        time.sleep(2)
        attempts += 1
PY

echo "Aplicando migraciones"
python manage.py makemigrations core || true
python manage.py migrate --noinput

echo "Colectando estáticos"
python manage.py collectstatic --noinput || true

echo "Levantando servidor Django"
python manage.py runserver 0.0.0.0:8000

# Ejecuta seed opcionalmente (solo desarrollo)
if [ "$DJANGO_LOAD_SEED" = "True" ] || [ "$DJANGO_LOAD_SEED" = "true" ]; then
  echo "Ejecutando init_seed"
  python manage.py init_seed || true
fi