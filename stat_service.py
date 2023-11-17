from injectable import load_injection_container, inject
import api_helper
from MysqlService import MysqlService


def main():
    # ----------------------------- Parse request parameters -----------------------------
    # Log Start of the process
    print(f"##### [Track Service] Launching processing")

    # --- Get dependencies
    load_injection_container()
    mysql_service = inject(MysqlService)

    # ----------------------------- Begin processing -----------------------------
    user_ids = ["2326", "12810"]

    # --- Get flights from weglide
    flights = api_helper.get_flights_for_user(user_ids)

    # --- Insert into database



