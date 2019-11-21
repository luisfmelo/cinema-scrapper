#!/usr/bin/env bash

cd ..
docker-compose down
docker-compose up --build -d mqtt crawler redis couchdb db normalizer
docker exec -it cinema-scrapper_crawler_1 python3 crawler.py