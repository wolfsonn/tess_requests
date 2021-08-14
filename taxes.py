from requests_db import export_one_for_taxes


def get_taxes(action):
    cases_list = export_one_for_taxes(action)
    taxes_prep = {}
    for i in cases_list:
        case_year = i[:4]
        case_number = i[-4:]
        if case_year not in taxes_prep.keys():
            taxes_prep[case_year] = [int(case_number)]
        taxes_prep[case_year].append(int(case_number))
    with open('taxes.txt', 'w') as f:
        for i in taxes_prep.keys():
            f.write(f'{i} - {",".join(str(i) for i in taxes_prep[i])}\n')


get_taxes('РБСС')
