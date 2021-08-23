import re

from PIL import Image
import pytesseract


class Request:
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

    def __init__(self, file):
        self.file = file

    @property
    def text(self):
        text = str((pytesseract.image_to_string(Image.open(self.file), lang="bul")))
        return text

    @property
    def actions(self):
        actions = []
        for action, keywords in Request.ACTIONS.items():
            for k in keywords:
                if k in self.text and action not in actions:
                    actions.append(action)
        if len(actions) == 0:
            actions.append('null')
        return actions

    @property
    def case_number(self):
        case_regex = r"изп. дело \d{1,4}\s*/\s*\d{4} г."
        case_search = (re.search(case_regex, self.text))
        if case_search:
            case = case_search.group()
            case_number = case.removeprefix('изп. дело ').removesuffix(' г.')
            full_case_number = f'{case_number[-4:]}8610{400000 + int(case_number[:-5])}'
            case_number = full_case_number
        else:
            case_number = 'null'
        return case_number

    @property
    def egn(self):
        egn_regex = r"ЕГН [\d|\D]{11}"
        egn_search = re.search(egn_regex, self.text)
        if egn_search:
            egn = egn_search.group().removeprefix('ЕГН ').removesuffix(",").replace(" ", "")
        else:
            egn = 'null'
        return egn

    @property
    def csv_data(self):
        csv_data = []
        for _ in self.actions:
            csv_data.append([_, self.case_number, self.egn])
        return csv_data
