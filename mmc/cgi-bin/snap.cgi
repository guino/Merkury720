#!/bin/sh
# JPEG address (only enter the digits after 0x)
ADDRESS=2d6648
# Get ppsapp PID
PPSID=$(ps | grep -v grep | grep ppsapp | awk '{print $1}')
/mnt/mmc01/jpeg-arm /proc/$PPSID/mem $ADDRESS 57336 2> /dev/null
