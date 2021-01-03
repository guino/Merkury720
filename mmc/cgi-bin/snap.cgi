#!/bin/sh
echo -e "Content-type: image/jpeg\r"
echo -e "\r"
# Get ppsapp PID
PPSID=$(ps | grep -v grep | grep ppsapp | awk '{print $1}')
# Get JPEG address
JPEGADDR=$(/mnt/mmc01/busybox dd if=/proc/$PPSID/mem bs=1 skip=$((0x2d6648)) count=4| /mnt/mmc01/busybox od -t x4 | /mnt/mmc01/busybox head -1 | awk '{print $2}')
JPEGADDR=${JPEGADDR:0:5}
/mnt/mmc01/busybox dd if=/proc/$PPSID/mem bs=4096 skip=$((0x$JPEGADDR)) count=14 | /mnt/mmc01/busybox tail -c +9
