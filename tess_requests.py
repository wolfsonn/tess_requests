import re

from PIL import Image
import pytesseract


class Request:
    def __init__(self, file):
        self.file = file
        self.text = ''
        self.case_number = ''
        self.egn = ''
        self.actions = []
        self.csv_data = []

    def get_text(self):
        request_text = str((pytesseract.image_to_string(Image.open(self.file), lang="bul")))
        self.text = request_text
        return self.text

    def get_case_number(self):
        case_regex = r"изп. дело \d{1,4}/\d{4} г."
        case = (re.search(case_regex, self.text)).group()
        case_number = case.removeprefix('изп. дело ').removesuffix(' г.')
        full_case_number = f'{case_number[-4:]}8610{400000 + int(case_number[:-5])}'
        self.case_number = full_case_number

    def get_egn(self):
        egn_regex = r"ЕГН [\d|\D]{11}"
        egn_search = re.search(egn_regex, self.text)
        if egn_search:
            egn = egn_search.group().removeprefix('ЕГН ').removesuffix(",").replace(" ", "")
        else:
            egn = 'null'
        self.egn = egn

    def get_actions(self):
        actions_temp = []
        ACTIONS = {
            "РБСС": ["банкови сметки", "сметки"],
            "опис": ["опис", "Опис"],
            "работодател": ["трудов", "трудови"],
            "мобилен оператор": ["мобилни оператори"],
            "МДТ": ["МДТ", "община"],
            "KAT": ["КАТ"],
            "ИКАР": ["ИКАР"],
            "74": ["НАП"],
            "напомнително": ["напомнително"],
        }

        for action, keyword in ACTIONS.items():
            for k in keyword:
                if k in self.text and action not in actions_temp:
                    actions_temp.append(action)
        if len(actions_temp) == 0:
            actions_temp.append('null')
        self.actions = actions_temp

    def get_request_data(self):
        self.get_text()
        self.get_case_number()
        self.get_egn()
        self.get_actions()

    def prep_csv(self):
        data = []
        self.get_request_data()
        for _ in self.actions:
            data.append([_, self.case_number, self.egn])
        self.csv_data = data
