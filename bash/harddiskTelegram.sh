#!/bin/bash

BotToken='...'
chatid="..."
sendTo="..."

diskName=/dev/vda1
minFree=10485760 #1Gb

freeSpace=`df  | grep /dev/vda1 | awk '{ print $4 }'`
echo $freeSpace'-'$minFree
if [ $freeSpace -lt $minFree ]
   then
      h=`hostname -f`
      fs=`df -h | grep ${diskName} | awk '{ print $4 }'`
      msg="FREE SPACE $fs  on server $h"
      curl -s -X POST https://api.telegram.org/bot$BotToken/sendMessage -d chat_id=$chatid --data-urlencode "text=$msg" > /dev/null

      echo $msg | mail -s 'Free spece' $sendTo