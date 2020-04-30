# To Run Locally:
# docker run -p 7289:8089 --name=pretixlocust -d -e TARGET_URL=http://10.2.0.1:7200 -e USERS=400 -e TOKEN=g6ohu79cix5111huvhs63ksjdvxsis6aksijlptpy3y1ffaie8re7xskkg43vkjc locust


# To Run Remotly:
# docker run -p 7289:8089 --name=pretixlocust -d -e TARGET_URL=http://10.2.0.1:7200 -e USERS=400 -e TOKEN=g6ohu79cix5111huvhs63ksjdvxsis6aksijlptpy3y1ffaie8re7xskkg43vkjc 10.2.0.1:5000/pretixlocust

FROM locustio/locust
ADD locustfile.py locustfile.py
