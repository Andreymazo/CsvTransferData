from curses.ascii import isdigit
import os, csv
import random
import sqlite3
from django.core.management import BaseCommand
import uuid
from datetime import datetime


def convert_timestamp_date(timestamp):
    ts = int(timestamp)
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
        # from datetime import datetime
        # ts = int('1615148137')
        # # if you encounter a "year is out of range" error the timestamp
        # # may be in milliseconds, try `ts /= 1000` in that case
        # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

def concant_by_date():
    date_to_find = input('Ведите дату по которой объединить данные из двух файлов, пример (2021,04,11)')
    year, month, day = map(int, date_to_find.split(','))
    date = datetime(year, month, day).strftime('%Y-%m-%d')
    data_to_save = []
    filename1 = "client.csv"
    filename2 = "server.csv"
    with open(filename1, 'r') as f:
        reader = csv.reader(f)
        index = 0
        for i in reader:
            # if index < 2:
                if i[0].isdigit() == True and convert_timestamp_date(i[0]) == date:#
                    data_to_save.append(i) 
                    # print('date, convert_timestamp_date(i[0])' , date, convert_timestamp_date(i[0]))
                    index += 1
        print(index)#474
    with open(filename2, 'r') as f:
        reader = csv.reader(f)
        index = 0
        for i in reader:
                if i[0].isdigit() == True and convert_timestamp_date(i[0]) == date:#
                    data_to_save.append(i) 
                    # print('date, convert_timestamp_date(i[0])' , date, convert_timestamp_date(i[0]))
                    index += 1
        print(index)
        print(len(data_to_save))
    with open('new_file.csv', 'w+', newline='') as f:
         writer = csv.writer(f, delimiter=',')
         writer.writerows(data_to_save)

         
               
               
              
                # index += 1
                
# Написать класс или функцию, которая:

# 1) Выгрузит данные из client.csv и server.csv за определенную дату.
# 2) Объединит данные из этих таблиц по error_id.
# 3) Исключит из выборки записи с player_id, которые есть в таблице  cheaters,
#    но только в том случае если:
#    у player_id ban_time - это предыдущие сутки или раньше относительно timestamp из server.scv
# 4) Выгрузит данные в таблицу, созданную в задаче 1. В ней должны бать следующие данные:

# timestamp из server.csv
# player_id из client.csv
# error_id  из сджойненных server.csv и client.csv
# json_server поле json из server.csv
# json_client поле json из client.csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        concant_by_date()
        # con = sqlite3.connect("my_db.db", timeout=10)

        # cur = con.cursor()
        # cur.execute("CREATE TABLE first(timestamp, player_id, event_id, error_id, json_server, json_client, year, score)")
        # con.close()
        
       
       




        # print(os.path.getsize(filename))
        # # random row:

        # with open(filename) as f:
        #     reader = csv.reader(f)
        #     chosen_row_pick_up = tuple(random.choice(list(reader)))
        #     print(chosen_row_pick_up)
        #     lat_pick_up = chosen_row_pick_up[1]
        #     lon_pick_up = chosen_row_pick_up[2]
        #     location1 = f"{lat_pick_up}, {lon_pick_up}"
        # with open(filename) as f:
        #     reader = csv.reader(f)
        #     chosen_row_destination = random.choice(tuple(reader))
        #     lat_dest = chosen_row_destination[1]
        #     lon_dest = chosen_row_destination[2]
        #     location2 = f"{lat_dest}, {lon_dest}"

        #     from geopy.distance import distance
        #     dist = distance(location1, location2).miles
        #     print(dist)
        # # https: // pypi.org / project / geopy /



        #     # ['24551', '37.36655', '-79.3268', 'Forest', 'VA', 'Virginia', 'TRUE', '', '26376', '137.3', '51019',
        #     #  'Bedford', '{"51019": 97.23, "51031": 2.42, "51680": 0.35}', 'Bedford|Campbell|Lynchburg',
        #     #  '51019|51031|51680', 'FALSE', 'FALSE', 'America/New_York']

        #     # "zip", "lat", "lng", "city", "state_id", "state_name", "zcta", "parent_zcta", "population", "density", "county_fips", "county_name", "county_weights", "county_names_all", "county_fips_all", "imprecise", "military", "timezone"

        #     # lat_dest = chosen_row[1]
        #     # lon_dest = chosen_row[2]
        #     # tup_destination = (lat_des, lon_des)
        #     # dist =
        # import psycopg2

        # # connection establishment
        # conn = psycopg2.connect(
        #     database="newdb",
        #     user='postgres',
        #     password='123456',
        #     host='localhost',
        #     port='5432'
        # )

        # conn.autocommit = True

        # # Creating a cursor object
        # cursor = conn.cursor()

        # # query to create a table
        # # sql = '''drop table locations'''
        # # sql = ''' CREATE TABLE locations (zip INT, latitude FLOAT, longtitude FLOAT, city VARCHAR(50), state VARCHAR(50)); '''
        # # sql = '''truncate table locations restart identity cascade'''

        # # cursor.execute(sql)
        # with open(filename, 'r', encoding='utf-8') as f:
        #     data = csv.reader(f, delimiter=',')
        #     next(data)

        #     for i in data:  ##Zapoliaem suppliers

        #         # index = 0
        #         # ii = ', '.join(i.get("products"))
        #         # print(ii)

        #         cursor.execute(
        #             'INSERT INTO locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
        #             (i[0], i[1], i[2], i[3], i[5].split(',')[0]))

        # # sql = '''insert into table locations '''
        # # executing above query

        # print("Table has been created successfully!!")

        # # Closing the connection
        # conn.close()