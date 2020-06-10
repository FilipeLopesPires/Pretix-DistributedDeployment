FROM pretix/standalone:stable
USER root

RUN apt-get update -q
RUN apt-get install bash -q

COPY ./wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

COPY ./entrypoint.sh /
RUN chmod 777 /entrypoint.sh
RUN chown -R pretixuser:pretixuser /entrypoint.sh

USER pretixuser
ENTRYPOINT ["/entrypoint.sh"]