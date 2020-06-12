#!/bin/bash

go get github.com/wrouesnel/postgres_exporter
cd ${GOPATH-$HOME/go}/src/github.com/wrouesnel/postgres_exporter
go run mage.go binary
# export DATA_SOURCE_NAME="postgresql://postgres:adminpassword@localhost:5432/customdatabase"
# ./postgres_exporter --web.listen-address=":9187" &

