
def get_zone(pos):

    if pos in ["LW", "LB"]:
        return "left"

    if pos in ["RW", "RB"]:
        return "right"

    return "center"
