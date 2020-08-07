# randomuser_statistics
Intern task

## Project Setup

- Create virtualenv `python -m venv venv` and then activate it
- install requirements `pip install -r requirements.txt`

## Create database

- run `py database_handler.py`

## Fill database

- run `py data_loader.py`

## Usage

###### Return percentage value of male and female in database
- run `py main.py -p`

###### Return average for all, male or female
- run `py main.py -a all / male / female`

###### Return most popular cities
- run `py main.py -c number`


###### Return most popular passwords
- run `py main.py -pass number`

###### Return users who are born between given 2 dates
- run `py main.py -d YYYY-MM-DD YYYY-MM-DD`

###### Return passwords with the highest score
- run `py main.py -b`
