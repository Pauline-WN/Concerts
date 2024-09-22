Concerts Project
================

Overview
--------

This project is a concert management system using SQLAlchemy and Alembic for migrations.

Project Models
--------------

The project includes the following models:

-   **Band**: Represents a musical band with attributes `id`, `name`, and `hometown`. It includes methods for:

    -   Getting associated concerts.
    -   Retrieving venues where the band performs.
    -   Scheduling a concert at a venue on a specific date.
    -   Generating introductions for concerts.
    -   Finding the band with the most performances.

-   **Venue**: Represents a concert location with attributes `id`, `title`, and `city`. It includes methods for:

    -   Getting associated concerts.
    -   Retrieving bands that perform at the venue.
    -   Finding a concert on a specific date.
    -   Identifying the most frequently performing band.
    
-   **Concert**: Represents a concert event with attributes `id`, `date`, `band_id`, and `venue_id`. It includes methods for:

    -   Getting the associated band and venue.
    -   Checking if the concert is a hometown show.
    -   Generating introductions for the audience.


Setup Instructions
------------------

### 1\. Clone the Repository

Copy code

`git clone git@github.com:Pauline-WN/Concerts.git
cd Concerts`

### 2\. Install Dependencies

Make sure you have Pipenv installed. Then run the following commands to install the required packages:

Copy code

`pipenv install
pipenv shell`

### 3\. Configure the Database

Update your `alembic.ini` file with the correct database URL in the `sqlalchemy.url` section:

Copy code

`sqlalchemy.url = sqlite:///concerts.db`

### 4\. Initialize Alembic Migrations

Before working with the models, initialize the migrations for your database.

Copy code

`alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head`

### 5\. Initialize the Database

You can initialize the database by running the `run.py` file. This will set up the schema based on your models.

Copy code

`python run.py`

This will output:

Copy code

`Database initialized!`

### 6\. Populate the Database

To add initial data to the database tables, run the `populate_db.py` script:

Copy code

`python populate_db.py`

This script will insert sample data into the `bands` table and any other relevant tables.

### 7\. Running the Application

Once the database is set up, you can start using the app. (In this project, `run.py` only initializes the database, but in a larger project, it could also start the app.)

### 8\. Running Tests

You can run the unit tests for the models to ensure everything works as expected:

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

      Copy code

    `alembic init migrations`

    This will create a `migrations/` directory containing Alembic's configuration files.

2.  **Generate Migration Files**\
    When you make changes to your models (e.g., adding a new table or modifying a column), generate a migration script using the `--autogenerate` flag:

      Copy code

    `alembic revision --autogenerate -m "Your migration message"`

3.  **Apply Migrations**\
    To apply the migration and update the database schema, run:

     Copy code

    `alembic upgrade head`

4.  **Check Database Version**\
    If you need to check the current state or version of the database, you can run:

       Copy code

    `alembic current`

### Rolling Back Migrations

If needed, you can roll back the last migration by running:

Copy code

`alembic downgrade -1`