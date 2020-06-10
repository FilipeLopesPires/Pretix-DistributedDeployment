#!/bin/bash

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting PGPool"
exec "/opt/bitnami/scripts/pgpool/entrypoint.sh" "$@"
