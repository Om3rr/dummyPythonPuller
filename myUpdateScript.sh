cd ../flaskTest/webSight
git pull
kill $(ps aux | grep 'application.py' | awk '{print $2}')
python application.py --host=0.0.0.0 --port=8080
