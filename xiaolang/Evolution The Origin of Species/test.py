#################
#   CONSTANTS   #
#################
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

# used for question 1 (d)
RED_TOKEN = 0
BLUE_TOKEN = 1

# used to index a animal_template
ANIMAL_TRAITS = 0
ANIMAL_FOOD_COUNT = 1
ANIMAL_IS_FULLY_FED = 2

# used to index a player_template
PLAYER_ANIMALS = 0

#################
# Question 1(a) #
#################
def calculate_animal_food_requirements(animal):
    food = 0
    if animal[2]:
        return food
    if TRAIT_CARNIVORE in animal[0]:
        food += 1
    if TRAIT_HIGH_BODY_WEIGHT in animal[0]:
        food += 1
    if TRAIT_PARASITE in animal[0]:
        food += 2
    return food + 1 - animal[1]


#################
# Question 1(b) #
#################
def count_animal_victory_points(animal):
    traits = animal[0]
    # The initial point is 2 because every living animal has 2 points
    points = 2
    # Every trait adds 1 point
    points += len(traits)
    # Compute extra food requirements
    # Hibernation trait doesn't have contribution
    if TRAIT_HIBERNATION in traits:
        return points
    else:
        if TRAIT_CARNIVORE in traits:
            points += 1
        if TRAIT_HIGH_BODY_WEIGHT in traits:
            points += 1
        if TRAIT_PARASITE in traits:
            points += 2
    return points

#################
# Question 1(c) #
#################
def can_predator_attack_prey(predator_animal, prey_animal):
    # If the predator is a carnivore
    predator_traits = predator_animal[0]
    prey_traits = prey_animal[0]
    # Check the predator must be carnivorous
    if TRAIT_CARNIVORE not in predator_traits:
        return False
    # Won't eat when it is full
    if predator_animal[2]:
        return False
    # Prey with hibernation cannot be attacked
    if TRAIT_HIBERNATION in prey_traits:
        return False
    # Prey with poisonous trait are protected
    if TRAIT_POISONOUS in prey_traits:
        return False
    # If prey has camouflage, predator must have sharp vision
    if (TRAIT_CAMOUFLAGE in prey_traits and
            TRAIT_SHARP_VISION not in predator_traits):
        return False
    # If prey has running, predator must also have running
    if TRAIT_RUNNING in prey_traits and TRAIT_RUNNING not in predator_traits:
        return False
    # If prey has high body weight, predator must also have high body weight
    if (TRAIT_HIGH_BODY_WEIGHT in prey_traits
            and TRAIT_HIGH_BODY_WEIGHT not in predator_traits):
        return False
    # if either animal has Swimming, both must have it.
    if ((TRAIT_SWIMMING in predator_traits or TRAIT_SWIMMING in prey_traits)
            and not (TRAIT_SWIMMING in predator_traits
                     and TRAIT_SWIMMING in prey_traits)):
        return False
    # If prey has burrowing and is fully fed, it cannot be attacked
    if TRAIT_BURROWING in prey_traits and prey_animal[2]:
        return False
    return True
#################
# Question 1(d) #
#################

def check_animal_not_fully_fed_and_feed(
    animal, red_tokens_eaten_count, blue_tokens_eaten_count, token_to_feed
    ):
    # Define updates_animal from animal
    updated_animal = list(animal)
    # if the animal is already fully fed, return directly
    if animal[2]:
        return (
            updated_animal,
            red_tokens_eaten_count,
            blue_tokens_eaten_count,
            False
        )
    # Calculate the food required for the animal
    # If the animal requires 0 food, return directly
    if calculate_animal_food_requirements(animal) == 0:
        return (
            updated_animal,
            red_tokens_eaten_count,
            blue_tokens_eaten_count,
            False
        )
    # Feed the animal, consumed food count + 1.
    updated_animal[1] += 1
    # Update token according to the token used.
    if token_to_feed == RED_TOKEN:
        red_tokens_eaten_count += 1
    elif token_to_feed == BLUE_TOKEN:
        blue_tokens_eaten_count += 1
    # Check if the animals are fully fed
    if calculate_animal_food_requirements(updated_animal) == 0:
        updated_animal[2] = True
    return (
        updated_animal,
        red_tokens_eaten_count,
        blue_tokens_eaten_count,
        True
    )

#################
# Question 2(a) #
#################

def feed_animal_red_token(player_animals, animal_to_feed_index):
   # Define updated_player_animals from player_animals
    updated_animals = [[animal[0], animal[1], animal[2]] for animal in player_animals]
    # Initialize red_tokens and blue_tokens
    red_tokens_eaten = 0
    blue_tokens_eaten = 0
    # Save used pairs
    used_pairs = set()

    def propagate_feed(index, token_to_feed):
        # decline nonlocal variables
        nonlocal red_tokens_eaten, blue_tokens_eaten
        nonlocal updated_animals, used_pairs
        # Take out the animal to be fed from the list
        animal = updated_animals[index]
        # Return if no feeding occurred
        if animal[2]:
            return
        # Get updated animal using check_animal_not_fully_fed_and_feed
        fed_result = check_animal_not_fully_fed_and_feed(
            animal,red_tokens_eaten,blue_tokens_eaten,token_to_feed)
        updated_animal, red_tokens_eaten, blue_tokens_eaten, fed = fed_result
        # Update the animal in updated_player_animals
        updated_animals[index] = updated_animal
        # Return if no feeding occurred
        if not fed:
            return
        traits = updated_animal[0]
        pairwise_trait = None
        # Deal with communication and cooperation
        if TRAIT_COOPERATION in traits:
            pairwise_trait = TRAIT_COOPERATION
        elif TRAIT_COMMUNICATION in traits:
            pairwise_trait = TRAIT_COMMUNICATION
        if pairwise_trait is None:
            return
        # Determine the token type for propagation
        # Cooperation uses BLUE_TOKEN
        # Communication uses RED_TOKEN
        if pairwise_trait == TRAIT_COOPERATION:
            propagation_token = BLUE_TOKEN
        else:
            propagation_token = RED_TOKEN
        candidate = None
        # Check right neighbor (index+1)
        if (index + 1 < len(updated_animals)
                and not updated_animals[index + 1][2]):
            # Attempt to establish a connection
            if (index, index + 1) not in used_pairs:
                candidate = index + 1
        # Check left neighbor (index-1)
        if (candidate is None and index - 1 >= 0
                and not updated_animals[index - 1][2]):
            if (index - 1, index) not in used_pairs:
                candidate = index - 1
        # If there is connection on both sides, right side firstly
        if candidate is not None:
            pair = (min(index, candidate), max(index, candidate))
            used_pairs.add(pair)
            propagate_feed(candidate, propagation_token)

    # Begin by feeding the selected animal with a red token.
    propagate_feed(animal_to_feed_index, RED_TOKEN)
    return (updated_animals, red_tokens_eaten, blue_tokens_eaten)
##################
# Question 2(b)  #
##################
def find_greedy_feeding_count(players, focus_player_index, red_tokens_available):
    import copy
    # Deep copy prevents changes to the original content
    copy_players = copy.deepcopy(players)
    # Get length of players
    num = len(copy_players)
    # # Initialize index
    current_index = 0
    # Accumulated number of red tokens since the last focus round
    total_red_token = 0
    # For storing the results
    return_tuple = []
    total_token_no_move = 0
    # Loop
    while True:
        # If the red token is exhausted
        # advance to the focal player turn first
        # record the accumulated value
        # and then exit
        if red_tokens_available <= 0:
            while current_index != focus_player_index:
                current_index = (current_index + 1) % num
            if total_red_token > 0:
                return_tuple.append(total_red_token)
            break
        # Focus player turn, record the accumulated value
        if current_index == focus_player_index:
            return_tuple.append(total_red_token)
            total_red_token = 0
            # The focus player's turn itself does not consume tokens
            # and is not counted towards the number of no moves
        else:
            # Non focused player turn: simulating greedy move
            player = copy_players[current_index]
            animals = player[0]
            best_move = list()
            best_red = 0
            for i, animal in enumerate(animals):
                if not animal[2]:
                    # For every hungry animal, call feed_animal_red_token
                    copy_animals = [[a[0], a[1], a[2]] for a in animals]
                    feed_result = feed_animal_red_token(copy_animals, i)
                    updated_animals, red_used, _ = feed_result
                    if red_used > best_red:
                        best_red = red_used
                        best_move = updated_animals
            if best_move is None or best_red == 0:
                total_token_no_move += 1
            else:
                total_token_no_move = 0
                copy_players[current_index][0] = best_move
                if best_red <= red_tokens_available:
                    tokens_taken = best_red
                else:
                    tokens_taken = red_tokens_available
                red_tokens_available -= tokens_taken
                total_red_token += tokens_taken
            # If all non focused players are unable to consume tokens
            # exit the loop
            if total_token_no_move >= (num - 1):
                break
        current_index = (current_index + 1) % num
    return return_tuple




##################
# Question 3(a)  #
##################

def create_attack_map(players):
# Initialize dictionaries to store results
    animal_can_attack = {}
    animal_attacked_by = {}
    # Initialize an entry for every animal in the game.
    for i, player in enumerate(players):
        animals = player[0]
        for j, animal in enumerate(animals):
            key = (i, j)
            animal_can_attack[key] = []
            animal_attacked_by[key] = []
    # Check if an attack is possible for every animal pair
    for i, player in enumerate(players):
        animals_predator = player[0]
        for j, predator in enumerate(animals_predator):
            attacker_key = (i, j)
            for k, other_player in enumerate(players):
                if k == i:
                    continue  # skip same player's animals
                animals_q = other_player[0]
                for l, prey in enumerate(animals_q):
                    prey_key = (k, l)
                    if can_predator_attack_prey(predator, prey):
                        animal_can_attack[attacker_key].append(prey_key)
                        animal_attacked_by[prey_key].append(attacker_key)
    # Filter out empty keys
    filtered_animal_can_attack = {}
    filtered_animal_attacked_by = {}
    for key, value in animal_can_attack.items():
        if value:
            filtered_animal_can_attack[key] = value
    for key, value in animal_attacked_by.items():
        if value:
            filtered_animal_attacked_by[key] = value
    return filtered_animal_can_attack, filtered_animal_attacked_by
##################
# Question 3(b)  #
##################
def calculate_food_crisis_survival_chance(
    players, player_index, animal_index, animal_can_attack, animal_attacked_by
    ):
    # Get the animal list
    animal = players[player_index][0][animal_index]
    # Fully fed animals survive.
    needed_food = calculate_animal_food_requirements(animal)
    # Required number of attacks = (r+1)//2.
    required_attacks = (needed_food + 1) // 2
    # To be safe, it needs at least 2 times preys
    required_prey = required_attacks * 2
    # Number of prey available (from the attack map)
    prey_list = animal_can_attack.get((player_index, animal_index), [])
    num_prey = len(prey_list)
    # If there are enough prey, the animal survives
    if num_prey >= required_prey:
        feeding_chance = 1.0
    else:
        feeding_chance = num_prey / float(required_prey)
    # Adjust for the risk of being attacked
    # Calculate the probability of not being attacked
    attackers = animal_attacked_by.get((player_index, animal_index), [])
    survival_multiplier = 1.0
    for attacker in attackers:
        # Get the number of prey available to the attacker
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

##################
#  Question 4    #
##################
def simulate_optimal_feeding_phase_gameplay(players, focus_player_index, red_tokens_available):
    import copy
    # Get the number of players
    num = len(players)
    # compute the number if red tokens taken by non-focus players
    # Initialize the dictionary to store the non focus moves
    non_focus_moves = {}
    # Loop through all players
    for i, player in enumerate(players):
        # Skip the focus player
        if i == focus_player_index:
            continue
        best = 0
        animals = player[0]
        for j, animal in enumerate(animals):
            # If not fed
            if not animal[2]:
                sim_animals = [[a[0], a[1], a[2]] for a in animals]
                # red_used is needing
                _, red_used, _ = feed_animal_red_token(sim_animals, j)
                # Check if the red_used is the best
                if red_used > best:
                    best = red_used
        # Store the best move
        non_focus_moves[i] = best

    # Define function `search` to assist, here is its description:
    # - red: remaining red tokens
    # - current: current player index (turn order cycles 0,1,...,n-1)
    # - focus_state: the current state (list) of focus player's animals
    # - focus_turns: the sequence of focus moves (animal indices chosen)
    #
    # Subtract non_focus_moves[player] when a non-focus turn comes
    # and leave that player's state unchanged.
    #
    # At focus turns, we branch over all possible moves
    # using feed_animal_red_token on the focus_state.

    def search(red, current, focus_state, focus_turns):
        if red <= 0:
            # Build final players state
            final_players = []
            for k, player in enumerate(players):
                if k == focus_player_index:
                    final_players.append([focus_state])
                else:
                    final_players.append(copy.deepcopy(player))
            # Call create_attack_map to get the attack map
            attack_map, attacked_by = create_attack_map(final_players)
            focus_animals = focus_state
            total = 0.0
            count = len(focus_animals)
            for l, focus_animal in enumerate(focus_animals):
                survive = calculate_food_crisis_survival_chance(
                    final_players,
                    focus_player_index,
                    l,
                    attack_map,
                    attacked_by
                )
                points = count_animal_victory_points(focus_animal)
                total += survive * points
            score = total
            return score, focus_turns
        if current != focus_player_index:
            # Non-focus turn: subtract fixed red tokens.
            tokens = non_focus_moves.get(current, 0)
            if tokens > red:
                tokens = red
            new_red = red - tokens
            next_player = (current + 1) % num
            return search(new_red, next_player, focus_state, focus_turns)
        else:
            # Focus player's turn: branch over all possible moves.
            best_score = -1.0
            best_seq = None
            move_found = False
            # Try each animal (by index) that is not fully fed.
            for m, focus_animal in enumerate(focus_state):
                if not focus_animal[2]:
                    move_found = True
                    sim_focus = [[a[0], a[1], a[2]] for a in focus_state]
                    # new_focus_state, red_used are needing
                    feed_tuple = feed_animal_red_token(sim_focus, m)
                    new_focus_state, red_used, _ = feed_tuple
                    if 0 < red_used <= red:
                        new_red = red - red_used
                        # searching the next player
                        next_player = (current + 1) % num
                        score, seq = search(
                            new_red,
                            next_player,
                            new_focus_state,
                            focus_turns + [m]
                        )
                        # choose the move with the lowest animal index
                        if score > best_score or (
                                score == best_score and
                                (seq and seq[0] < (best_seq[0]
                                if best_seq else 10 ** 99))):
                            # update best_score and best_seq
                            best_score = score
                            best_seq = seq
            # If no move is possible
            if not move_found:
                next_player = (current + 1) % num
                return search(red, next_player, focus_state, focus_turns)
            return best_score, best_seq

    focus_initial = copy.deepcopy(players[focus_player_index][0])
    best_result = search(red_tokens_available, 0, focus_initial, [])
    best_score, best_turns = best_result
    return best_score, best_turns

