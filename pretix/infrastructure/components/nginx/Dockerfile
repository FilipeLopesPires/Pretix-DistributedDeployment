FROM nginx:1.18.0

RUN apt-get update -qq
RUN apt-get install wget -y -qq
RUN apt-get install curl -y -qq
# RUN apt-get install git -y -qq

COPY ./nginx-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/nginx-entrypoint.sh

EXPOSE 8080
EXPOSE 9913

ENTRYPOINT ["nginx-entrypoint.sh"]
# CMD ["nginx", "-g", "daemon off;"]

