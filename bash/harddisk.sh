#!/bin/bash
# This script is licensed under GNU GPL version 2.0 or above
# --------------------------------------------------------------------
# This script is part of linuxtuning.ru collection
# Visit https://linuxtuning.ru for more information
# --------------------------------------------------------------------
# Linux shell script to watch disk space (should work on other UNIX oses )
# set admin email so that you can get email
# Thanks to @kreon for perl part
ADMIN='mail@to'
# set alert level 90% is default
ALERT=91
df -h | grep -v Filesystem | while read output;
do
   usep=$(echo $output | awk '{ print $5}' | cut -d'%' -f1 )
   partition=$(echo $output | awk '{ print $1 " (" $6 ") " }' )
   if [ $usep -ge $ALERT ]; then
      echo "Running out of space \"$partition ($usep%)\" on $(hostname) as on $(date)" |
mail -s "Alert: Almost out of disk space $usep" $ADMIN;
        echo "$(date) Alert sent"; fi
done