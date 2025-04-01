
from Personajes import VideoGameCharacter
from Personajes import separate_characters_by_type
# Example usage
if __name__ == "__main__":
    characters = [
        VideoGameCharacter("Mario", True),
        VideoGameCharacter("Pikachu", False),
        VideoGameCharacter("Lara Croft", True),
        VideoGameCharacter("Bowser", False)
    ]
    
    humans, non_humans = separate_characters_by_type(characters)
    print("Human Characters:", humans)
    print("Non-Human Characters:", non_humans)