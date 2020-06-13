#!/bin/bash

# wget -q https://github.com/wrouesnel/postgres_exporter/releases/download/v0.8.0/postgres_exporter_v0.8.0_linux-amd64.tar.gz
# tar xzf postgres_exporter_v0.8.0_linux-amd64.tar.gz && rm -rf postgres_exporter_v0.8.0_linux-amd64.tar.gz

# cd postgres_exporter_v0.8.0_linux-amd64/
# export DATA_SOURCE_NAME="postgresql://postgres:adminpassword@localhost:5432/customdatabase"
# ./postgres_exporter --web.listen-address=":9187" &
# cd ..

# go get github.com/wrouesnel/postgres_exporter
cd ${GOPATH-$HOME/go}/src/github.com/wrouesnel/postgres_exporter
# go run mage.go binary
export DATA_SOURCE_NAME="postgresql://postgres:adminpassword@localhost:5432/customdatabase?sslmode=disable"
./postgres_exporter --web.listen-address=":9187" &

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting PG"
exec "/opt/bitnami/scripts/postgresql-repmgr/entrypoint.sh" "$@"
