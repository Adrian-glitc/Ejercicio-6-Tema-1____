class VideoGameCharacter:
    def __init__(self, name, is_human):
        self.name = name
        self.is_human = is_human

def separate_characters_by_type(characters):
    humans = []
    non_humans = []
    for character in characters:
        if character.is_human:
            humans.append(character.name)
        else:
            non_humans.append(character.name)
    return sorted(humans), sorted(non_humans)