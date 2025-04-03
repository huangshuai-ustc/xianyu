# Assume these constants are defined globally:
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
    Given an animal template:
       animal = [traits, consumed_food_count, is_fully_fed]
    returns the number of additional food tokens needed to be considered fully fed.
    """
    traits = animal[0]
    consumed = animal[1]

    # Hibernating species are always considered fed.
    if TRAIT_HIBERNATION in traits:
        return 0

    # Base requirement: at least 1 food token.
    total_requirement = 1

    # Traits that increase food requirements:
    if TRAIT_CARNIVORE in traits:
        total_requirement += 1
    if TRAIT_HIGH_BODY_WEIGHT in traits:
        total_requirement += 1
    if TRAIT_PARASITE in traits:
        total_requirement += 2

    remaining = total_requirement - consumed
    return remaining if remaining > 0 else 0


# Example usage:
animal = [(TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, False]
print(calculate_animal_food_requirements(animal))  # Expected output: 2
