FROM bitnami/pgpool:4
USER root

RUN apt-get update -qq
RUN apt-get install curl -y -qq

COPY ./entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 5432

USER 1001
ENTRYPOINT ["entrypoint.sh"]
#ENTRYPOINT [ "/opt/bitnami/scripts/pgpool/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/pgpool/run.sh" ]