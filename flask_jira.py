# -*- coding: utf-8 -*-
from jira import JIRA

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class FlaskJIRA(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        app.config.setdefault('JIRA_SERVER', None)
        app.config.setdefault('JIRA_OPTIONS', None)
        app.config.setdefault('JIRA_BASIC_AUTH', None)
        app.config.setdefault('JIRA_OAUTH', None)
        app.config.setdefault('JIRA_JWT', None)

    def __getattr__(self, item):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'jira'):
                ctx.jira = JIRA(server=ctx.app.config.get('JIRA_SERVER'),
                                options=ctx.app.config.get('JIRA_OPTIONS'),
                                basic_auth=ctx.app.config.get('JIRA_BASIC_AUTH'),
                                oauth=ctx.app.config.get('JIRA_OAUTH'),
                                jwt=ctx.app.config.get('JIRA_JWT'))


            return getattr(ctx.jira, item)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'jira'):
            ctx.jira = None