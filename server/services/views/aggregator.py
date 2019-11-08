import aiohttp
from sanic.response import json

from services.utils import match_teams


async def aggregator(request):
    async with aiohttp.ClientSession() as session:
        link_id = 1
        teams = {}
        while True:
            async with session.get('http://localhost:8000/parse-links/{link_id}/teams'.format(link_id=link_id)) as resp:
                if resp.status == 404:
                    break
                teams[link_id] = await resp.json()
                link_id += 1
        if request.raw_args.get("team"):
            real_team = await match_teams(request.raw_args["team"], teams)
            return json(real_team)
        async with session.get('http://localhost:8000/real-teams') as resp:
            teams["real teams"] = await resp.json()
            return json(teams)
