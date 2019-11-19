from sanic.response import json

from services.utils import get_aggr_teams, get_aggr_teams_by_link_id


async def aggr(request):
    result = await get_aggr_teams(request)
    return json(result, 200)


async def aggr_by_link_id(request, link_id):
    result = await get_aggr_teams_by_link_id(request, link_id)
    return json(result, 200)
