# TJX EIC Capstone Project - Database and Analytics Team

from csv import writer
import names
import random
from random import randrange, choice
from faker import Faker


def generateEntries():

    coin_toss1 = randrange(2)
    if coin_toss1 == 0:
        first_name = names.get_first_name(gender='male')
        coin_toss2 = randrange(2)
        if coin_toss2 == 0:
            middle_name = names.get_first_name(gender='male')
        else:
            middle_name = ""
    else:
        first_name = names.get_first_name(gender='female')
        coin_toss2 = randrange(2)
        if coin_toss2 == 0:
            middle_name = names.get_first_name(gender='female')
        else:
            middle_name = ""

    last_name = names.get_last_name()

    country = choice(['United States', 'United Kingdom', 'Canada'])
    if country == "United States":
        phone_country_code = 1
        phone = ""
        for i in range(0, 10):
            phone += str(random.randint(0, 9))
        phone = int(phone)
        fake = Faker(['en_US'])
    elif country == "Canada":
        phone_country_code = 1
        phone = ""
        for i in range(0, 10):
            phone += str(random.randint(0, 9))
        phone = int(phone)
        fake = Faker(['en_CA'])
    elif country == "United Kingdom":
        phone_country_code = 44
        phone = ""
        for i in range(0, 10):
            phone += str(random.randint(0, 9))
        phone = int(phone)
        fake = Faker(['en_GB'])
    city = fake.city()
    zip_code = fake.postcode()
    street = str(fake.street_address())
    street = street.replace('\n', ' ')

    fake = Faker(['en_GB'])
    customer_notes = fake.sentence()

    email_types = ['@gmail.com', '@outlook.com', '@yahoo.com']

    first_name_email = first_name.lower()
    last_name_email = last_name.lower()
    email = str(first_name_email) + str(last_name_email) + str(random.choices(email_types, [0.8, 0.15, 0.05]))[2:-2]

    list_return = [customerID, first_name, middle_name, last_name, phone_country_code, phone, email, customer_notes, street,
           city, zip_code, country]

    return customerID, first_name, middle_name, last_name, phone_country_code, phone, email, customer_notes, street, \
           city, zip_code, country


csv_file = open("Customers.csv", "w")
csv_file.truncate()
csv_file.close()

text_file = open("Customers.txt", "w")
text_file.write("INSERT INTO Customers (first_name, middle_name, last_name, phone_country_code, phone,"\
                "email, customer_notes, street, city, zip_code, country)\nVALUES\n")

with open('Customers.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object, delimiter=',')
    writer_object.writerow(['customer_id', 'first_name', 'middle_name', 'last_name', 'phone_country_code', 'phone',
                            'email', 'customer_notes', 'street', 'city', 'zip_code', 'country'])
    f_object.close()

customerNumber = 0
for i in range(1000):
    customerNumber += 1
    customerID = format(customerNumber, '010d')
    generated_values = generateEntries()

    list_csv = [generated_values[0], generated_values[1], generated_values[2], generated_values[3],
                generated_values[4], generated_values[5], generated_values[6], generated_values[7],
                generated_values[8], generated_values[9], generated_values[10], generated_values[11]]

    text_file.write("('" + str(generated_values[1]) + "', '" +
                    str(generated_values[2]) + "', '" + str(generated_values[3]) + "', '" + str(generated_values[4]) +
                    "', '" + str(generated_values[5]) + "', '" + str(generated_values[6]) + "', '" +
                    str(generated_values[7]) + "', '" + str(generated_values[8]) + "', '" + str(generated_values[9]) +
                    "', '" + str(generated_values[10]) + "', '" + str(generated_values[11]) + "')")

    if i != 999:
        text_file.write(",\n")

    with open('Customers.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object, delimiter=',')
        writer_object.writerow(list_csv)
        f_object.close()

text_file.write(";")
text_file.close()





