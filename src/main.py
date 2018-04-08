#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector
from market import MakertFactory


config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '@WSX4rfv',
    'port': 3306,
    'database': 'workdata',
    'charset': 'utf8'
}


def main():
    # try:
    #     cnn = mysql.connector.connect(**config)
    # except mysql.connector.Error as e:
    #     print('connect fails!{}'.format(e))
    #
    # cursor = cnn.cursor()
    #
    # try:
    #     sql_query = 'select id, name from t_test ;'
    #     cursor.execute(sql_query)
    #     for name, age in cursor:
    #         print(name, age)
    # except mysql.connector.Error as e:
    #     print('query error!{}'.format(e))
    # finally:
    #     cursor.close()
    #     cnn.close()
    pass


if __name__ == '__main__':
    # main()

    market = MakertFactory.instance(api_key=3, api_secret=34)
    market.get_price()
