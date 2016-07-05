"""
Flask-JIRA
-------------

Flask extension that provides simple integration with JIRA REST API.
"""
from setuptools import setup


setup(
    name='Flask-JIRA',
    version='0.0.2',
    url='https://github.com/jiribires/flask-jira',
    license='MIT',
    author='Jiri Bires',
    author_email='jiri.bires@gmail.com',
    description='Flask extension that provides simple integration with JIRA REST API',
    long_description=__doc__,
    py_modules=['flask_jira'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'jira'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)