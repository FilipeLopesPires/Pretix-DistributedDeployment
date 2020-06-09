#!/bin/bash

wget https://github.com/hnlq715/nginx-vts-exporter/releases/download/v0.10.3/nginx-vts-exporter-0.10.3.linux-amd64.tar.gz
tar xvzf nginx-vts-exporter-0.10.3.linux-amd64.tar.gz && rm -rf nginx-vts-exporter-0.10.3.linux-amd64.tar.gz

cd nginx-vts-exporter-0.10.3.linux-amd64/ && ./nginx-vts-exporter -telemetry.address=":9913" -nginx.scrape_uri=http://localhost/status/format/json &

echo "=> Starting HAProxy"
exec "/docker-entrypoint.sh" "$@"