#!/bin/bash

# wget -q https://github.com/hnlq715/nginx-vts-exporter/releases/download/v0.10.3/nginx-vts-exporter-0.10.3.linux-amd64.tar.gz
# tar xzf nginx-vts-exporter-0.10.3.linux-amd64.tar.gz && rm -rf nginx-vts-exporter-0.10.3.linux-amd64.tar.gz

# cd nginx-vts-exporter-0.10.3.linux-amd64/ && nohup ./nginx-vts-exporter -telemetry.address=":9913" -nginx.scrape_uri=http://localhost/status/format/json &

# curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting NGinX"
#nginx -g "daemon off;"