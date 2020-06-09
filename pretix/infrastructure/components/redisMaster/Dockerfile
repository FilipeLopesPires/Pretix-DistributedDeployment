FROM redis:5.0.9-alpine

RUN apk add --no-cache \
        curl \
        bash

COPY ./entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 6379
EXPOSE 9121

ENTRYPOINT ["entrypoint.sh"]