import difflib


async def match_teams(real_team, all_teams):
    result = {"real_team": real_team}
    for i in range(1, len(all_teams) + 1):
        teams_by_link = []
        for team in all_teams[i]:
            teams_by_link.append(team["name"])
            result[i] = difflib.get_close_matches(real_team, teams_by_link, n=10, cutoff=0.2)
    return result
