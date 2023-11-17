import json

import requests

import common_logging

logger = common_logging.getLogger("api_helper")
weglide_base_url = "https://api.weglide.org"


def trigger_github_action():
    url = "https://api.github.com/repos/llauner/flight-analysis/dispatches"
    body = {'event_type': 'flights_table_updated'}
    headers = {'Authorization': 'Bearer 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'}

    x = requests.post(url, headers=headers, json=body)
    logger.debug(f"Trigger Action [flights_table_updated]: {x.text}")


def get_flights_for_user(user_ids: list):
    url = weglide_base_url + "/v1/flight"
    payload = {'user_id_in': ",".join(user_ids)}

    x = requests.get(url, payload)

    flights = json.loads(x.text)
    return flights
