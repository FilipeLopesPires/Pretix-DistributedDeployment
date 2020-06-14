from flask import Flask, request
import yaml
import json
import logging
import docker
import os

os.environ["DOCKER_HOST"]="tcp://10.2.0.1:2375"
logging.basicConfig(filename='/var/log/alertAndIp',level=logging.DEBUG)

app = Flask(__name__)
client=docker.from_env()

snmp={}

redisslave={}
redismaster={}
redissentinel={}
redisproxy={}
web={}
nginx={}
pg0={}
pg1={}
pg2={}

# pg0:            -       7259
# pg1:            -       7258
# pg2:            -       7257
# pgpool:         7232    7256
# redisproxy:     7279    7255
# redismaster:    -       7254
# redisslave:     -       7253
# redissentinel:  -       7252
# web:            7201    7251
# nginx:          7200    7250

def dockerScaleServiceUp(service):
    serviceName="pretix_"+service
    dockerService=client.services.get(serviceName)
    if(dockerService.scale(len(eval(service))+1)):
        logging.warning("Service "+ service+" scaled up with success.")


def dockerScaleServiceDown(service):
    serviceName="pretix_"+service
    dockerService=client.services.get(serviceName)
    if(dockerService.scale(len(eval(service))-1)):
        logging.warning("Service "+ service+" scaled down with success.")

def changeTargets(service):
    file=open("/etc/prometheus/exporters/"+service+"_targets.json", "w")
    file.write(json.dumps([{"targets":list(set(eval(service).values()))}]))
    file.close()

def updateExporters(serviceType, replica, ip):
    if serviceType=="pretix_redisslave":
        redisslave[replica]=ip+":7253"
    elif serviceType=="pretix_redissentinel":
        redissentinel[replica]=ip+":7252"
    elif serviceType=="pretix_redismaster":
        redismaster[replica]=ip+":7254"
    elif serviceType=="pretix_redisproxy":
        redisproxy[replica]=ip+":7255"
    elif serviceType=="pretix_web":
        web[replica]=ip+":7200"
    elif serviceType=="pretix_nginx":
        nginx[replica]=ip+":7250"
    elif serviceType=="pretix_pg0":
        pg0[replica]=ip+":7259"
    elif serviceType=="pretix_pg1":
        pg1[replica]=ip+":7258"
    elif serviceType=="pretix_pg2":
        pg2[replica]=ip+":7257"
    changeTargets(serviceType.split("_")[1])


@app.route('/service', methods=["POST"])
def receiveServiceIP():
    remoteIp=request.remote_addr
    data=json.loads(request.data)
    logging.warning(remoteIp+" Received: "+str(data))
    tmp=data["service"].split(".")
    srvc=tmp[0].replace("-","")+"."+tmp[1]
    snmp[srvc]=remoteIp
    changeTargets("snmp")
    updateExporters(tmp[0].replace("-",""), tmp[1], remoteIp)
    return ''

@app.route('/alert', methods=["POST"])
def receiveAlert():
    data=json.loads(request.data)
    logging.warning("Received Alert: "+str(data))
    rule=data["ruleName"]
    state=data["state"]
    if state=="alerting":
        if rule in ["NGINX-Pretix Response Time alert","PRETIX-Number of Events alert[test]","PRETIX-Order POST Time Distribution alert"]:
            logging.warning("Scaling up service 'web'")
            dockerScaleServiceUp("web")
        elif rule in ["REDIS-# Connected Clients alert", "HAPROXY-Proxy Average Response Time of Redis alert"]:
            logging.warning("Scaling up service 'redisslave'")
            dockerScaleServiceUp("redisslave")
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)