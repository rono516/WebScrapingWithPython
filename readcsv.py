import csv


def PRINT(string):
    print(string)


def process_csv(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        # skip the header
        next(reader, None)
        for row in reader:
            PRINT(row)


if __name__ == '__main__':
    process_csv('new.csv')
