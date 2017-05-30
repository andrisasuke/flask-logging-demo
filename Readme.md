Flask Logging Demo
- How to log (info, debug, error) into file.log and console (for both `python run` and `gunicorn run`)

1. $> virtualenv venv
2. $> source venv/bin/activate; pip install -r requirements.txt;
3. $> pip install gunicorn 
4. Run as standalone server : $> python run.py
5. Run as wsgi : $> gunicorn run:app -b localhost:5000
6. curl http://127.0.0.1:5000/log
7. Then logging will appear in `app.log` and console log. :)