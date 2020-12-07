import json

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from data.parser.every_day_parser import Parser
from .deserializer.CurrencyDeserializer import CurrencyDeserializer
from data.DataRepository import DateRepository
import datetime


# Create your views here.
class CurrencyViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get_queryset(self):
        query_params = self.request.query_params
        date = query_params.get('date', None)
        request_type = query_params.get('type', None)

        if date == "today":
            date = str(datetime.datetime.today().date())

        data_query = {"date": date, "type": request_type}
        return data_query

    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = []
    allowed_methods = ('GET', 'POST', 'DELETE')

    @csrf_exempt
    def get(self, request, format=None):
        qset = self.get_queryset()
        data = DateRepository()
        if qset["type"] == "charCode":
            return HttpResponse(json.dumps(data.load_char_codes()))
        if qset["date"] is not None:
            validate(qset["date"])
            rates = data.get_by_date_in_json(qset["date"])
        else:
            rates = data.load_as_json()
        rates = json.dumps(rates)
        return HttpResponse(rates)

    @csrf_exempt
    def post(self, request, format=None):
        date = self.get_queryset()["date"]

        if date is not None:
            print(date)
            validate(date)
            try:
                Parser(date=date).parse()
            except:
                pass
        else:
            Parser().parse()
        return HttpResponse("Ok")


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        print("date validate error")
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
