# TJX EIC Capstone Project - Database and Analytics Team

import pandas as pd
import random
from random import randrange
from datetime import datetime
from datetime import timedelta
from faker import Faker
from csv import writer
fake = Faker(['en_GB'])


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


df = pd.read_csv('product_data.csv')
append_id = [format(i, '010d') for i in range(len(df))]
df['product_id'] = append_id

df2 = pd.read_csv('Customers.csv', converters={'customer_id': lambda x: str(x)})

products_sum = 0
for i in range(len(df)):
    products_sum += df.product_quantity[i]

rand_num = random.randint(40, 70)
products_perc = round(products_sum/100*rand_num)

orders = []

csv_file1 = open("OrdersData.csv", "w")
csv_file1.truncate()
csv_file1.close()

with open('OrdersData.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object, delimiter=',')
    writer_object.writerow(['order_id', 'customer_id', 'order_status', 'datetime_order_placed', 'total_order_price',
                            'order_notes'])
    f_object.close()

text_file1 = open("OrdersData.txt", "w")
text_file1.write("INSERT INTO Orders (customer_id, order_status, datetime_order_placed, total_order_price,"
                 " order_notes)\nVALUES\n")

csv_file2 = open("OrderDetail.csv", "w")
csv_file2.truncate()
csv_file2.close()

with open('OrderDetail.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object, delimiter=',')
    writer_object.writerow(['order_id', 'product_id', 'quantity_purchased'])
    f_object.close()

text_file2 = open("OrderDetail.txt", "w")
text_file2.write("INSERT INTO Order_detail (order_id, product_id, quantity_purchased)\nVALUES\n")

for i2 in range(products_perc):
    a1 = range(0, len(df))
    product_line = random.choice([x for x in a1 if x not in df[df['product_quantity'] == 0].index])

    df.at[product_line, 'product_quantity'] = df.product_quantity[product_line] - 1
    product_id = df.product_id[product_line]
    loop = 1
    while loop == 1:
        order_id = format(random.randint(0, products_perc), '010d')
        if order_id in orders:
            loop = 1
        else:
            orders.append(order_id)
            loop = 0

    quantity_types = [1, 2, 3, 4]
    order_quantity = str(random.choices(quantity_types, [0.8, 0.12, 0.06, 0.02]))[1:-1]

    list_csv = [order_id, product_id, order_quantity]

    text_file2.write("('" + str(order_id) + "', '" + str(product_id) + "', '" + str(order_quantity) + "')")

    if i2 != products_perc-1:
        text_file2.write(",\n")

    with open('OrderDetail.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object, delimiter=',')
        writer_object.writerow(list_csv)
        f_object.close()

text_file2.write(";")
text_file2.close()
df3 = pd.read_csv('OrderDetail.csv', converters={'product_id': lambda x: str(x), 'order_id': lambda x: str(x)})

it = 0
for i3 in orders:
    coin_toss1 = randrange(2)
    if coin_toss1 == 0:
        order_status_code = random.randint(1, 6)
    else:
        order_status_code = random.randint(7, 8)

    if order_status_code in [7, 8]:
        d1 = datetime.strptime('1/11/2021 1:30 PM', '%d/%m/%Y %I:%M %p')
        d2 = datetime.strptime('15/11/2021 4:50 AM', '%d/%m/%Y %I:%M %p')
    else:
        d1 = datetime.strptime('1/01/2021 1:30 PM', '%d/%m/%Y %I:%M %p')
        d2 = datetime.strptime('1/11/2021 4:50 AM', '%d/%m/%Y %I:%M %p')
    datetime_order_placed = random_date(d1, d2)

    order_notes = fake.sentence()

    a2 = df[['product_price', 'product_id']]
    a3 = df3.loc[df3['order_id'] == i3]

    order_price = 0
    new_df = pd.merge(a2, a3, on='product_id', how='inner')

    order_price += float(new_df.product_price) * int(new_df.quantity_purchased)
    order_price = round(order_price, 2)

    random_customer = df2.sample()
    a = random_customer.customer_id

    list_csv = [a.values[0], order_status_code, datetime_order_placed, order_price, order_notes]

    with open('OrdersData.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object, delimiter=',')
        writer_object.writerow(list_csv)
        f_object.close()

    text_file1.write("(" + str(a.values)[1:-1] + ", '" + str(order_status_code) + "', '" +
                     str(datetime_order_placed) + "', '" + str(order_price) + "', '" + str(order_notes) + "')")

    if it != len(orders)-1:
        text_file1.write(",\n")

    it += 1

text_file1.write(";")
text_file1.close()


