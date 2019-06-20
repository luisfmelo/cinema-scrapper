#!/usr/bin/env bash

echo "Creating Crons..."

mkdir -p /crontab_logs

# Add necessary permissions
chmod 777 /src/

# Create Crons
echo "07 * * * * python /app/crawler.py >> /crontab_logs/crawler.log" >> mycron

# Install new cron file
crontab mycron
rm mycron

# Success
/etc/init.d/cron start

crontab -l
echo "Crons successfully installed. Type: 'crontab -e' to see."

tail -f /dev/null