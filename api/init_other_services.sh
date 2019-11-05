#!/usr/bin/env bash

cd ..
docker-compose up -d mqtt crawler redis couchdb db
docker exec -it cinema-scrapper_crawler_1 python3 crawler.py