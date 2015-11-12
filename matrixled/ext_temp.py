import requests


def get_temp_hum():
    r = requests.get(
        "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.fore"
        "cast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%2"
        "0text%3D%22Genova%22)%20and%20u%3D'c'&format=json&env=store%3A%2F%2Fdatatabl"
        "es.org%2Falltableswithkeys")

    channel = r.json()['query']['results']['channel']

    return channel['item']['condition']['temp'], channel['atmosphere']['humidity']
