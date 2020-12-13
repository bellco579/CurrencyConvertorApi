import errno
import json
import os

import pandas


class PandasCurrencyController:
    def __init__(self, path="jsons/currencyRatesList.json"):
        self.path = path

    def save(self, df):
        if not os.path.exists(os.path.dirname(self.path)):
            try:
                os.makedirs(os.path.dirname(self.path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        df.to_json(self.path)

    def save_json(self, df):
        if not os.path.exists(os.path.dirname(self.path)):
            try:
                os.makedirs(os.path.dirname(self.path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(self.path, "w") as js_file:
            json.dump(df, js_file)

    def load(self):
        return pandas.read_json(self.path)

    def load_json(self):
        with open(self.path) as js_file:
            return json.load(js_file)
