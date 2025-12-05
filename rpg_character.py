
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    #Validate Name
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    #Validate Stat
    for stat in (strength, intelligence, charisma):
        if not isinstance(stat, int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    #Create Dot
    def create_dot(stat):
        return full_dot * stat + empty_dot * (10 - stat)

    return (
        f'{name}\n'
        f'STR {create_dot(strength)}\n'
        f'INT {create_dot(intelligence)}\n'
        f'CHA {create_dot(charisma)}'
    )
#Result
print(create_character("ren", 4, 2, 1))