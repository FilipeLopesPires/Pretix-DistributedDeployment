FROM redis:4.0.10-alpine

RUN apk add --no-cache \
        curl \
        bash

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY ./wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

EXPOSE 26379

ENTRYPOINT ["/entrypoint.sh"]