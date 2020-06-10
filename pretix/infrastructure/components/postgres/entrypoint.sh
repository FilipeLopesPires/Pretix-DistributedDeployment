#!/bin/bash

cd postgres_exporter_v0.8.0_linux-amd64/
export DATA_SOURCE_NAME="postgresql://postgres:adminpassword@localhost:5432/customdatabase"
./postgres_exporter --web.listen-address=":9187" &
cd ..

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting PG"
exec "/opt/bitnami/scripts/postgresql-repmgr/entrypoint.sh" "$@"
