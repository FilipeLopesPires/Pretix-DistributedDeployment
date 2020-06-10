FROM haproxy:1.7

RUN apt-get update -q
RUN apt-get install wget -y -q
RUN apt-get install unzip -q
RUN apt-get install make -q
RUN apt-get install curl -y -q
RUN apt-get install golang -y -q

COPY haproxy-entrypoint.sh /

RUN chmod +x /haproxy-entrypoint.sh

EXPOSE 6379
EXPOSE 9000
EXPOSE 9101

ENTRYPOINT [ "/haproxy-entrypoint.sh" ]

CMD [ "haproxy", "-f", "/etc/haproxy/haproxy.cfg" ]