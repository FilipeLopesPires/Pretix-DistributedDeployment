# FROM nginx:1.18.0

# RUN apt-get update -qq
# RUN apt-get install wget -y -qq
# RUN apt-get install curl -y -qq
# RUN apt-get install git -y -qq

# COPY ./nginx-entrypoint.sh /usr/local/bin/
# RUN chmod +x /usr/local/bin/nginx-entrypoint.sh

# EXPOSE 7200
# EXPOSE 9913

# ENTRYPOINT ["nginx-entrypoint.sh"]
# # CMD ["nginx", "-g", "daemon off;"]








# FROM nginx:1.18.0

# ENV NGINX_VERSION     "1.18.0"
# ENV NGINX_VTS_VERSION "0.1.14"

# RUN echo "deb-src http://nginx.org/packages/debian/ stretch nginx" >> /etc/apt/sources.list \
#   && apt-get update -qq \
#   && apt-get install -y dpkg-dev curl -qq \
#   && mkdir -p /opt/rebuildnginx \
#   && chmod 0777 /opt/rebuildnginx \
#   && cd /opt/rebuildnginx \
#   && su --preserve-environment -s /bin/bash -c "apt-get source nginx" _apt \
#   && apt-get build-dep -y nginx=${NGINX_VERSION} -qq \
#   && cd /opt \
#   && curl -sL https://github.com/vozlt/nginx-module-vts/archive/v${NGINX_VTS_VERSION}.tar.gz | tar -xz \
# #  && ls /opt/rebuildnginx/ \
# #  && ls /opt/rebuildnginx/nginx-${NGINX_VERSION}/ \
# #  && ls /opt/rebuildnginx/nginx-${NGINX_VERSION}/debian/ 
#   && sed -i -r -e "s/\.\/configure(.*)/.\/configure\1 --add-module=\/opt\/nginx-module-vts-${NGINX_VTS_VERSION}/" /opt/rebuildnginx/nginx-${NGINX_VERSION}/debian/rules \
#   && cd /opt/rebuildnginx/nginx-${NGINX_VERSION} \
#   && dpkg-buildpackage -b \
#   && cd /opt/rebuildnginx \
#   && dpkg --install nginx_${NGINX_VERSION}-1~stretch_amd64.deb \
#   && apt-get remove --purge -y dpkg-dev curl && apt-get -y --purge autoremove && rm -rf /var/lib/apt/lists/*

# ENTRYPOINT ["nginx-entrypoint.sh"]
# CMD ["nginx", "-g", "daemon off;"]
























# FROM alpine:3.5

# LABEL maintainer="eric@slant.co"

# ENV NGINX_VERSION 1.15.2
# ENV VTS_VERSION 0.1.18

# COPY ./nginx-entrypoint.sh /usr/local/bin/
# RUN chmod +x /usr/local/bin/nginx-entrypoint.sh

# RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl

# RUN GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \
# 	&& CONFIG="\
# 		--prefix=/etc/nginx \
# 		--sbin-path=/usr/sbin/nginx \
# 		--modules-path=/usr/lib/nginx/modules \
# 		--conf-path=/etc/nginx/nginx.conf \
# 		--error-log-path=/var/log/nginx/error.log \
# 		--http-log-path=/var/log/nginx/access.log \
# 		--pid-path=/var/run/nginx.pid \
# 		--lock-path=/var/run/nginx.lock \
# 		--http-client-body-temp-path=/var/cache/nginx/client_temp \
# 		--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
# 		--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
# 		--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
# 		--http-scgi-temp-path=/var/cache/nginx/scgi_temp \
# 		--user=nginx \
# 		--group=nginx \
# 		--with-http_ssl_module \
# 		--with-http_realip_module \
# 		--with-http_addition_module \
# 		--with-http_sub_module \
# 		--with-http_dav_module \
# 		--with-http_flv_module \
# 		--with-http_mp4_module \
# 		--with-http_gunzip_module \
# 		--with-http_gzip_static_module \
# 		--with-http_random_index_module \
# 		--with-http_secure_link_module \
# 		--with-http_stub_status_module \
# 		--with-http_auth_request_module \
# 		--with-http_xslt_module=dynamic \
# 		--with-http_image_filter_module=dynamic \
# 		--with-http_geoip_module=dynamic \
# 		--with-http_perl_module=dynamic \
# 		--with-threads \
# 		--with-stream \
# 		--with-stream_ssl_module \
# 		--with-stream_ssl_preread_module \
# 		--with-stream_realip_module \
# 		--with-stream_geoip_module=dynamic \
# 		--with-http_slice_module \
# 		--with-mail \
# 		--with-mail_ssl_module \
# 		--with-compat \
# 		--with-file-aio \
# 		--with-http_v2_module \
#                 --add-module=/usr/src/nginx-module-vts-$VTS_VERSION \
# 	" \
# 	&& addgroup -S nginx \
# 	&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
# 	&& apk add --no-cache --virtual .build-deps \
# 		gcc \
# 		libc-dev \
# 		make \
# 		openssl-dev \
# 		pcre-dev \
# 		zlib-dev \
# 		linux-headers \
# 		curl \
# 		gnupg \
# 		libxslt-dev \
# 		gd-dev \
# 		geoip-dev \
# 		perl-dev \
# 	&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o nginx.tar.gz \
# 	&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc  -o nginx.tar.gz.asc \
# 	&& curl -fSL https://github.com/vozlt/nginx-module-vts/archive/v$VTS_VERSION.tar.gz  -o nginx-modules-vts.tar.gz \
# 	&& export GNUPGHOME="$(mktemp -d)" \
# 	&& found=''; \
# 	for server in \
# 		ha.pool.sks-keyservers.net \
# 		hkp://keyserver.ubuntu.com:80 \
# 		hkp://p80.pool.sks-keyservers.net:80 \
# 		pgp.mit.edu \
# 	; do \
# 		echo "Fetching GPG key $GPG_KEYS from $server"; \
# 		gpg --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$GPG_KEYS" && found=yes && break; \
# 	done; \
# 	test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" && exit 1; \
# 	gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \
# 	&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \
# 	&& mkdir -p /usr/src \
# 	&& tar -zxC /usr/src -f nginx.tar.gz \
# 	&& tar -zxC /usr/src -f nginx-modules-vts.tar.gz \
# 	&& rm nginx.tar.gz nginx-modules-vts.tar.gz \
# 	&& cd /usr/src/nginx-$NGINX_VERSION \
# 	&& ./configure $CONFIG --with-debug \
# 	&& make -j$(getconf _NPROCESSORS_ONLN) \
# 	&& mv objs/nginx objs/nginx-debug \
# 	&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-debug.so \
# 	&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-debug.so \
# 	&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \
# 	&& mv objs/ngx_http_perl_module.so objs/ngx_http_perl_module-debug.so \
# 	&& mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \
# 	&& ./configure $CONFIG \
# 	&& make -j$(getconf _NPROCESSORS_ONLN) \
# 	&& make install \
# 	&& rm -rf /etc/nginx/html/ \
# 	&& mkdir /etc/nginx/conf.d/ \
# 	&& mkdir -p /usr/share/nginx/html/ \
# 	&& install -m644 html/index.html /usr/share/nginx/html/ \
# 	&& install -m644 html/50x.html /usr/share/nginx/html/ \
# 	&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \
# 	&& install -m755 objs/ngx_http_xslt_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \
# 	&& install -m755 objs/ngx_http_image_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \
# 	&& install -m755 objs/ngx_http_geoip_module-debug.so /usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \
# 	&& install -m755 objs/ngx_http_perl_module-debug.so /usr/lib/nginx/modules/ngx_http_perl_module-debug.so \
# 	&& install -m755 objs/ngx_stream_geoip_module-debug.so /usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \
# 	&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \
# 	&& strip /usr/sbin/nginx* \
# 	&& strip /usr/lib/nginx/modules/*.so \
# 	&& rm -rf /usr/src/nginx-$NGINX_VERSION \
# 	\
# 	# Bring in gettext so we can get `envsubst`, then throw
# 	# the rest away. To do this, we need to install `gettext`
# 	# then move `envsubst` out of the way so `gettext` can
# 	# be deleted completely, then move `envsubst` back.
# 	&& apk add --no-cache --virtual .gettext gettext \
# 	&& mv /usr/bin/envsubst /tmp/ \
# 	\
# 	&& runDeps="$( \
# 		scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so /tmp/envsubst \
# 			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
# 			| sort -u \
# 			| xargs -r apk info --installed \
# 			| sort -u \
# 	)" \
# 	&& apk add --no-cache --virtual .nginx-rundeps $runDeps \
# 	&& apk del .build-deps \
# 	&& apk del .gettext \
# 	&& mv /tmp/envsubst /usr/local/bin/ \
# 	\
# 	# forward request and error logs to docker log collector
# 	&& ln -sf /dev/stdout /var/log/nginx/access.log \
# 	&& ln -sf /dev/stderr /var/log/nginx/error.log

# #COPY nginx.conf /etc/nginx/nginx.conf

# EXPOSE 80 443

# EXPOSE 7200
# EXPOSE 9913

# #STOPSIGNAL SIGTERM

# ENTRYPOINT ["nginx-entrypoint.sh"]
# CMD "nginx"
# #CMD ["nginx", "-g", "daemon off;"]