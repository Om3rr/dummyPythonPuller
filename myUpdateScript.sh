cd ../flaskTest
git pull
kill $(ps aux | grep port=80 | awk '{print $2}')
export FLASK_APP=application.py
flask run --host=0.0.0.0 --port=80 &
disown
