## Django REST API CRUD Tutorial
A repository that helps to kickstart [Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.10.0
- Django 4.1.2
- djangorestframework 3.14.0

## Features

- Create Movie
- List Movies
- Update Movie
- Delete Movie


## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```


## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/` | GET | READ | Get all movies
`/get-movie/:id` | GET | READ | Get a single movie
`/add/`| POST | CREATE | Create a new movie
`/update/` | PUT | UPDATE | Update a movie
`/delete/:id` | DELETE | DELETE | Delete a movie

## Use
We can test the API using use [Postman](https://www.postman.com/)

Postman is a user-friendly API testing Application.

First, we have to start up Django's development server.

## Running the Application

Create the DB tables first:
```
python manage.py makemigrations
python manage.py migrate
```
Run the development web server:
```
python manage.py runserver 8080
```

Open the URL http://localhost:8080/ with test APIs.

## Get List of Movies

### Request

`GET /`

    http://localhost:8080/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 OCT 2022 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 74

    [
    {
        "id":1,"
        name":"Wolf Of The Wallstreet",
        "description":"Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living
        the high life to his fall involving crime, corruption and the federal government."
    },
    {
        "id":2,"
        name":"Fight Club",
        "description":"An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more."
    },
    {
        "id":3,"
        name":"Avengers: Infinity War",
        "description":"The Avengers and their allies must be willing to sacrifice all in an attempt to defeat 
        the powerful Thanos before his blitz of devastation and ruin puts an end to the universe."
    },

    ]


## Create a Movie

### Request

`POST /add/`

Key |Value | Description
-- | -- |--
`id` | 1 | Id of movie
`name` | Wolf Of The Wallstreet | Movie Name
`description` | Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.|description of the movie


    http://localhost:8080/add/

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 OCT 2022 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /add/1
    Content-Length: 36

    {
        "id":1,"
        name":"Wolf Of The Wallstreet",
        "description":"Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living
        the high life to his fall involving crime, corruption and the federal government."
    }


## Get a Movie

### Request

`GET /get-movie/id/`

    http://localhost:8080/get-movie/1/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 OCT 2022 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {
        "id":1,"
        name":"Wolf Of The Wallstreet",
        "description":"Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living
        the high life to his fall involving crime, corruption and the federal government."
    }


## Update Movie

### Request

`PUT /update/`


Key |Value | Description
-- | -- |--
`id` | 3 | Id of movie
`name` | Avengers: Endgame | Movie Name
`description` | After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.|description of the movie

    http://localhost:8080/1/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 OCT 2020 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 40

    {
        "id":3,
        "name":"Avengers: Endgame",
        "description":"After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. 
        With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to 
        the universe."
    }


## Delete a Movie

### Request

`DELETE /delete/id/`

    http://localhost:8080/delete/1/

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 24 OCT 2022 12:36:32 GMT
    Status: 204 No Content
    Connection: close


## Authors

- [@adnankattekaden](https://www.github.com/adnankattekaden)

