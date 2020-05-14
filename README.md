# daf-monitor
Monitoring of DAF environment and devices

Running webapp
```bash
export FLASK_APP=daf-monitor.py
flask run --host 0.0.0.0
```

Optional
```bash
export FLASK_DEBUG=1
```

Using [bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/)

[wtforms](https://wtforms.readthedocs.io/en/latest/fields/#module-wtforms.fields.html5)


source roberval/dev-env-py38/bin/activate
cd roberval/daf-monitor/
source ../dotfiles/.aliases 
export FLASK_APP=daf-monitor.py
export FLASK_DEBUG=1
nedit app/routes.py app/templates/dryair.html  &
nedit app/dryair/forms.py  &


