# Constants
TRAIT_CARNIVORE = 0
TRAIT_COMMUNICATION = 1
TRAIT_COOPERATION = 2
TRAIT_SWIMMING = 3
TRAIT_RUNNING = 4
TRAIT_HIGH_BODY_WEIGHT = 5
TRAIT_BURROWING = 6
TRAIT_HIBERNATION = 7
TRAIT_CAMOUFLAGE = 8
TRAIT_POISONOUS = 9
TRAIT_SHARP_VISION = 10
TRAIT_PARASITE = 11


def can_predator_attack_prey(predator_animal, prey_animal):
    """
    Determines whether predator_animal can attack prey_animal.
    Conditions:
      1. The predator must have the carnivore trait.
      2. The predator must not be fully fed.
      3. Prey with the hibernation trait cannot be attacked.
      4. Prey with the poisonous trait are protected.
      5. If prey has camouflage, predator must have sharp vision.
      6. If prey has running, predator must also have running.
      7. If prey has high body weight, predator must also have high body weight.
      8. If either animal has swimming, then both must have it.
      9. If prey has burrowing and is fully fed, it cannot be attacked.
    """
    predator_traits = predator_animal[0]
    prey_traits = prey_animal[0]

    # 1. Predator must be carnivorous.
    if TRAIT_CARNIVORE not in predator_traits:
        return False
    # 2. Predator must not be fully fed.
    if predator_animal[2]:
        return False
    # 3. Prey with hibernation: cannot be attacked.
    if TRAIT_HIBERNATION in prey_traits:
        return False
    # 4. Prey with poisonous trait are protected.
    if TRAIT_POISONOUS in prey_traits:
        return False
    # 5. If prey has camouflage, predator must have sharp vision.
    if TRAIT_CAMOUFLAGE in prey_traits and TRAIT_SHARP_VISION not in predator_traits:
        return False
    # 6. If prey has running, predator must also have running.
    if TRAIT_RUNNING in prey_traits and TRAIT_RUNNING not in predator_traits:
        return False
    # 7. If prey has high body weight, predator must also have it.
    if TRAIT_HIGH_BODY_WEIGHT in prey_traits and TRAIT_HIGH_BODY_WEIGHT not in predator_traits:
        return False
    # 8. Swimming rule: if one has swimming then both must have it.
    if (TRAIT_SWIMMING in predator_traits or TRAIT_SWIMMING in prey_traits) and not (
            TRAIT_SWIMMING in predator_traits and TRAIT_SWIMMING in prey_traits):
        return False
    # 9. If prey has burrowing and is fully fed, it cannot be attacked.
    if TRAIT_BURROWING in prey_traits and prey_animal[2]:
        return False

    return True


def create_attack_map(players):
    """
    Creates two dictionaries:
      - animal_can_attack: keys are animals (identified as (player_index, animal_index))
        and values are lists of animals (as (player_index, animal_index)) that the key animal can attack.
      - animal_attacked_by: keys are animals and values are lists of animals that can attack that animal.

    We consider only pairs of animals belonging to different players.
    """
    animal_can_attack = {}
    animal_attacked_by = {}

    # Initialize an entry for every animal in the game.
    for p, player in enumerate(players):
        animals = player[0]
        for a, animal in enumerate(animals):
            key = (p, a)
            animal_can_attack[key] = []
            animal_attacked_by[key] = []

    # For every animal pair from different players, check if an attack is possible.
    for p, player in enumerate(players):
        animals_p = player[0]
        for a, predator in enumerate(animals_p):
            attacker_key = (p, a)
            for q, other_player in enumerate(players):
                if q == p:
                    continue  # skip same player's animals
                animals_q = other_player[0]
                for b, prey in enumerate(animals_q):
                    prey_key = (q, b)
                    if can_predator_attack_prey(predator, prey):
                        animal_can_attack[attacker_key].append(prey_key)
                        animal_attacked_by[prey_key].append(attacker_key)
    filtered_animal_can_attack = {key: value for key, value in animal_can_attack.items() if value}
    filtered_animal_attacked_by = {key: value for key, value in animal_attacked_by.items() if value}
    return filtered_animal_can_attack, filtered_animal_attacked_by


# --- Example usage ---
if __name__ == "__main__":
    # Define players and their animals according to the example.
    player1_animals = [
        [(TRAIT_CARNIVORE,), 0, False],
        [(TRAIT_RUNNING, TRAIT_CARNIVORE), 0, False]
    ]
    player2_animals = [
        [(TRAIT_COMMUNICATION,), 0, False],
        [(TRAIT_RUNNING, TRAIT_CARNIVORE), 0, False]
    ]
    player1 = [player1_animals]
    player2 = [player2_animals]
    players = [player1, player2]

    animal_can_attack, animal_attacked_by = create_attack_map(players)
    print("animal_can_attack:", animal_can_attack)
    print("animal_attacked_by:", animal_attacked_by)

    # Expected output:
    # animal_can_attack: {(0, 0): [(1, 0)], (0, 1): [(1, 0), (1, 1)], (1, 0): [], (1, 1): [(0, 0), (0, 1)]}
    # animal_attacked_by: {(0, 0): [(1, 1)], (0, 1): [(1, 1)], (1, 0): [(0, 0), (0, 1)], (1, 1): [(0, 1)]}
