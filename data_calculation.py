from database_handler import Person
from peewee import fn
import math


class DataCalculation:

    def show_percentage(self):

        # count all persons
        all_users = Person.select().count()
        female = Person.select().where(Person.gender == 'female').count()
        male = Person.select().where(Person.gender == 'male').count()

        print("Female {female_result}%, Male {male_result}% "
              .format(female_result=round((female / all_users) * 100, 2),
                      male_result=round((male / all_users) * 100, 2)))

    def show_average(self,gender):

        # print average age
        if gender == "all":
            query = Person.select(fn.AVG(Person.age)).scalar()
        elif gender == 'female':
            query = Person.select(fn.AVG(Person.age)).where(Person.gender == "female").scalar()
        elif gender == "male":
            query = Person.select(fn.AVG(Person.age)).where(Person.gender == "male").scalar()
        print(query)

    def check_password_security(self):
        query = Person.select()
        passwords_list = []
        passwords_points = []
        result = 0
        help_value = 0

        for i in range(0, len(query)):

            if len(query[i].password) >= 8:
                help_value += 5

            if (any(p.islower() for p in query[i].password)):
                help_value += 1

            if (any(p.isupper() for p in query[i].password)):
                help_value += 2

            if (any(p.isdigit() for p in query[i].password)):
                help_value += 1

            if not(query[i].password.isalnum()):
                help_value += 3

            if (help_value >=result):
                result = help_value
                passwords_list.append(query[i].password)
                passwords_points.append(help_value)

            help_value = 0

        final_result = dict(zip(passwords_list,passwords_points))

        #find max value in dictionary
        max_value = max(final_result.items(), key=lambda x: x[1])

        list_of_keys = list()
        #find all max values
        for k,v in final_result.items():
            if v == max_value[1]:
                list_of_keys.append(k)

        print('Passwords with the highest points:')
        for l in list_of_keys:
            print(l)
        print('Points: ', max_value[1])

    def most_popular_city(self,number):

        query = Person\
            .select(Person.city, fn.COUNT(Person.id).alias('count'))\
            .group_by(Person.city)\
            .order_by(fn.COUNT(Person.id).desc())\
            .limit(number)

        for q in query:
            print(q.city,q.count)

    def most_popular_passwords(self,number):

        query = Person\
            .select(Person.password, fn.COUNT(Person.id).alias('count'))\
            .group_by(Person.password)\
            .order_by(fn.COUNT(Person.id).desc())\
            .limit(number)

        for q in query:
            print(q.password,q.count)


    def show_users_between_date(self,date):

        query = Person\
                .select()\
                .where(Person.dob.between(date[0],date[1]))

        for q in query:
            print(q.first_name, q.last_name, q.dob)
