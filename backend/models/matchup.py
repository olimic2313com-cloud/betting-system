def matchup_boost(att_pos, def_pos):

    if att_pos in ["LW", "RW"]:
        return 1.1

    if att_pos == "ST":
        return 1.1

    return 1.0
