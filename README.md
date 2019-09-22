# Bungalow

Simple Django REST Framework API for property listings.

## Setup

Project is set up using Docker and Python 3.7. [Poetry](https://github.com/sdispater/poetry) is used for dependency management because it is the only python dependency management tool that I do not hate LOL.

## Design

I have broken down the design into 3 models.

1. `Listing`: A property for sale with the permanent data (address, size, rooms etc etc) and current price.
1. `SaleHistory`: The previous sale price (if available). From the sample data, it appears like we might only have one record, but this is a little bit a future proofing. For example, we might support more import data times that might include more historical data about the listing. (Think of house sigma).
1. `Metadata`: Contains all the "extra" (estimates on rent, tax data) data about the listing. I designed it so that we could actually have multiple metadata sources, but for the sake of time, we currenly only support Zillow. I could have made this a bit more robust and allowed for variable columns, but I didn't want to make too many assumptions. Once multiple sources are add, to would be better revisit this design.

In truth, I could have just created a fat model with all the data in it, which would just reflect the CSV import, but I wanted to show off my relationship skills ^_^.

### Assumptions

1. Table relationships were desired.
1. We are only dealing with US properties (limiting this due to time constraints)
1. Columns which include `z`, ie `rentzestimate_amount`, is metadata provided by Zillow.
1. The Django command should not use the API to create the DB records, this way you do not need an instance of the app running to run the command.


### Running the API

`docker-compose up app`

Notes:

1. You need Docker & docker-compose installed (duh!)

1. Because of Docker, on your system (the host) the URL is http://localhost:8000/ and *not* the URL displayed in the console (http://0.0.0.0:8000/).

### Importing the Sample Data

TODO: This will be a Django command.
