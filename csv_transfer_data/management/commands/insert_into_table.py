
import csv
import sqlite3
from django.core.management import BaseCommand
class Command(BaseCommand):
    
# 4) Выгрузит данные в таблицу, созданную в задаче 1. В ней должны бать следующие данные:

# timestamp из server.csv
# player_id из client.csv
# error_id  из сджойненных server.csv и client.csv
# json_server поле json из server.csv
# json_client поле json из client.csv
    
    
    def handle(self, *args, **options):
        # with open('server.csv', 'r') as f:
        #     reader1 = csv.reader(f)
        con = sqlite3.connect("my_db.db", timeout=10)
        con.isolation_level = None
            # cur = con.cursor()
        con.execute("CREATE TABLE first(timestamp TEXT, player_id INT, event_id TEXT, error_id TEXT, json_server TEXT, json_client TEXT, year TEXT, score TEXT)")
# https://ruseller.com/lessons.php?id=2277


        # con.execute('''CREATE TABLE first
        #     (timestamp     TEXT     NOT NULL,
        #     player_id           TEXT    NOT NULL,
        #     event_id            INT     NOT NULL,
        #     error_id     TEXT,   
        #     json_server TEXT ,
        #     json_client  TEXT ,    
        #     year     TEXT  ,
        #     score    TEXT    ;''')
        con.commit()
        con.close()
            # , player_id, , i[1], error_id, i[3], json_client, i[5],, year, score, i[6], i[7], i[8], i[9]
#             for i in reader1:

#                 con.execute(f"INSERT INTO first (timestamp, json_server) VALUES ({i[0]}, {i[3]})")
# #1612068364,76,38152c64-d439-43cf-9856-4ca35d39d7ac,"{""purpose"": ""...
#         # result = cur.execute("select * from cheaters")
#         # data_from_cheaters = [i for i in result]
#         #############################################################
#         # data_from_cheaters_0 = [i[0] for i in result]
#         # print('len(data_from_cheaters)', len(data_from_cheaters))
#         # cur.execute("CREATE TABLE first(timestamp, player_id, event_id, error_id, json_server, json_client, year, score)")
#         # list(cur.fetchall())
#         # print(data_from_cheaters)#[...(999892, '2021-01-25 14:38:15'), (999922, '2021-05-18 03:50:08')]
#         # print(data_from_cheaters_0)#[...999633, 999665, 999735, 999761, 999850, 999892, 999922]
#             con.commit()
#         con.close()