# acs-django
Testing django 2.1 with postgresql database
# Installation guide
Create virtualenv inside the project root directory
```
$ virtualenv -p <python-version> ve
```
Activate virtualenv and install dependences
```
$ source ve/bin/activate
$ pip install -r requirements.txt
```
Edit database settings in `src/acs/settings.py`

Run migrations
```
$ puthon src/manage.py migrate
```
Run server
```
$ python src/manage.py runserver
```

