import requests


def get_temp_hum():
    r = requests.get(
        "http://api.wunderground.com/api/2e7c13d800eac2d7/conditions/q/pws:IGENOVA70.json")

    current = r.json()['current_observation']
    e_temp = current['temp_c']
    e_hum = current['relative_humidity']
    return e_temp, e_hum
