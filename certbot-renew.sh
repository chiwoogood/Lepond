#!/bin/bash

docker run --rm \
  -v "/etc/letsencrypt:/etc/letsencrypt" \
  -v "$(pwd)/certbot/webroot:/var/www/certbot" \
  certbot/certbot renew --webroot --webroot-path=/var/www/certbot

docker compose restart nginx