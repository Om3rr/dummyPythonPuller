cd ../flaskTest/webSight
git pull
kill $(ps aux | grep port=8080 | awk '{print $2}')
export FLASK_APP=application.py
flask run --host=0.0.0.0 --port=8080 &
disown
