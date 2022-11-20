if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd src; python manage.py createsuperuser --no-input)
fi
(cd src; gunicorn core.wsgi --user www-data --bind 0.0.0.0:8010 --workers 5) &
nginx -g "daemon off;"