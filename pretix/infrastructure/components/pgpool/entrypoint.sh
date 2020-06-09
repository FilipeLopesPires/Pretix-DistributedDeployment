#!/bin/bash

ls
cd postgres_exporter_v0.8.0_linux-amd64/
export DATA_SOURCE_NAME="postgresql://postgres:adminpassword@localhost:5432/customdatabase"
./postgres_exporter --web.listen-address=":9187" &
cd ..

exec "/opt/bitnami/scripts/postgresql-repmgr/entrypoint.sh" "$@"
