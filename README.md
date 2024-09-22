Concerts Project
================

Overview
--------

This project is a concert management system using SQLAlchemy and Alembic for migrations.

Setup Instructions
------------------

### 1\. Clone the Repository

bash

Copy code

`git clone git@github.com:Pauline-WN/Concerts.git
cd Concerts`

### 2\. Install Dependencies

Make sure you have Pipenv installed. Then run the following commands to install the required packages:

bash

Copy code

`pipenv install
pipenv shell`

### 3\. Configure the Database

Update your `alembic.ini` file with the correct database URL in the `sqlalchemy.url` section:

ini

Copy code

`sqlalchemy.url = sqlite:///concerts.db`

### 4\. Initialize Alembic Migrations

Before working with the models, initialize the migrations for your database.

bash

Copy code

`alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head`

### 5\. Initialize the Database

You can initialize the database by running the `run.py` file. This will set up the schema based on your models.

bash

Copy code

`python run.py`

This will output:

Copy code

`Database initialized!`

### 6\. Populate the Database

To add initial data to the database tables, run the `populate_db.py` script:

bash

Copy code

`python populate_db.py`

This script will insert sample data into the `bands` table and any other relevant tables.

### 7\. Running the Application

Once the database is set up, you can start using the app. (In this project, `run.py` only initializes the database, but in a larger project, it could also start the app.)

### 8\. Running Tests

You can run the unit tests for the models to ensure everything works as expected:

bash

Copy code

`python -m unittest discover`

Additional Notes
----------------

### Database Setup

This project uses **SQLite** as the database. The database file, named `concerts.db`, will be created automatically in the project directory when you initialize the database using SQLAlchemy.

### Alembic Migrations

Alembic is used for database migrations to manage changes to the database schema. Follow these steps to use Alembic for migrations:

1.  **Initialize Alembic**\
    After installing the dependencies, run the following command to initialize Alembic in your project:

    bash

    Copy code

    `alembic init migrations`

    This will create a `migrations/` directory containing Alembic's configuration files.

2.  **Generate Migration Files**\
    When you make changes to your models (e.g., adding a new table or modifying a column), generate a migration script using the `--autogenerate` flag:

    bash

    Copy code

    `alembic revision --autogenerate -m "Your migration message"`

3.  **Apply Migrations**\
    To apply the migration and update the database schema, run:

    bash

    Copy code

    `alembic upgrade head`

4.  **Check Database Version**\
    If you need to check the current state or version of the database, you can run:

    bash

    Copy code

    `alembic current`

### Rolling Back Migrations

If needed, you can roll back the last migration by running:

bash

Copy code

`alembic downgrade -1`