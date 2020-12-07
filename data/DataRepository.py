import pandas

from data.parser.every_day_parser import Parser
from json_db.PandasCharCodeController import PandasCharCodeController
from json_db.PandasCurrencyContrller import PandasCurrencyController


class DateRepository:
    def __init__(self):
        self.rates_db = PandasCurrencyController()
        self.char_code_db = PandasCharCodeController()
        self.currency_df = pandas.DataFrame()
        self.load()

    def load(self) -> pandas.DataFrame():
        self.currency_df = self.rates_db.load()
        return self.currency_df

    def load_as_json(self):
        return self.rates_db.load_json()

    def save(self):
        pass

    def get_by_date_in_json(self, date):
        json_value = self.load_as_json()
        try:
            rates = json_value[date]
        except:
            rates = Parser(date).parse()
            # index = list(json_value)[-1]
            # rates = json_value[index]
        obj = {str(date): rates}
        return obj

    def get_by_date(self, date):
        try:
            currency_by_date = self.currency_df[date]
        except:
            currency_by_date = self.currency_df.iloc[:, -1:]
        return currency_by_date.to_json(orient="table")

    def get_today_rates(self):
        pass

    def get_all_rates(self):
        pass

    def load_char_codes(self):
        return self.char_code_db.load_json()
