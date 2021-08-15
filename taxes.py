from requests_db import export_taxes


def get_taxes(action, status):
    cases_list = export_taxes(action, status)
    taxes_prep = {}
    for i in cases_list:
        case_year = i[:4]
        case_number = i[-4:]
        if case_year not in taxes_prep.keys():
            taxes_prep[case_year] = [int(case_number)]
        taxes_prep[case_year].append(int(case_number))
    with open(f'{action + "_" if action else ""}{status + "_" if status else ""}taxes.txt', 'w') as f:
        for i in taxes_prep.keys():
            f.write(f'{i} - {",".join(str(i) for i in taxes_prep[i])}\n')

