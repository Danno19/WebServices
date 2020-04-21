#!/bin/bash
# Create custom local network
docker network create ws_bridge
# Run Danno Movie WebService
docker-compose up --build -d
# Run DeMa Book WebService
cd dema4638
docker-compose up --build -d
