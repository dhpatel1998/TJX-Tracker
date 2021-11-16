# TJX EIC Capstone Project - Database and Analytics Team

import pandas as pd

df = pd.read_csv('product_data.csv')

prod_data = open("ProductData.txt", "w")
prod_data.write("INSERT INTO Products (product_sku, product_price, product_name, product_quantity,"\
                "product_description, image_url)\nVALUES\n")

product_id = 0
for i in range(len(df)):
    df.at[i, 'product_name'] = df.product_name[i].replace('\'', '')
    df.at[i, 'product_description'] = df.product_description[i].replace('\'', '')
    df.at[i, 'image_url'] = df.image_url[i].replace('\'', '')
    product_id += 1
    prod_data.write("('" + str(df.product_SKU[i]) + "', '" +
                    str(df.product_price[i]) + "', '" + str(df.product_name[i]) + "', '" +
                    str(df.product_quantity[i]) + "', '" + str(df.product_description[i]) + "', '" +
                    str(df.image_url[i]) + "')")

    if i != len(df)-1:
        prod_data.write(",\n")

prod_data.write(";")
prod_data.close()
