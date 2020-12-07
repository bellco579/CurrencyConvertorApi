import requests


class Download:
    def __init__(self, date: str):
        self._base_url = "http://data.fixer.io/api/"
        self._access_key = "4e6d19854b38f237582b3bf7dd7fa96a"
        self._date = date

    def build_url(self):
        return "{}{}?access_key={}".format(self._base_url, self._date, self._access_key)

    def fetch_data(self):
        url = self.build_url()
        response = requests.get(url)
        if response.status_code == 200:
            print("parsed date: {}".format(self._date))
            return response.json()

    def fetch_controller(self):
        return self.fetch_data()
        # return self.test_fetch_date()


if __name__ == '__main__':
    Download("2020-12-01").fetch_data()
    # print(dw)