#!/bin/bash

docker-compose exec -T mysql mysqldump -uroot -proot estocae_db > initdb/estocae-db.sql
cd initdb
gzip -f estocae-db.sql
