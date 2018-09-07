ps aux | grep main.sh | awk '{print $2}'|xargs kill -9
sleep 5
ps aux | grep doTrade | awk '{print $2}'|xargs kill -9