import csv
from datetime import timedelta
import sqlite3
from django.core.management import BaseCommand
from csv_transfer_data.management.commands.chek import convert_timestamp_date_time

from csv_transfer_data.management.commands.concat_by_date_csv import convert_timestamp_date

# def exclude_ch():
#     data_to_save = []
#     filename1 = "client.csv"
#     filename2 = "server.csv"
#     with open(filename1, 'r') as f1:
#         reader1 = csv.reader(f1)
#         with open(filename2, 'r') as f2:
#             reader2 = csv.reader(f2)
#             for i in reader1:
#                 for ii in reader2:
#                     if i[1] == ii[2]:
#                         data_to_save.append((i, ii))
#     print('len(data_to_save)', len(data_to_save), data_to_save)


def sutki_ili_ranshe(x):
    data_fm_server = []
    filename2='server.csv'
    with open(filename2, 'r') as f:
        reader1 = csv.reader(f)
        # data_to_chek = []
        # for i in reader1:
        #     data_to_chek.append(i)
        # print('len(data_to_chek)', len(data_to_chek))
        index = 0
        for i in reader1:
            print(i[0])
            # if i[0].isdigit() 
        #################################################
        # for i in reader1:
        #     # print('x[1]', x[1])#x[1] 2021-04-20 03:34:14
        #     if i[0].isdigit() and x[1] < str(convert_timestamp_date_time(i[0]) - timedelta(days=1)):
        #         index += 1
        #         # print(index)
        #         return x[0]
                
        #     elif i[0].isdigit() and x[1] >= str(convert_timestamp_date_time(i[0]) - timedelta(days=1)):
        #         index +=1
        #         # print(index)
        #         # x = None
        #         # return x


class Command(BaseCommand):
    
# 3) Исключит из выборки записи с player_id, которые есть в таблице  cheaters,
#    но только в том случае если:
#    у player_id ban_time - это предыдущие сутки или раньше относительно timestamp из server.scv
# Думаю ошибка, не server.scv, а client.csv
    
    
    def handle(self, *args, **options):
        data_from_cheaters = []
        data_from_cheaters_0 = []
        # print(len(data_fm_server))
        data_from_cheaters_clear = []
        data_to_save = []
        filename1 = "client.csv"
        con = sqlite3.connect("cheaters.db", timeout=10)
        cur = con.cursor()
        result = cur.execute("select * from cheaters")
        data_from_cheaters = [i for i in result]
        #############################################################
        # data_from_cheaters_0 = [i[0] for i in result]
        # print('len(data_from_cheaters)', len(data_from_cheaters))
        # cur.execute("CREATE TABLE first(timestamp, player_id, event_id, error_id, json_server, json_client, year, score)")
        # list(cur.fetchall())
        # print(data_from_cheaters)#[...(999892, '2021-01-25 14:38:15'), (999922, '2021-05-18 03:50:08')]
        # print(data_from_cheaters_0)#[...999633, 999665, 999735, 999761, 999850, 999892, 999922]
        con.close()
        index = 0
        data_fm_client_csv_cheaters = []
        filename2='client.csv'
        with open(filename2, 'r') as f:
            next(f)
            reader1 = csv.reader(f)
        # data_to_chek = []
        # for i in reader1:
        #     data_to_chek.append(i)
        # print('len(data_to_chek)', len(data_to_chek))
            
            # print(len(data_from_cheaters_0))#16577
            
            for i in reader1:
                # if index < 50: #Dlya proverok chtobi ne gonyat tisyachi strok vvodim index
                ################################################
                    for ii in data_from_cheaters:
                        if int(i[2])==int(ii[0]) and ii[1] < str(convert_timestamp_date_time(i[0]) - timedelta(days=1)):
                            data_fm_client_csv_cheaters.append(i[2])#Spisok cheaters
                            # index += 1
                    # print('777777777777', len(data_fm_client_csv))#777777777777 17592 # without: ii[1] < str(convert_timestamp_date_time(i[0]) - timedelta(days=1))
                    print('777777777777', len(data_fm_client_csv_cheaters))#777777777777 8743
            
        with open(filename2, 'r') as f:
            next(f)
            reader1 = csv.reader(f)   
            # print(len(list(reader1)))
            data_without_cheaters = [x for x in reader1 if x[2] not in data_fm_client_csv_cheaters]
            # data_without_cheaters = []
            # for i in reader1:
            #     print(i[2])
            #     if i[2] not in data_fm_client_csv_cheaters:
            #         data_without_cheaters.append(i)

            print(len(data_without_cheaters))#57555
            with open('new_without_cheaters.csv', 'w+') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerows(data_without_cheaters)
        