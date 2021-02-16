## Directory Structure

quickstart - contains a Python script that creates a basic setup of Pretix in the deployed infrastructure, preparing it for load testing as well.

loadTesting - contains test scripts for evaluating infrastructure performance under high volumes of simultaneous requests.

monitorVM - contains the code of the virtual machine used for monitoring the entire infrastructure, resorting to Elastic Search, Kibana, Logstash and Prometheus.

infrastructure - contains all configurations (local and remote) for the distributed infrastructure that allows hosting the product.
