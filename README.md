# flask-jira
Flask extension that provides simple integration with JIRA REST API

## Usage

In order to install:
```
pip install Flask-JIRA
```

In your main app file:
```
from flask import Flask
from flask_jira import FlaskJIRA

app = Flask(__name__)
jira = FlaskJIRA(app)
```

If you're following the [Application Factories](http://flask.pocoo.org/docs/0.10/patterns/appfactories/) pattern:
```
from flask import Flask
from flask_jira import FlaskJIRA

jira = FlaskJIRA()

app = Flask(__name__)
jira.init_app(app)
```

Now that you have the ```jira``` object, you can perform Jira API requests. To read more about how to do that, see [Python JIRA](https://pythonhosted.org/jira/#).


## Customizing Properties

In order to customize the connection properties, add the following options into your app.config (see [Configuration Handling](http://flask.pocoo.org/docs/0.10/config/) for more details):
```
JIRA_SERVER 
JIRA_OPTIONS 
JIRA_BASIC_AUTH 
JIRA_OAUTH 
JIRA_JWT 
```

All options are documented in [Python JIRA API](https://jira.readthedocs.io/en/latest/api.html#jira).