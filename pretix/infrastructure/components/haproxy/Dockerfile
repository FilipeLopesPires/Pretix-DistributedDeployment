FROM haproxy:1.7

RUN apt-get update -qq
RUN apt-get install wget -y -qq
RUN apt-get install unzip -qq
RUN apt-get install make -qq
RUN apt-get install curl -y -qq
RUN apt-get install golang -y -qq

COPY haproxy-entrypoint.sh /
RUN chmod +x /haproxy-entrypoint.sh

EXPOSE 6379
EXPOSE 9000
EXPOSE 9101

ENTRYPOINT [ "/haproxy-entrypoint.sh" ]

CMD [ "haproxy", "-f", "/etc/haproxy/haproxy.cfg" ]