import difflib

from common.rest_client.base_client_betting_data import BaseClientBettingData


client = BaseClientBettingData()


async def match_teams(real_team, all_teams):
    result = {"real_teams": real_team}
    for i in range(1, len(all_teams) + 1):
        teams_by_link = []
        for team in all_teams[i]:
            teams_by_link.append(team["name"])
            result[i] = difflib.get_close_matches(real_team, teams_by_link, n=10, cutoff=0.2)
    return result


async def get_aggr_teams(request, link_id=None):
    if link_id:
        resp = await client.get_teams(link_id)
    else:
        resp = await client.get_teams()
    resp_json = resp.json
    teams = {}
    for team in resp_json:
        if team["link_id"] in teams:
            teams[team["link_id"]].append(team)
        else:
            teams[team["link_id"]] = []
    if request.args.get("team"):
        close_matches = await match_teams(request.args.get("team"), teams)
        return close_matches
    resp = await client.get_real_teams()
    teams["real_teams"] = resp.json
    return teams
