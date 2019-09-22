# Bungalow

Simple Django REST Framework API for property listings.

## Setup

Project is set up using Docker and Python 3.7. [Poetry](https://github.com/sdispater/poetry) is used for dependency management because it is the only python dependency management tool that I do not hate LOL.

### Running the API

`docker-compose up app`

Notes:
1. You need Docker & docker-compose installed (duh!)

1. Because of Docker, on your system (the host) the URL is http://localhost:8000/ and *not* the URL displayed in the console (http://0.0.0.0:8000/).

### Importing the Sample Data

TODO: This will be a Django command.
