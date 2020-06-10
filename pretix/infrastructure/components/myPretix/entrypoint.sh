#!/usr/bin/env bash

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting MyPretix"
exec /wait-for-it.sh ${POSTGRESIP}:5432 --strict -- /wait-for-it.sh ${REDISIP}:6379 --strict -- pretix all