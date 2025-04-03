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


def count_animal_victory_points(animal):
    """
    Computes the victory points for a fully fed animal.

    Victory points are calculated as follows:
      - +2 points for the animal itself.
      - +1 point for each trait card on the animal.
      - +1 point for each extra food token required over the base 1 token.
        (For example, an animal with a parasite trait requires 2 extra tokens and thus adds +2.)

    Note:
      - Animals with the Hibernation trait are always considered fully fed,
        and do not require any food tokens (thus no extra points for feeding).
      - If the animal is not fully fed (animal[2] is False), we return 0.

    Parameters:
      animal: a list or tuple following the animal_template, where
          animal[0] is a tuple of trait constants,
          animal[1] is the consumed food count,
          animal[2] is a boolean indicating if the animal is fully fed.

    Returns:
      An integer representing the victory points for the animal.
    """
    # Only fully fed animals contribute victory points.
    if not animal[2]:
        return 0

    traits = animal[0]

    # Base points for the animal and for each trait
    animal_points = 2
    trait_points = len(traits)

    # Compute extra food requirements (beyond the base 1 token)
    # If the animal has Hibernation, it's always fed and doesn't require tokens.
    if TRAIT_HIBERNATION in traits:
        extra_food_points = 0
    else:
        total_required = 1  # base food requirement
        if TRAIT_CARNIVORE in traits:
            total_required += 1
        if TRAIT_HIGH_BODY_WEIGHT in traits:
            total_required += 1
        if TRAIT_PARASITE in traits:
            total_required += 2
        # Extra tokens are those above the base requirement
        extra_food_points = total_required - 1

    return animal_points + trait_points + extra_food_points


# Example usage:
animal = [(TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, True]
print(count_animal_victory_points(animal))
# For this animal:
#   - Base animal points: 2
#   - Number of traits: 3  (i.e., +3)
#   - Extra food requirements: Carnivore adds +1 (total requirement = 1 + 1 = 2, extra = 1)
# Total = 2 + 3 + 1 = 6
