# source-finder
Software for finding sources in a FITS image

## Installation
Once you have cloned down this repository using `git clone` cd into the app directory eg.

```
cd source-finder
```

The project uses pipenv to manage project and development packages. To install these requirements run

```
pipenv install --dev
```

To initialise the virtual environment run

```
pipenv shell
```

To exit the virtual environment use `exit` and to see where you virtual environment is located run
`pipenv --venv` which may be useful when setting up your project interpreter in your IDE.

This project used the black auto formatter which can be run on git commit along with flake8 if you install pre-commit. To do this run the following in your terminal from within your virtual environment.

```
pre-commit install
```

Now pre-commit hooks should run on `git commit`.

You will need to create the database for the application to connect to and the relations within the database. To do this run the following commands in your terminal.

```bash
createdb source_finder
python manage.py migrate
```
