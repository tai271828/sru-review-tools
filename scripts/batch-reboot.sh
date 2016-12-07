#!/bin/bash
#
# batch-reboot.sh
#
# usage: ./batch-reboot.sh CID1 CID2
#
cidip="$HOME/src/checkbox-message/trunk/bin/cidip"
time_interval=600
#time_interval=1200
echo "begin to reboot with time interval $time_interval secs" 
for cid in "$@"
do
    echo "reboot $cid"
    ssh -o StrictHostKeyChecking=no ubuntu@`$cidip $cid` 'sudo reboot'
    sleep $time_interval
done

echo "done!"
