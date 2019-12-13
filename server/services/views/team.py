from http import HTTPStatus

from sanic.response import json
from sanic.views import HTTPMethodView

from services.utils import get_aggr_teams


class AggrTeams(HTTPMethodView):
    async def get(self, request):
        team_for_match = request.args.get("team")
        link_id = request.args.get("link_id")
        result = await get_aggr_teams(team_for_match, link_id)
        return json(result, HTTPStatus.OK)
