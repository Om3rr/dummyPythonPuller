kill $(ps aux | grep 'application.py' | awk '{print $2}')
sleep 1
screen -r app
sleep 1
git pull
sleep 1
python application.py &
sleep 1
screen -d
