# GIC - Computational Infrastructures Management

## University of Aveiro | DETI | Course Project Repository

## Authors:

Filipe Pires (85122)

João Alegria (85048)

## Description:

This repository contains de work developed by the authors for the discipline of Computational Infrastructures Management.
The aim of the project is to deploy and manage a distributed product of an already existing open-source solution.
The system will have a fully-automatic deployment pipeline and will be fault tolerant.
We provide reports on the work developed, the source code and the respective documentation.

The product provided is Pretix (https://github.com/pretix/pretix), a ticket shop application for conferences, festivals, tech events, etc.
Persistence is done using a PostgreSQL cluster, caching using a Redis cluster and communications with the product resort to Pretix's REST API.
Load balancing is done with NGinX implemented both inside Pretix and outside to distribute load amongst a set of endpoints.
The deployed service is hosted in a Docker Compose Swarm.

## Repository Structure

docs - contains all documentation (presentation and reports).

pretix - contains containers' configurations, performance evaluation scripts and a quickstart script.

## Deployment Instructions

[Under construction]

