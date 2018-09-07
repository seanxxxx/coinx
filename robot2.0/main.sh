#!/bin/sh
ps -aux|grep doTrade|awk '{print $2}'|xargs kill -9
nohup python -u /home/zhoujiayi/robot/main.py > coinx.log 2>&1 &
sleep 5
while [ 1 ] 
do
  ps -aux|grep doTrade.py |grep -v grep
  if [ $? -ne 0 ];then
    echo "start process....."
     ps -aux|grep doTrade|awk '{print $2}'|xargs kill -9
     nohup python -u /home/zhoujiayi/robot/main.py > coinx.log 2>&1 &
     sleep 5
  else
    echo "runing....."
  fi
done