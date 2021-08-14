import os

from tess_requests import Request


def process():
    requests_csv = []
    folder = str(input("select dir: "))
    # folder = '/Users/wolfson/wolfson_dev/tess_requests/molbi'  # testing
    directory = fr'{folder}'
    for entry in os.scandir(directory):
        if (entry.path.endswith('.jpg')) and entry.is_file():
            obj = Request(entry.path)
            obj.prep_csv()
            for _ in obj.csv_data:
                requests_csv.append(_)
            os.rename(entry, f'{directory}/{obj.case_number}.jpg')
    return requests_csv
