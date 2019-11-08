from listeners import acquire_con, close_con
from services.views.aggregator import aggr, aggr_by_link_id


def add_routes(app):
    app.register_listener(acquire_con, "before_server_start")
    app.register_listener(close_con, "after_server_stop")

    app.add_route(aggr, '/aggregator', methods=['GET'])
    app.add_route(aggr_by_link_id, '/aggregator/<link_id:int>', methods=['GET'])
