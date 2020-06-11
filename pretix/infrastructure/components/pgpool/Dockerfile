FROM bitnami/pgpool:4
USER root

RUN apt-get update -q
RUN apt-get install curl -y -q

COPY ./entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 5432

USER 1001
ENTRYPOINT ["entrypoint.sh"]
#ENTRYPOINT [ "/opt/bitnami/scripts/pgpool/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/pgpool/run.sh" ]