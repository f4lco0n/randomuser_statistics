from peewee import *


db = SqliteDatabase('profil_software.db')


class Person(Model):

    first_name = CharField()
    last_name = CharField()
    title = CharField()
    gender = CharField()
    email = CharField(unique=True)
    street_name = CharField()
    street_number = IntegerField()
    city = CharField()
    state = CharField()
    country = CharField()
    postcode = CharField()
    latitude = FloatField()
    longitude = FloatField()
    offset = CharField()
    description = CharField()
    uuid = UUIDField()
    username = CharField()
    password = CharField()
    salt = CharField()
    md5 = CharField()
    sha1 = CharField()
    sha256 = CharField()
    dob = DateField()
    age = IntegerField()
    registered_date = DateTimeField()
    registered_age = IntegerField()
    phone = CharField()
    cell = CharField()
    nat = CharField()
    daysleft = IntegerField()

    class Meta:
        database = db



if __name__ == "__main__":
    db.connect()
    db.create_tables([Person])
    db.close()