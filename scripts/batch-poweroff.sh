#!/bin/bash
#
# batch-poweroff.sh
#
# usage: ./batch-poweroff.sh CID1 CID2
#
cidip="$HOME/src/checkbox-message/trunk/bin/cidip"
echo "begin to shutdown and rm checkbox-autostart-desktop" 
for cid in "$@"
do
    echo "reboot $cid"
    ssh -o StrictHostKeyChecking=no ubuntu@`$cidip $cid` 'sudo apt-get purge checkbox-autostart-desktop -y; sudo shutdown -h now'
done

echo "done!"
