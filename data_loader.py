import requests
import requests.exceptions
from datetime import date
from database_handler import Person


class DataLoader:

    def get_data(self):

        #if you want to get more users, change value in link
        persons = requests.get("https://randomuser.me/api/?results=100")
        if persons.status_code == 200:

            data = persons.json()

            results = data['results']
            print('Data are adding to database...')
            self.load_data_to_database(results)
        else:
            print('Something went wrong')

    def fix_date_of_birth(self,date):
        return date[0:10]


    def fix_cell_phone(self,cellphone):
        return cellphone \
            .replace('-', '') \
            .replace('(', '') \
            .replace(')', '') \
            .replace(' ', '')


    def days_to_birthday(self,given_date):
        cleared_date = given_date[0:10]
        splitted_date = cleared_date.split('-')
        born_date = date(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2]))
        today = date.today()

        if born_date.month >= today.month:
        # if month of birth is higher or the same as current month, create new date (current year-MoB-DoB)
            new_date = date(today.year, born_date.month, born_date.day)
            delta = new_date - today
            return delta.days

        else:
        # if month of birth is lower than current month, we know next birthday will be next year
            new_date = date(today.year + 1, born_date.month, born_date.day)
            delta = new_date - today
            return delta.days


    def load_data_to_database(self,results):

        for i in range(0, len(results)):

            person = Person(
                first_name=results[i]['name']['first'],
                last_name=results[i]['name']['last'],
                title=results[i]['name']['title'],
                gender=results[i]['gender'],
                email=results[i]['email'],
                street_name=results[i]['location']['street']['name'],
                street_number=results[i]['location']['street']['number'],
                city=results[i]['location']['city'],
                state=results[i]['location']['state'],
                country=results[i]['location']['country'],
                postcode=results[i]['location']['postcode'],
                latitude=results[i]['location']['coordinates']['latitude'],
                longitude=results[i]['location']['coordinates']['longitude'],
                offset=results[i]['location']['timezone']['offset'],
                description=results[i]['location']['timezone']['description'],
                uuid=results[i]['login']['uuid'],
                username=results[i]['login']['username'],
                password=results[i]['login']['password'],
                salt=results[i]['login']['salt'],
                md5=results[i]['login']['md5'],
                sha1=results[i]['login']['sha1'],
                sha256=results[i]['login']['sha256'],
                dob=self.fix_date_of_birth(results[i]['dob']['date']),
                age=results[i]['dob']['age'],
                registered_date=results[i]['registered']['date'],
                registered_age=results[i]['registered']['age'],
                phone=self.fix_cell_phone(results[i]['phone']),
                cell=self.fix_cell_phone(results[i]['cell']),
                nat=results[i]['nat'],
                daysleft=self.days_to_birthday(results[i]['dob']['date']),

            )
            person.save()
        print('Data was added to database')

if __name__ == '__main__':
    dl = DataLoader()
    dl.get_data()

