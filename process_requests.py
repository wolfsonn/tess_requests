import os

from tess_requests import Request


def process(folder):
    requests_csv = []
    # folder = '/Users/wolfson/Desktop/homework/molbi/molbi_asv'  # testing
    directory = fr'{folder}'
    for entry in os.scandir(directory):
        if (entry.path.endswith('.jpg')) and entry.is_file():
            obj = Request(entry.path)
            print(entry)
            for _ in obj.csv_data:
                requests_csv.append(_)
            os.rename(entry, f'{directory}/{obj.case_number}.jpg')
    return requests_csv
