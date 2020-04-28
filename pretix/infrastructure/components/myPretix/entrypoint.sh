#!/usr/bin/env bash

exec /wait-for-it.sh ${POSTGRESIP}:5432 --strict -- /wait-for-it.sh ${REDISIP}:6379 --strict -- pretix all