# Bungalow

Simple Django REST Framework API for property listings.

## Setup

Project is set up using Docker and Python 3.7. [Poetry](https://github.com/sdispater/poetry) is used for dependency management because it is the only python dependency management tool that I do not hate LOL.

## Design

I have broken down the design into 3 models.

1. `Listing`: A property for sale with the permanent data (address, size, rooms etc etc) and current price.
1. `SaleHistory`: The previous sale price (if available). From the sample data, it appears like we might only have one record, but this is a little bit a future proofing. For example, we might support more import data times that might include more historical data about the listing. (Think of house sigma).
1. `Metadata`: Contains all the "extra" (estimates on rent, tax data) data about the listing. I designed it so that we could actually have multiple metadata sources, but for the sake of time, we currently only support Zillow. I could have made this a bit more robust and allowed for variable columns, but I didn't want to make too many assumptions. Once multiple sources are add, to would be better revisit this design.

In truth, I could have just created a fat model with all the data in it, which would just reflect the CSV import, but I wanted to show off my relationship skills ^_^. 

### Assumptions

1. Table relationships were desired.
1. We are only dealing with US properties (limiting this due to time constraints)
1. Columns which include `z`, ie `rentzestimate_amount`, is metadata provided by Zillow.
1. The Django command should not use the API to create the DB records, this way you do not need an instance of the app running to run the command.

### Running the App

`docker-compose up app` 

If it is the 1st time running the app, you will need to run the migrations, `make db.migrate` has got you covered.

Also see the Makefile for other commands to make like easier ^_^. (I am not a fan of make, but at least I know it's installed on your system)

Notes:

1. You need Docker & docker-compose installed (duh!)

1. Because of Docker, on your system (the host) the URL is http://localhost:8000/ and *not* the URL displayed in the console (http://0.0.0.0:8000/).

### Importing the Sample Data

The Django command to import data is... `python manage.py import_data FILENAME`.
I have a sample CSV in `.data/imports/sample.py`.

`docker-compose run --entrypoint "python manage.py import_data .data/imports/sample.py" app`

or you can run `make db.seed` :)
