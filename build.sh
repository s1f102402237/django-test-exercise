#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
echo "--- Django settings test start ---"
python manage.py shell -c "from django.conf import settings; print('SECRET_KEY exists:', hasattr(settings, 'SECRET_KEY'))"
echo "--- Django settings test end ---"