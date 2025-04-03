# Constants (as defined previously)
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


def calculate_animal_food_requirements(animal):
    """
    Given an animal (format: [traits, consumed_food_count, is_fully_fed]),
    returns the number of additional food tokens required to become fully fed.
    """
    traits = animal[0]
    consumed = animal[1]

    # Hibernating animals are always fed.
    if TRAIT_HIBERNATION in traits:
        return 0

    total_required = 1  # base requirement
    if TRAIT_CARNIVORE in traits:
        total_required += 1
    if TRAIT_HIGH_BODY_WEIGHT in traits:
        total_required += 1
    if TRAIT_PARASITE in traits:
        total_required += 2

    remaining = total_required - consumed
    return remaining if remaining > 0 else 0


def calculate_food_crisis_survival_chance(players, player_index, animal_index, animal_can_attack, animal_attacked_by):
    """
    Estimates the survival chance of a given animal during the food crisis
    (i.e. at the end of the feeding phase) based on our heuristic.

    The heuristic is as follows:
      - Fully fed animals survive with chance 1.0.
      - Hungry non-carnivores have 0.0 chance (they go extinct).
      - Hungry carnivores must secure enough prey to feed. Let r be the number
        of food tokens still needed. They must attack (r+1)//2 times; to be safe,
        we require at least twice that number of prey. If the available prey count
        is greater than or equal to ((r+1)//2)*2, the feeding chance is 1.0,
        otherwise it is linearly scaled.

      Then, for each potential attacker (from animal_attacked_by), we assume:
        - Each attacker attacks with 50% chance.
        - If attacking, it picks uniformly among its potential prey.
        Thus, the chance that a given attacker does not attack our animal is:
          0.5 + 0.5 * ((n - 1)/n)
        where n is the number of prey available to that attacker.

    The overall survival chance is the product of the feeding survival chance and
    the survival modifiers from each potential attacker.

    Parameters:
      players: a list following the players_template.
      player_index: index of the player whose animal is being considered.
      animal_index: index of the animal within that player's animals.
      animal_can_attack: dictionary as produced by create_attack_map (keys: (p,a), values: list of prey).
      animal_attacked_by: dictionary as produced by create_attack_map (keys: (p,a), values: list of attackers).

    Returns:
      A float representing the estimated chance of survival.
    """
    # Get the animal in question.
    animal = players[player_index][0][animal_index]

    # Fully fed animals survive.
    if animal[2]:
        return 1.0

    # Hungry non-carnivores go extinct.
    if TRAIT_CARNIVORE not in animal[0]:
        return 0.0

    # For a hungry carnivore, compute the feeding survival chance.
    # r: tokens still needed.
    r = calculate_animal_food_requirements(animal)
    # Required number of attacks = (r+1)//2.
    required_attacks = (r + 1) // 2
    # To be safe, we want at least twice that many prey.
    required_prey = required_attacks * 2

    # Number of prey available (from the attack map)
    prey_list = animal_can_attack.get((player_index, animal_index), [])
    num_prey = len(prey_list)

    if num_prey >= required_prey:
        feeding_chance = 1.0
    else:
        feeding_chance = num_prey / float(required_prey)

    # Next, adjust for the risk of being attacked.
    # For each potential attacker, compute the chance that it does NOT attack our animal.
    attackers = animal_attacked_by.get((player_index, animal_index), [])
    survival_multiplier = 1.0
    for attacker in attackers:
        # Get the number of prey available to the attacker.
        attacker_prey = animal_can_attack.get(attacker, [])
        n = len(attacker_prey)
        if n > 0:
            # Attacker does not attack our animal if it either:
            #  (a) does not attack (50% chance), or
            #  (b) attacks and does not choose our animal (50% * (n-1)/n).
            not_attacked_prob = 0.5 + 0.5 * ((n - 1) / float(n))
        else:
            not_attacked_prob = 1.0
        survival_multiplier *= not_attacked_prob

    return feeding_chance * survival_multiplier


# --- Example usage ---
if __name__ == "__main__":
    # Define animals for player1 and player2 according to the example.
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

    # Example attack maps as produced by create_attack_map (see Q3(a)).
    # For this example, we assume:
    # animal_can_attack = { (0,0): [(1,0)],
    #                       (0,1): [(1,0), (1,1)],
    #                       (1,1): [(0,0), (0,1)] }
    # animal_attacked_by = { (1,0): [(0,0), (0,1)],
    #                        (1,1): [(0,1)],
    #                        (0,0): [(1,1)],
    #                        (0,1): [(1,1)] }
    animal_can_attack = {(0, 0): [(1, 0)],
                         (0, 1): [(1, 0), (1, 1)],
                         (1, 1): [(0, 0), (0, 1)]}
    animal_attacked_by = {(1, 0): [(0, 0), (0, 1)],
                          (1, 1): [(0, 1)],
                          (0, 0): [(1, 1)],
                          (0, 1): [(1, 1)]}
    player_index = 1
    animal_index = 1
    # We compute the survival chance for player 1's animal at index 1.
    # (Note: player indices are 0-based; so player2 is index 1)
    survival_chance = calculate_food_crisis_survival_chance(players, player_index, animal_index, animal_can_attack, animal_attacked_by)
    print(survival_chance)  # Expected output: 0.75
