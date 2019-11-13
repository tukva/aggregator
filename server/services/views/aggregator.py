import aiohttp
from sanic.response import json

from services.utils import get_aggr_teams, get_aggr_teams_by_link_id


async def aggr(request):
    result = await get_aggr_teams(request)
    return json(result, 200)


async def aggr_by_link_id(request, link_id):
    async with aiohttp.ClientSession() as session:
        result = await get_aggr_teams_by_link_id(request, session, link_id)
        return json(result, 200)
