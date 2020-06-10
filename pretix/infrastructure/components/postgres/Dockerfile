FROM bitnami/postgresql-repmgr:11
USER root

RUN apt-get update -q
RUN apt-get install wget -y -q
RUN apt-get install curl -y -q

COPY ./get-exporter.sh /
RUN chmod +x /get-exporter.sh
RUN /get-exporter.sh

COPY ./entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 9187

USER 1001

ENTRYPOINT ["entrypoint.sh"]

CMD [ "/opt/bitnami/scripts/postgresql-repmgr/run.sh" ]