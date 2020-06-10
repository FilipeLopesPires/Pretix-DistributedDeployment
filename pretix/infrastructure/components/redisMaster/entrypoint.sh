#!/bin/bash

wget -qO- https://github.com/oliver006/redis_exporter/releases/download/v1.6.1/redis_exporter-v1.6.1.linux-amd64.tar.gz | tar xz redis_exporter-v1.6.1.linux-amd64 && ./redis_exporter-v1.6.1.linux-amd64/redis_exporter -web.listen-address ":9121" &

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting RedisMaster"
redis-server