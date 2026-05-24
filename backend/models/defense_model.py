def get_def_strength(team_data, side, league_avg):

    values = team_data.get(side, [])

    if not values:
        return 1.0

    avg = sum(values) / len(values)

    return avg / league_avg
