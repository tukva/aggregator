from http import HTTPStatus

from sanic.response import json
from sanic.views import HTTPMethodView

from services.utils import get_aggr_teams


class AggrTeams(HTTPMethodView):
    async def get(self, request):
        team_for_match = request.raw_args.get("team")
        params = request.raw_args
        result = await get_aggr_teams(team_for_match, **params)
        return json(result, HTTPStatus.OK)
