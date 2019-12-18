import difflib

from common.rest_client.base_client_betting_data import BaseClientBettingData


async def match_teams(team_for_match, teams):
    result = {"real_teams": team_for_match}
    teams_name = []
    for team in teams["teams"]:
        teams_name.append(team["name"])
    result["teams"] = difflib.get_close_matches(team_for_match, teams_name, n=10, cutoff=0.2)
    return result


async def get_aggr_teams(team_for_match=None, **kwargs):
    teams = {}
    client = BaseClientBettingData()
    resp_teams = await client.get_teams(**kwargs)
    teams["teams"] = resp_teams
    if team_for_match:
        close_match_teams = await match_teams(team_for_match, teams)
        return close_match_teams
    resp_real_teams = await client.get_real_teams()
    teams["real_teams"] = resp_real_teams
    return teams
