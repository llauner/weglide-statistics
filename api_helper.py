import json

import requests

import common_logging

logger = common_logging.getLogger("api_helper")
weglide_base_url = "https://api.weglide.org"


def get_flights_for_user(user_ids: list):
    url = weglide_base_url + "/v1/flight"
    payload = {'user_id_in': ",".join(user_ids)}

    x = requests.get(url, payload)

    flights = json.loads(x.text)
    return flights
