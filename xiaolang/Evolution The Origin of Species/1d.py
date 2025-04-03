# Constants for tokens
RED_TOKEN = 0
BLUE_TOKEN = 1


def check_animal_not_fully_fed_and_feed(animal, red_tokens_eaten_count, blue_tokens_eaten_count, token_to_feed):
    """
    Checks if an animal is not fully fed and, if possible, feeds it with one token.
    It updates the animal's consumed food count and (if applicable) its full-fed status.

    Parameters:
      animal: a list/tuple following the animal_template, i.e.,
              [traits (tuple), consumed_food_count (int), is_fully_fed (bool)]
      red_tokens_eaten_count: current count of red tokens already used for feeding
      blue_tokens_eaten_count: current count of blue tokens already used for feeding
      token_to_feed: constant RED_TOKEN (0) or BLUE_TOKEN (1) indicating which counter to update

    Returns:
      A tuple (updated_animal, new_red_tokens_eaten_count, new_blue_tokens_eaten_count, was_fed)
        - updated_animal: a new copy of the animal with an updated consumed_food_count and possibly updated is_fully_fed
        - new_red_tokens_eaten_count: updated red token count
        - new_blue_tokens_eaten_count: updated blue token count
        - was_fed: True if feeding occurred, or False if the animal was already full
    """
    # Make a shallow copy of the animal (traits tuple remains unchanged)
    updated_animal = [animal[0], animal[1], animal[2]]

    # Check if the animal is already fully fed.
    # We use the animal's is_fully_fed flag, which should be consistent with its food count.
    if updated_animal[2]:
        return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, False)

    # Determine additional tokens needed using the previously defined function.
    # If no tokens are needed, the animal is already full.
    remaining = calculate_animal_food_requirements(updated_animal)
    if remaining == 0:
        # Already fully fed; cannot feed further.
        return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, False)

    # Feed the animal by incrementing its consumed food count.
    updated_animal[1] += 1

    # Update token counters according to the token used.
    if token_to_feed == RED_TOKEN:
        red_tokens_eaten_count += 1
    elif token_to_feed == BLUE_TOKEN:
        blue_tokens_eaten_count += 1
    else:
        # If an invalid token is passed, we do nothing.
        pass

    # After feeding, check if the animal has now met its full food requirement.
    if calculate_animal_food_requirements(updated_animal) == 0:
        updated_animal[2] = True

    return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, True)


# --- For demonstration purposes ---
# Reusing the calculate_animal_food_requirements function from part (a):
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
    Returns the number of additional food tokens needed for an animal to be fully fed.
    Considers the traits that increase food requirement.
    """
    traits = animal[0]
    consumed = animal[1]

    # Hibernation: always fed.
    if TRAIT_HIBERNATION in traits:
        return 0

    total_required = 1  # Base requirement

    # Increase food requirements based on traits.
    if TRAIT_CARNIVORE in traits:
        total_required += 1
    if TRAIT_HIGH_BODY_WEIGHT in traits:
        total_required += 1
    if TRAIT_PARASITE in traits:
        total_required += 2

    remaining = total_required - consumed
    return remaining if remaining > 0 else 0


# Example usage:
animal = [(TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, False]
red_tokens_eaten_count = 2
blue_tokens_eaten_count = 2
token_to_feed = BLUE_TOKEN

result = check_animal_not_fully_fed_and_feed(animal, red_tokens_eaten_count, blue_tokens_eaten_count, token_to_feed)
print(result)
# Expected output:
# ([ (0, 3, 1), 1, False ], 2, 3, True)
# Interpreting: The animal now has consumed 1 token (still not fully fed since it needs 2 tokens total),
# red token count remains 2, blue token count increases to 3, and feeding occurred (True).
