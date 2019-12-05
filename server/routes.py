from listeners import acquire_con, close_con, parse_real_teams
from services.views.aggregator import aggr, aggr_by_link_id


def add_routes(app):
    app.register_listener(acquire_con, "before_server_start")
    app.register_listener(parse_real_teams, "before_server_start")
    app.register_listener(close_con, "after_server_stop")

    app.add_route(aggr, '/aggregate', methods=['GET'])
    app.add_route(aggr_by_link_id, '/aggregate/<link_id:int>', methods=['GET'])
