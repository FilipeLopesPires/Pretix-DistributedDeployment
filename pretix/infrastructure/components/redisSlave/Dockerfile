FROM redis:5.0.9-alpine

RUN apk add --quiet --no-cache \
        curl \
        bash

COPY ./redis.conf /etc/redis/redis.conf
RUN chown redis:redis /etc/redis/redis.conf

COPY ./entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY ./wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

EXPOSE 6379

EXPOSE 9121

ENTRYPOINT ["entrypoint.sh"]