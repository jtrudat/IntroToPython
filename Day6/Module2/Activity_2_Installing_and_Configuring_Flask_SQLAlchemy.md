# Activity: Installing and Configuring Flask-SQLAlchemy

In the previous activities, we set PetFax up to let users submit their own fun animal facts to the shelter. All we were missing was a database. Now that we've covered the tools to integrate a database into a Flask application, we can start making it more functional! In this activity, we will create our Postgres database for PetFax and then install and configure Flask-SQLAlchemy to connect to that database.

## Getting Started

1. Open your terminal.
2. Navigate to [Day5/PetFax](../PetFax).
3. Open it in your code editor of choice.
4. Create the virtual environment if it does not exist.
   - `python3 -m venv venv`
5. Activate the virtual environment by running the command below for your operating system.
   - MacOS -> `. venv/bin/activate`
   - Windows -> `& .\venv\Scripts\Activate.ps1`
6. Run the app with `flask run --reload`.

## Creating the Database

Before we do anything inside our app, let's create our database. This will give SQLAlchemy something to connect to later on.

### In terminal or pgAdmin

1. Decide your preferred method of creating the Postgres database: psql through terminal or the pgAdmin application.
2. Create a database named `petfax`.
3. Take note of the connection string, which by default should be:
   - `postgresql://username:password@localhost:5432/petfax`
   - Where username and password are replaced with your own credentials.
   - Remember, if you never set up a username or password, the default is `postgres` for both.

That's all we need to do for now. We will create our tables using the ORM later on. With the database created, we can now get started with Flask-SQLAlchemy!

## Installing Flask-SQLAlchemy

Installing the ORM is fairly simple since it can be installed through pip.

### In terminal

1. Be sure you are at the root of the [Day5/PetFax](../PetFax) directory inside the activated virtual environment.
2. Install Flask-SQLAlchemy with pip.
   - Note: The package name is `flask_sqlalchemy`

#### What your terminal should look like

```powershell
pip install flask_sqlalchemy
```

## Configuring Flask-SQLAlchemy

With the package installed, we can get to configuration. A lot of it will be done within our Petfax `__init__.py` file, but later we will also be creating a new file that will house the SQLAlchemy instance.

First, let's set configuration variables on our app instance.

### __init__.py

1. Set a variable named `SQLALCHEMY_DATABASE_URI` on the app instance's config object.
2. Set its value to the connection string of our database, which we noted earlier.
3. While we're at it, let's also set a variable named `SQLALCHEMY_TRACK_MODIFICATIONS` on the app's config object to False.
   - What does this do? If set to `True`, it will track modifications of objects, as the name suggests. We don't need this feature, so we should set it to `False`.
   - Why are we manually setting it to `False`? When left unset, its value defaults to `None`, which requires extra memory.

#### What your code should look like

```python
# factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']        = 'postgresql://username:password@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

Now we need to create the SQLAlchemy instance. As we just learned, the SQLAlchemy class is what holds all the ORM functionality that we will need in the future. This includes the method to connect our app to a database.

Technically, we could create the instance within our app factory method. However, just as with blueprints, it's preferable to modularize logic into other files and import them into the factory. If we created the instance within the app factory, we would only be able to use it within the factory.

With all that said, it's clear the best choice here is to create a new file to house the SQLAlchemy instance. That way, we can import it into the factory and into any other file that may need it later.

### petfax/models.py

1. Create a file named `models.py` within the `PetFax` folder.
   - Why "models"? It's the conventional name and we will be creating our model within this file later on.
2. At the the top of that file, import the `SQLAlchemy` class from the `flask_sqlalchemy` package.
3. Underneath, set a variable named `db` to a new instance of the `SQLAlchemy` class.

#### What your code should look like

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### petfax/__init__.py

Now that we've created the SQLAlchemy instance, we can import it within `__init__.py`.

1. Open the `__init__.py` file.
2. Within the factory method, underneath the app.config variables, import the `models` folder we just created.
3. We now have access to all the built-in SQLAlchemy class methods through `models.db`. Call the `init_app` method on it and pass it the app instance.

#### What your code should look like

```python
# database config
app.config['SQLALCHEMY_DATABASE_URI']        = 'postgresql://username:password@localhost:5432/petfax'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from . import models
models.db.init_app(app)
```

## Creating a Model

Let's create our model within the `models.py` file.

### models.py

1. Create a class named `Fact`.
2. Have the class inherit the built-in SQLAlchemy `Model` class.
   - Think: how would access this built-in class? Don't forget, we created an instance of `SQLAlchemy`.
3. Inside the class, set the `__tablename__` to the desired table name. In this case, let's name it `facts`.
4. Underneath that, set up all the columns with the following datatypes:
   - `id`: Integer. It should be the primary key column.
   - `submitter`: String with a character limit of 250.
   - `fact`: Text.

#### What your code should look like

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ =  'facts'

    id        = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    fact      = db.Column(db.Text)
```

**Note:** If you desire better file organization, you could create separate files for each model and import them into `models.py`. For simplicity, we will stick with a singular `models.py` file.

Now that we've created our first model, when the app runs, the table should be created within our database... right? Try it. Make sure your Flask app is still running correctly, then check your database to see if the facts table has been created.

As you can see, it has not. In order to actually make any changes to our database's tables, we have to migrate them.

Migrating our Changes
As we learned, Flask SQLAlchemy unfortunately does not have built-in migration tools. That's fine, because we also learned about another package named `Flask-Migrate` that does have migration tools.

### In terminal

1. Install the package through pip. Note that its package name is capitalized and hyphenated as `Flask-Migrate` during installation.
2. We also have to install a Postgres database adapter, `psycopg2-binary`.
   - This package will allow our Python application to work with Postgres.
   - Visit the [package's page on PyPi](https://pypi.org/project/psycopg2-binary/) for more information.

```powershell
pip install Flask-Migrate
pip install psycopg2-binary
```

### __init__.py

1. Import the `Migrate` class from the package. Note that within Python, the package name is lowercased and underscored as `flask_migrate`.
2. Underneath all our database configuration, set a variable called `migrate` to a new instance of the `Migrate` class.
3. Pass the `Migrate` class two arguments:
   - First, pass the Flask app instance.
   - Second, pass the SQLAlchemy instance.

#### What your code should look like

```python
# config
# [ ... ]
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)

    # database config
    # [ ... ]
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # [ ... ]
```

Now we have access to some Flask migration tools.

### In terminal

1. Make sure you're within a virtual environment at the root of the `petfax` directory.
2. Initialize a migrations folder by running `flask db init`.
3. Create the migration script by running `flask db migrate`. This will automatically detect any relevant changes.
   - Note: If you get a `KeyError` here for "formatters", you may have installed the wrong package. Remember to install `Flask-Migrate`, not ~~flask_migrate~~, when installing through pip. If you've done so, simply delete the `migrations` folder, install the correct package, and then start from step two of this section again.
4. Apply the migration script to the database by using the `flask db upgrade` command.
5. Now we can check our database and we will see that the facts table has been created!

#### What your terminal should look like

```powershell
flask db init
flask db migrate
flask db upgrade
```

Now that we've initialized the migrations folder, the only scripts we need to run in this app to apply future database changes are:

- `flask db migrate`
- `flask db upgrade`

## Conclusion

We've finally connected a database to our app! This opens up so much more functionality that can be added to our application. This allows us to finish up the new facts page. In the next lesson, we'll learn how to query from and insert data into the database.
