#!/bin/bash
echo "Stopping services"
docker rm external -f
docker rm danno_vu_service -f
docker rm dema_vu_service -f
echo "Removing local network"
docker network rm ws_bridge
docker network rm webservice_ws_bridge
echo "Clearing empty images"
docker rmi $(docker images --filter dangling=true -q --no-trunc)
echo "Done"