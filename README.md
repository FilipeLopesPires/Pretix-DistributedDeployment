# Distributed Deployment and Management of <br /> [Pretix - a Ticket Shop Application](https://github.com/pretix)

## Description

This project allows the deployment and management of a distributed open-source product.
The product provided is [Pretix](https://github.com/pretix/pretix), a ticket shop application for conferences, festivals, tech events, etc.
The system has a fully-automatic deployment pipeline and is fault tolerant.
We provide reports on the work developed, the source code and the respective documentation.

Persistence is done using a PostgreSQL cluster, caching using a Redis cluster and communications with the product resort to Pretix's REST API.
Load balancing is done with NGinX implemented both inside Pretix and outside to distribute load amongst a set of endpoints.
The deployed service is hosted in a Docker Compose Swarm.

## Repository Structure

docs - contains all documentation (presentation and reports).

pretix - contains containers' configurations, performance evaluation scripts and a quickstart script.

## Additional Resources

![InfrastructureArchitecture](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/diagrams/InfrastructureArchitecture.png)

Diagram of the infrastructure architecture deployed in Docker Swarm.

![Kibana](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/kibana.png)

Populated Kibana GUI.

![Grafana](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/home.png)

Grafana Custom Home Dashboard.

![Pretix](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixServiceDashboard.png)

Populated Pretix Service Dashboard.

![Redis1](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixRedisDashboard.png)

![Redis2](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixRedis2Dashboard.png)

Populated Redis Dashboard.

![PostgreSQL](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixPostgresDashboard.png)

Populated PostgreSQL Dashboard.

![Nginx](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixNginxDashboard.png)

Populated Nginx Dashboard.

![SNMP1](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixSnmpDashboard.png)

![SNMP2](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/pretixSnmp2Dashboard.png)

Populated SNMP Dashboard.

![Teams](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/images/alerts.png)

Microsoft Teams alert examples.

## Authors

The authors of this repository are Filipe Pires and João Alegria, and the project was developed for the Computational Infrastructures Management Course of the Master's degree in Informatics Engineering of the University of Aveiro.

For further information, please read our [report](https://github.com/FilipePires98/GIC/blob/master/docs/reports/FinalReport/report.pdf) or contact us at filipesnetopires@ua.pt or joao.p@ua.pt.


