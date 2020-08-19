# flask-creator

flask-creator is a CLI for creating Flask application easily.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install flask-creator
pip3 install flask-creator
```


## Usage

```bash
flask-creator create --app appName # create a new flask application 

flask-creator create --page pageName # create a basic html page 

flask-creator run # run your flask application (1)

flask-creator install # install the dependencies specified in the setup.py of your application

flask-creator generate --require # create the requirements.txt of your application 
```

## New project directory tree 

```
├── example
│   ├── __init__.py
│   └── pages
│       └── index.html
├── Procfile
├── requirements.txt
├── run.sh
├── setup.py
└── venv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://github.com/MOSvisio/flask-creator/blob/master/LICENCE)
