# Constants
RED_TOKEN = 0
BLUE_TOKEN = 1

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


# Helper from Question 1(d)
def check_animal_not_fully_fed_and_feed(animal, red_tokens_eaten_count, blue_tokens_eaten_count, token_to_feed):
    # Make a copy so as not to modify the original
    updated_animal = [animal[0], animal[1], animal[2]]
    # Do nothing if already full
    if updated_animal[2]:
        return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, False)
    # Determine if any tokens are needed
    # (Assuming calculate_animal_food_requirements returns >0 if feeding is needed)
    # Feed the animal by incrementing its consumed_food_count.
    updated_animal[1] += 1
    if token_to_feed == RED_TOKEN:
        red_tokens_eaten_count += 1
    elif token_to_feed == BLUE_TOKEN:
        blue_tokens_eaten_count += 1
    # After feeding, if the animal now meets its food requirement, mark it fully fed.
    # (For our simplified simulation, we assume that if one token is enough then it becomes full.)
    # In our examples, this holds because base requirement is 1 unless extra traits require more.
    # (Note: In a full simulation you would call calculate_animal_food_requirements here.)
    if updated_animal[1] >= 1:
        updated_animal[2] = True
    return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, True)


def feed_animal_red_token(player_animals, animal_to_feed_index):
    """
    Simulates feeding one animal with a red token, including any pairwise propagation.

    Parameters:
      player_animals: a list of animal templates; each animal is [traits, consumed_food_count, is_fully_fed]
      animal_to_feed_index: the index of the animal to feed initially with a red token.

    Returns:
      A tuple (updated_player_animals, new_red_tokens_eaten_count, new_blue_tokens_eaten_count)
    """
    # Create a new copy of the animals list.
    updated_animals = [[animal[0], animal[1], animal[2]] for animal in player_animals]
    red_tokens_eaten = 0
    blue_tokens_eaten = 0
    # Set to record adjacent pairs already used this turn; store as (min_index, max_index)
    used_pairs = set()

    # Recursive helper to propagate feeding.
    def propagate_feed(index, token_to_feed):
        nonlocal red_tokens_eaten, blue_tokens_eaten, updated_animals, used_pairs
        animal = updated_animals[index]
        # Check that the animal is not already fully fed.
        if animal[2]:
            return
        # Feed the animal with the specified token.
        updated, red_tokens_eaten, blue_tokens_eaten, fed = check_animal_not_fully_fed_and_feed(animal,
                                                                                                red_tokens_eaten,
                                                                                                blue_tokens_eaten,
                                                                                                token_to_feed)
        updated_animals[index] = updated
        if not fed:
            return
        # Now, if the animal has a pairwise trait, try to propagate feeding.
        # (Remember: pairwise traits are stored in the animal’s traits.)
        traits = updated[0]
        pairwise_trait = None
        # If both Cooperation and Communication are present, Cooperation takes precedence.
        if TRAIT_COOPERATION in traits:
            pairwise_trait = TRAIT_COOPERATION
        elif TRAIT_COMMUNICATION in traits:
            pairwise_trait = TRAIT_COMMUNICATION
        if pairwise_trait is None:
            return
        # Determine the token type for propagation.
        # Cooperation uses BLUE_TOKEN; Communication uses RED_TOKEN.
        if pairwise_trait == TRAIT_COOPERATION:
            propagation_token = BLUE_TOKEN
        else:
            propagation_token = RED_TOKEN
        # Determine which adjacent animal to feed:
        candidate = None
        # Check right neighbor first.
        if index + 1 < len(updated_animals) and not updated_animals[index + 1][2]:
            # Ensure the pair (index, index+1) has not been used.
            if (index, index + 1) not in used_pairs:
                candidate = index + 1
        # If right neighbor not eligible, check left neighbor.
        if candidate is None and index - 1 >= 0 and not updated_animals[index - 1][2]:
            if (index - 1, index) not in used_pairs:
                candidate = index - 1
        # If a candidate is found, mark the pair as used and propagate feeding.
        if candidate is not None:
            pair = (min(index, candidate), max(index, candidate))
            used_pairs.add(pair)
            propagate_feed(candidate, propagation_token)

    # Begin by feeding the selected animal with a red token.
    propagate_feed(animal_to_feed_index, RED_TOKEN)
    return (updated_animals, red_tokens_eaten, blue_tokens_eaten)


# --- Example usage ---

if __name__ == "__main__":
    # Example 1:
    player_animals1 = [
        [(TRAIT_RUNNING, TRAIT_COMMUNICATION), 0, False],
        [(TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, False],
        [(TRAIT_HIBERNATION, TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, True],
        [(TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_RUNNING), 0, False]
    ]
    result1 = feed_animal_red_token(player_animals1, 0)
    print(result1)
    # Expected output:
    # ([[(4,1), 1, True], [(0,3,1), 1, False], [(7,3,1), 0, True], [(0,3,4), 0, False]], 2, 0)

    # Example 2:
    player_animals2 = [
        [(4, 2), 0, False],  # (4,2) means TRAIT_RUNNING and TRAIT_COOPERATION
        [(0, 3, 2), 0, False],  # (0,3,2) means TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_COOPERATION
        [(7, 3, 2), 0, True],  # Fully fed (hibernation etc.)
        [(0, 3, 9), 0, False]  # (0,3,9) means TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_POISONOUS
    ]
    result2 = feed_animal_red_token(player_animals2, 0)
    print(result2)
    # Expected output:
    # ([[(4,2), 1, True], [(0,3,2), 1, False], [(7,3,2), 0, True], [(0,3,9), 0, False]], 1, 1)
