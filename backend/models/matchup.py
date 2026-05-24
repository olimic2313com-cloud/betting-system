def matchup_boost(att_pos, def_pos):

    if att_pos in ["LW","RW"] and def_pos in ["RB","LB"]:
        return 1.15

    if att_pos == "ST" and def_pos == "CB":
        return 1.1

    return 1.0
