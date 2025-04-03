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


def can_predator_attack_prey(predator_animal, prey_animal):
    """
    Determines whether predator_animal can attack prey_animal based on their traits.

    Conditions:
      1. The predator must have the carnivore trait.
      2. The predator must not be fully fed.
      3. Prey with the hibernation trait are always considered fed and cannot be attacked.
      4. Prey with the poisonous trait are protected from attack.
      5. If the prey has the camouflage trait, the predator must have the sharp vision trait.
      6. If the prey has the running trait, the predator must also have the running trait.
      7. If the prey has the high body weight trait, the predator must also have the high body weight trait.
      8. Swimming rule: if either animal has the swimming trait, then both must have it.
      9. If the prey has the burrowing trait and is fully fed, it cannot be attacked.

    Parameters:
      predator_animal: a list following the animal_template.
      prey_animal: a list following the animal_template.

    Returns:
      True if the predator can attack the prey based on the rules, otherwise False.
    """
    predator_traits = predator_animal[0]
    prey_traits = prey_animal[0]

    # 1. The predator must be carnivorous.
    if TRAIT_CARNIVORE not in predator_traits:
        return False

    # 2. The predator cannot be fully fed.
    if predator_animal[2]:
        return False

    # 3. Prey with hibernation are always considered fed => cannot be attacked.
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

    # 7. If prey has high body weight, predator must also have high body weight.
    if TRAIT_HIGH_BODY_WEIGHT in prey_traits and TRAIT_HIGH_BODY_WEIGHT not in predator_traits:
        return False

    # 8. Swimming rule: if either animal has Swimming, both must have it.
    if (TRAIT_SWIMMING in predator_traits or TRAIT_SWIMMING in prey_traits) and not (
            TRAIT_SWIMMING in predator_traits and TRAIT_SWIMMING in prey_traits):
        return False

    # 9. If prey has burrowing and is fully fed, it cannot be attacked.
    if TRAIT_BURROWING in prey_traits and prey_animal[2]:
        return False

    return True


# Example usage:
predator_animal = [(TRAIT_CARNIVORE, TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, False]
prey_animal_1 = [(TRAIT_SWIMMING, TRAIT_COMMUNICATION), 0, False]
prey_animal_2 = [(TRAIT_RUNNING, TRAIT_COMMUNICATION), 0, False]

print(can_predator_attack_prey(predator_animal, prey_animal_1))  # Expected output: True
print(can_predator_attack_prey(predator_animal, prey_animal_2))  # Expected output: False
