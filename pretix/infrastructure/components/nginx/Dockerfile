FROM nginx:latest

#RUN apk add --no-cache \
#        curl \
#        bash

RUN apt-get update
RUN apt-get install wget -y 
#RUN apt-get install make
#RUN apt-get install golang -y
#RUN apt-get install git -y

COPY ./nginx-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/nginx-entrypoint.sh

EXPOSE 7200
EXPOSE 9913

ENTRYPOINT ["nginx-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]