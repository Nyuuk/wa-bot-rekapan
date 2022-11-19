import csv

with open("DATA-SANTRI-PUTRA(fix).csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are {','.join(row)}")
            line_count += 1
        else:
            line_count += 1
            print("nama santri: {}".format(row[0]))
    print("total data yang di proses: {}".format(line_count-1))
