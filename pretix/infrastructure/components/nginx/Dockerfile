FROM nginx:latest

RUN apt-get update -q
RUN apt-get install wget -y -q
RUN apt-get install curl -y -q

COPY ./nginx-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/nginx-entrypoint.sh

EXPOSE 7200
EXPOSE 9913

ENTRYPOINT ["nginx-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]