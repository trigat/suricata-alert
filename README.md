# Suricata Alert
Parse through end of Suricata log and e-mail alerts.

# How to use

### Save surialert.py to Suricata server and create cron job

```
# RUN EVERY 5 MINUTES
# Save to /etc/crontab

PATH=/sbin:/bin:/usr/sbin:/usr/bin
SHELL=/bin/sh

*/5 * * * * root cd /var/log/suricata && /usr/bin/python3 /var/log/suricata/surialert.py
```
