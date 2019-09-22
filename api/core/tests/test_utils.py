from django.test import TestCase
from datetime import datetime

from api.core.utils.parse_date import parse_date
from api.core.utils.parse_price import parse_price

class UtilsTestCase(TestCase):
    def test_parse_price_millions(self):
        self.assertEquals(parse_price("$2.79M"), 2790000.0)

    def test_parse_price_thousands(self):
        self.assertEquals(parse_price("$720K"), 720000.0)
        self.assertEquals(parse_price("$1K"), 1000.0)

    def test_parse_price_hundreds(self):
        self.assertEquals(parse_price("$720"), 720.0)
        self.assertEquals(parse_price("$1234"), 1234.0)
    
    def test_parse_price_empty(self):
        self.assertEquals(parse_price(""), 0.0)
        self.assertEquals(parse_price(None), 0.0)

    def test_parse_date(self):
        self.assertEquals(
            parse_date("08/13/2015"), 
            datetime(2015, 8, 13, 0, 0)
        )

        self.assertEquals(
            parse_date("02/22/2017"), 
            datetime(2017, 2, 22, 0, 0)
        )
