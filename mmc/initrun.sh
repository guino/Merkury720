#!/bin/sh

# Copy app partition if not already done
if [ ! -e /mnt/mmc01/home ]; then 
 MTDNUM=`cat /proc/cmdline | sed 's/.*ppsAppParts=\([0-9]\).*/\1/'`
 mount -t cramfs /dev/mtdblock$MTDNUM /opt/pps
 tar xzf /opt/pps/app.tar.gz -C /mnt/mmc01/
fi

# Now flag the hack is done
echo done > /mnt/mmc01/hack

# Try to run custom.sh
while true; do
 if [ -e /mnt/mmc01/custom.sh ]; then
  /mnt/mmc01/custom.sh
 fi
 sleep 10
done
