from injectable import injectable

import common_logging

logger = common_logging.getLogger("MysqlService")


@injectable
class MysqlService:
    """ Access MySQL database"""

    def __init__(self):
        self.table_name = "flights"

    def insert_flight_rows(self, flights):
        return True



