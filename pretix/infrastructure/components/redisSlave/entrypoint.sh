#!/bin/bash

# get container id from /proc/self/cgroup
# CONTAINER_ID_LONG=`cat /proc/self/cgroup | grep 'docker' | sed 's/^.*\///' | tail -n1`

# # search for the id in /etc/hosts, it uses only first 12 characters
# CONTAINER_ID_SHORT=${CONTAINER_ID_LONG:0:12}
# DOCKER_CONTAINER_IP_LINE=`cat /etc/hosts | grep $CONTAINER_ID_SHORT`

# # get the ip address
# THIS_DOCKER_CONTAINER_IP=`(echo $DOCKER_CONTAINER_IP_LINE | grep -o '[0-9]\+[.][0-9]\+[.][0-9]\+[.][0-9]\+')`

# # set as environment variable
# export DOCKER_CONTAINER_IP=$THIS_DOCKER_CONTAINER_IP

# replace placeholders in redis.conf file with environment variables
sed -i 's,{{REDIS_MASTER}},'"${REDIS_MASTER}"',g' /etc/redis/redis.conf
# sed -i 's,{{REPLICA_CONTAINER_IP}},'"${DOCKER_CONTAINER_IP}"',g' /etc/redis/redis.conf

wget -qO- https://github.com/oliver006/redis_exporter/releases/download/v1.6.1/redis_exporter-v1.6.1.linux-amd64.tar.gz | tar xvz redis_exporter-v1.6.1.linux-amd64 && ./redis_exporter-v1.6.1.linux-amd64/redis_exporter -web.listen-address ":9121" &

curl -f -s -H "Content-Type: application/json" -d "{\"service\":\"$NAME\"}" 10.5.0.108:9999/service &

# start redis
echo "=> Starting RedisSlave"
exec /wait-for-it.sh ${REDIS_MASTER}:6379 --strict -- docker-entrypoint.sh redis-server /etc/redis/redis.conf
