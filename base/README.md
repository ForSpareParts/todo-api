todo API
========


This project is a RESTful web service that tracks todo items, with optional due
dates, for users.

Available endpoints include:

* `/users/` (accepts GET and POST)
* `/to-dos/` (accepts GET and POST)
* `/users/:id` (accepts GET and PUT)
* `/to-dos/:id` (accepts GET and PUT)

The `/to-dos/` endpoint also accepts the following filter parameters on GET:

* `user` (the ID of a user to filter on)
* `is_completed` (true or false)


Data Format
-----------

The API uses a datatype of `application/json`, with the following formats.

For users:

    {
        "id": 1
        "username": "jdoe",
        "email": "john.doe@example.com",
    }


For todo items:

    {
        "id": 1,
        "title": "do stuff",
        "user": 1,
        "completed_on": '2015-08-01T00:00:00-05:00',
        "due_date": '2015-08-02T00:00:00-05:00'
    }

Note that `completed_on` and `due_date` are optional, and that the `id` field
cannot be specified or changed -- it is read-only.


Running the Project
-------------------

The API is a Django project that requires Python 2.7. To run the API, after
cloning,

1. `cd` to the project directory.
2. `pip install -r requirements.txt` (installs project dependencies -- ideally,
    this should be done in a [virtualenv](https://virtualenv.pypa.io/en/latest/), but it's technically not necessary)
3. `./manage.py migrate` (creates the SQLite3 database file)
4. `./manage.py runserver` (starts the server on localhost:8000)


Running the Tests
-----------------

To run the API's test suite, run `./manage.py test` from the project directory.
To ensure dependencies are met, follow the instructions in Running the Project,
above, before running the tests.

