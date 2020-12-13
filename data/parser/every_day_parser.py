import datetime
import time

import pandas

from json_db.PandasCurrencyContrller import PandasCurrencyController
from WebServices.DownloadDailyRates import Download


def sort_df(df):
    start_date = datetime.datetime(2000, 1, 1)
    end_date = datetime.datetime(2020, 12, 31)
    res = pandas.date_range(
        min(start_date, end_date),
        max(start_date, end_date)
    ).strftime('%Y-%m-%d').tolist()
    # %%

    df_new = pandas.DataFrame()

    # %%

    print(len(res))
    # %%

    for date in res:
        try:
            df_new[str(date)] = df[date]
        except:
            pass
    # %%
    return df


class Parser:
    def __init__(self, date=datetime.datetime.today().date()):
        self.today = str(date)
        self.download_rate_by_date = Download(self.today)
        self.currency_db_controller = PandasCurrencyController()
        self.currency_df = self.load_df()

    def parse(self):
        json_data = self.fetch_downloaded_json_rates()["rates"]
        self.currency_df[self.today] = json_data
        self.currency_df = sort_df(self.currency_df)
        self.save()
        return json_data

    def fetch_downloaded_json_rates(self):
        return self.download_rate_by_date.fetch_data()

    def load_df(self):
        return self.currency_db_controller.load_json()

    def save(self):
        self.currency_db_controller.save_json(self.currency_df)
