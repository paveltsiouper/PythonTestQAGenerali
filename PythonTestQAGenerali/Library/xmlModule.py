import xml.etree.ElementTree as ET
from datetime import timedelta, date, datetime
import re

def get_timestamp(day_from_now):
    year, month, day = re.findall("\d+", str(date.today() + timedelta(days=5)))
    return datetime(int(year), int(month), int(day)).timestamp()


def update_itenuary_xmlfile(add_departure_days, add_return_days, filepath_in, filepath_out):
    """
    1. Create a python method that takes arguments int X and int Y,
       and updates DEPART and RETURN fields
        in test_payload1.xml:
        - DEPART gets set to X days in the future from the current date
       (whatever the current date is at the moment of executing the code)
        - RETURN gets set to Y days in the future from the current date
        Please write the modified XML to a new file.
    """
    tree = ET.parse(filepath_in)
    rootElement = tree.getroot()
    datetime_object_depart = get_timestamp(add_departure_days)
    for element in rootElement.iter("DEPART"):
        element.text = str(datetime_object_depart)
    datetime_object_return = get_timestamp(add_return_days)
    for element in rootElement.iter("RETURN"):
        element.text = str(datetime_object_return)
    tree.write(filepath_out)

