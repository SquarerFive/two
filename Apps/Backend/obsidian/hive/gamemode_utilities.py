# Gamemode Utilities

def get_gamemode_name(id):
    if (id is 0):
        return "Conquest"
    if (id is 1):
        return "Domination"
    if (id is 2):
        return "Team Deathmatch"
    if (id is 3):
        return "Zombies"
    if (id is 4):
        return "Disarm"
