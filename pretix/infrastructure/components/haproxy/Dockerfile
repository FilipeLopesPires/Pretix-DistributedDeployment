FROM haproxy:1.7

RUN apt-get update
RUN apt-get install wget -y 
RUN apt-get install unzip
RUN apt-get install make
RUN apt-get install curl -y
RUN apt-get install golang -y

COPY haproxy-entrypoint.sh /

RUN chmod +x /haproxy-entrypoint.sh

EXPOSE 6379
EXPOSE 9000
EXPOSE 9101

ENTRYPOINT [ "/haproxy-entrypoint.sh" ]

CMD [ "haproxy", "-f", "/etc/haproxy/haproxy.cfg" ]