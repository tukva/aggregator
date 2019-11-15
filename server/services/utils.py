import difflib

from common.rest_client.base_clients import BaseClientParser


client = BaseClientParser(host='http://localhost', port=8000)


async def match_teams(real_team, all_teams):
    result = {"real_team": real_team}
    for i in range(1, len(all_teams) + 1):
        teams_by_link = []
        for team in all_teams[i]:
            teams_by_link.append(team["name"])
            result[i] = difflib.get_close_matches(real_team, teams_by_link, n=10, cutoff=0.2)
    return result


async def get_aggr_teams(request):
    link_id = 1
    teams = {}
    while True:
        resp = await client.get_teams_by_link(link_id)
        if resp["status"] == 404:
            break
        teams[link_id] = resp["json"]
        link_id += 1
    if request.args.get("team"):
        close_matches = await match_teams(request.args.get("team"), teams)
        return close_matches
    teams["real teams"] = await client.get_real_teams()
    return teams


async def get_aggr_teams_by_link_id(request, link_id):
    teams = {}
    resp = await client.get_teams_by_link(link_id)
    teams[link_id] = resp["json"]
    if request.args.get("team"):
        close_matches = await match_teams(request.args.get("team"), teams)
        return close_matches
    teams["real teams"] = await client.get_real_teams()
    return teams
