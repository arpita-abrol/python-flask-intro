# python-flask-intro
Introductory Material for Learning Python Flask

## Requirements
Python 3, pip

## Setup

Using the command line, first ```cd``` into the project folder. Please make sure to check that you use the specified commands for your OS.

First, create the virtual environment (```venv```). This only needs to be done the first time you run the project.

```
python -m venv venv
py -3 -m venv venv (Windows)
```

Next, we will activate the virtual enviroment

```
. venv/bin/activate
venv\Scripts\activate (Windows)
```

Now, let's install needed libraries to the virtual environment. This only needs to be done when the ```venv``` is first created or when ```requirements.txt``` is updated.

```
pip install -r requirements.txt
```

If you do not have a ```requirements.txt```, you can instead do ```pip install flask```.

Now, it is time to run our project.

```
export FLASK_APP=server.py
set FLASK_APP=server.py (Windows)
$env:FLASK_APP = "server.py" (Windows Powershell)
```

And finally.

```
flask run
```

In the terminal, you'll be able to view a link to your project on localhost.

NOTE: While developing, it may help to auto-refresh without needing to stop Flask from running. You can do this by enabling development mode
```
export FLASK_ENV=development
set FLASK_ENV=development (Windows)
```
