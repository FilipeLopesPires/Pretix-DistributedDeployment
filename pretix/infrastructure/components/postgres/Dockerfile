FROM bitnami/postgresql-repmgr:11

USER root

RUN apt-get update -qq
RUN apt-get install wget -y -qq
RUN apt-get install unzip -qq
RUN apt-get install make -qq
RUN apt-get install curl -y -qq
RUN apt-get install golang -y -qq
RUN apt-get install git -y -qq

COPY ./postgres-exporter.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/postgres-exporter.sh
RUN ["postgres-exporter.sh"]

COPY ./postgres-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/postgres-entrypoint.sh

EXPOSE 9187

USER 1001

ENTRYPOINT ["postgres-entrypoint.sh"]

CMD [ "/opt/bitnami/scripts/postgresql-repmgr/run.sh" ]


