def calculate_league_avg(data):

    all_values = []

    for team in data.values():

        for side in ["home", "away"]:
            all_values.extend(team.get(side, []))

    if not all_values:
        return 10  # safe default

    return sum(all_values) / len(all_values)
