import jsonpickle
import csv
import json
import sqlite3
from django.core.management import BaseCommand


def write_rows(nomer, data_for_save):
    with open(f'new/newfile{nomer}', 'w+') as f:
        # data_for_save = []
        # data_for_save.append(ii)
        #####################################
        # writer = csv.writer(f)
        # writer.writerow(data_for_save)
        f.writelines(data_for_save)

def devider(filename, rows_infile):
        # filename = 'server.csv'
        # rows_infile = 5000
        f = open(filename)
        header = next(f)
        data_for_save = [header]
        index = 0
        numer = 0
        for i in f:
            if index >= rows_infile:
                index = 0
                numer += 1
                write_rows(numer, data_for_save)
                data_for_save = [header]
            data_for_save.append(i)
            index += 1
        # numer += 1
            
            

class Command(BaseCommand):
    
# 4) Выгрузит данные в таблицу, созданную в задаче 1. В ней должны бать следующие данные:

# timestamp из server.csv
# player_id из client.csv
# error_id  из сджойненных server.csv и client.csv
# json_server поле json из server.csv
# json_client поле json из client.csv
    
    
    def handle(self, *args, **options):
        devider()
        