kill $(ps aux | grep 'application.py' | awk '{print $2}')
screen -r app
git pull
python application.py &
screen -d
