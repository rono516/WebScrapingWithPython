# import csv
#
#
# def process_csv_dict_reader(file_obj):
#     reader = csv.DictReader(file_obj)
#     for line in reader:
#         print(f'{line["book_title"]} by {line["author"]}')
#
#
# if __name__ == "__main__":
#     with open('new.csv') as csvfile:
#         process_csv_dict_reader(csvfile)


# csv_dict_reader.py
import csv


def process_csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj)
    for line in reader:
        print(f'{line["book_title"]} by {line["author"]}')


if __name__ == '__main__':
    with open('new.csv') as csvfile:
        process_csv_dict_reader(csvfile)
