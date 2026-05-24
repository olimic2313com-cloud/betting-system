def get_role(pos):

    if pos in ["CB", "RB", "LB"]:
        return "defender"

    if pos in ["CDM", "CM", "CAM"]:
        return "midfielder"

    return "attacker"
