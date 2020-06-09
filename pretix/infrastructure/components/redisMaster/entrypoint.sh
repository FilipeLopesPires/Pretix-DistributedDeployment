#!/bin/bash

wget -qO- https://github.com/oliver006/redis_exporter/releases/download/v1.6.1/redis_exporter-v1.6.1.linux-amd64.tar.gz | tar xvz redis_exporter-v1.6.1.linux-amd64 && ./redis_exporter-v1.6.1.linux-amd64/redis_exporter -web.listen-address ":9121" &

redis-server