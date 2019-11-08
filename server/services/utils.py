import difflib


async def match_teams(real_team, all_teams):
    result = {"real_team": real_team}
    for i in range(1, len(all_teams) + 1):
        teams_by_link = []
        for team in all_teams[i]:
            teams_by_link.append(team["name"])
            result[i] = difflib.get_close_matches(real_team, teams_by_link, n=10, cutoff=0.2)
    return result


async def get_aggr_teams(request, session):
    link_id = 1
    teams = {}
    while True:
        async with session.get('http://localhost:8000/parse-links/{link_id}/teams'.format(link_id=link_id)) as resp:
            if resp.status == 404:
                break
            teams[link_id] = await resp.json()
            link_id += 1
    if request.raw_args.get("team"):
        close_matches = await match_teams(request.raw_args["team"], teams)
        return close_matches
    async with session.get('http://localhost:8000/real-teams') as resp:
        teams["real teams"] = await resp.json()
        return teams


async def get_aggr_teams_by_link_id(request, session, link_id):
    teams = {}
    async with session.get('http://localhost:8000/parse-links/{link_id}/teams'.format(link_id=link_id)) as resp:
        teams[link_id] = await resp.json()
    if request.raw_args.get("team"):
        close_matches = await match_teams(request.raw_args["team"], teams)
        return close_matches
    async with session.get('http://localhost:8000/real-teams') as resp:
        teams["real teams"] = await resp.json()
        return teams
