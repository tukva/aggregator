from listeners import acquire_con, close_con
from services.views.aggregator import aggregator


def add_routes(app):
    app.register_listener(acquire_con, "before_server_start")
    app.register_listener(close_con, "after_server_stop")

    app.add_route(aggregator, '/aggregator', methods=['GET'])
