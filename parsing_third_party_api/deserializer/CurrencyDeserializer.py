import json

from parsing_third_party_api.models import CurrencyModel


class CurrencyDeserializer:
    def __init__(self, json_str: str):
        json_value = json.loads(json_str)
        self.day = json_value["day"]
        self.month = json_value["month"]
        self.year = json_value["year"]
        self.charCode = json_value["charCode"]
        self.name = json_value["name"]
        self.value = json_value["value"]

    def create_model(self):
        model = CurrencyModel.objects.get_or_create(day=self.day, month=self.month, year=self.year,
                                                    charCode=self.charCode, name=self.name, value=self.value)
        return model
