from http import HTTPStatus

from sanic.response import json

from services.utils import get_aggr_teams


async def aggr(request):
    result = await get_aggr_teams(request)
    return json(result, HTTPStatus.OK)


async def aggr_by_link_id(request, link_id):
    result = await get_aggr_teams(request, link_id)
    return json(result, HTTPStatus.OK)
