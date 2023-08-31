import csv
from django.core.management import BaseCommand
# 2) Объединит данные из этих таблиц по error_id
def concant_by_error():
    data_to_save = []
    filename1 = "client.csv"
    filename2 = "server.csv"
    index = 0
    with open(filename1, 'r') as f1:
        reader1 = csv.reader(f1)
        for i in reader1:
            data_to_save.append(i[1])
            index += 1
    print(index)
    with open(filename2, 'r') as f2:
        reader2 = csv.reader(f2)
        for i in reader2:
            data_to_save.append(i[2])
            index += 1
    print(index)
    print(len(data_to_save))
    with open('new_file_2.csv', 'w+') as f:
         writer = csv.writer(f, delimiter=',')
         writer.writerows(data_to_save)
                


class Command(BaseCommand):
    

    def handle(self, *args, **options):
        
        concant_by_error()