#!/bin/bash
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ask
sudo gunicorn -c /home/box/web/etc/gunicorn.conf -c /home/box/web/etc/gunicorn_ask.conf ask.wsgi
