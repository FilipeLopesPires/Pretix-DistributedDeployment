#!/bin/bash

set -ex

echo "=> Creating HAProxy Configuration Folder"
mkdir -p /etc/haproxy


echo "=> Writing HAProxy Configuration File"
tee /etc/haproxy/haproxy.cfg <<EOF
defaults
  mode tcp
  timeout connect 3s
  timeout server 6s
  timeout client 6s
listen stats
  mode http
  bind :9000
  stats enable
  stats hide-version
  stats realm Haproxy\ Statistics
  stats uri /haproxy_stats
frontend ft_redis
  mode tcp
  bind *:6379
  default_backend bk_redis
backend bk_redis
  mode tcp
  option tcplog
  option tcp-check
  #uncomment these lines if you have basic auth
  #tcp-check send AUTH\ yourpassword\r\n
  #tcp-check expect +OK
  tcp-check send PING\r\n
  tcp-check expect string +PONG
  tcp-check send info\ replication\r\n
  tcp-check expect string role:master
  tcp-check send QUIT\r\n
  tcp-check expect string +OK
EOF

echo "=> Adding Redis Nodes to Health Check"
COUNT=1

for i in $(echo $REDIS_HOSTS | sed "s/,/ /g")
do
    # call your procedure/other scripts here below
    echo "  server redis-backend-$COUNT $i:6379 maxconn 1024 check inter 1s" >> /etc/haproxy/haproxy.cfg
    COUNT=$((COUNT + 1))
done

wget -q https://github.com/prometheus/haproxy_exporter/archive/master.zip 
unzip -q ./master.zip
cd ./haproxy_exporter-master && make build && ./haproxy_exporter-master --web.listen-address=":9101" --haproxy.scrape-uri="http://localhost:9000/haproxy_stats;csv" &

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

echo "=> Starting HAProxy"
exec "/docker-entrypoint.sh" "$@"