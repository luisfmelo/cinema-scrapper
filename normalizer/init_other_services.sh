#!/usr/bin/env bash

cd ..
docker-compose down
docker-compose up -d --build mqtt crawler redis couchdb db go_api nginx
docker exec -it cinema-scrapper_crawler_1 python3 crawler.py