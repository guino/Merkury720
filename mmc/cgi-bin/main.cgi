#!/bin/sh
echo -en "Content-Type: text/plain\r\n\r\n"
/mnt/mmc01/busybox ls -a -Xp ..${REQUEST_URI#${SCRIPT_NAME}}
