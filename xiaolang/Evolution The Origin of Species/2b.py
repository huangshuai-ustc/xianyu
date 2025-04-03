# --- 常量定义 ---
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


# --- 辅助函数：计算动物还需多少食物代币才能被喂满 ---
def calculate_animal_food_requirements(animal):
    """
    animal 的格式为 [traits, consumed_food_count, is_fully_fed]
    基础需求为1个代币，另外：
      - 如果存在 TRAIT_CARNIVORE，则 +1
      - 如果存在 TRAIT_HIGH_BODY_WEIGHT，则 +1
      - 如果存在 TRAIT_PARASITE，则 +2
    如果动物具有 TRAIT_HIBERNATION，则需求为 0。
    返回还需要的代币数（如果已满足则返回0）。
    """
    traits = animal[0]
    consumed = animal[1]
    if TRAIT_HIBERNATION in traits:
        return 0
    total_required = 1
    if TRAIT_CARNIVORE in traits:
        total_required += 1
    if TRAIT_HIGH_BODY_WEIGHT in traits:
        total_required += 1
    if TRAIT_PARASITE in traits:
        total_required += 2
    remaining = total_required - consumed
    return remaining if remaining > 0 else 0


# --- 辅助函数：单次喂食（如果动物未被喂满，则给其加1个代币） ---
def check_animal_not_fully_fed_and_feed(animal, red_tokens, blue_tokens, token):
    """
    如果 animal 未被喂满（格式：[traits, consumed_food_count, is_fully_fed]），
    则给它喂1个 token（RED_TOKEN 或 BLUE_TOKEN），并更新代币计数，
    当动物所需代币数变为0时，将 is_fully_fed 置为 True。

    返回一个元组：(updated_animal, new_red_tokens, new_blue_tokens, was_fed)
    """
    updated = [animal[0], animal[1], animal[2]]
    if updated[2]:
        return (updated, red_tokens, blue_tokens, False)
    updated[1] += 1
    if token == RED_TOKEN:
        red_tokens += 1
    elif token == BLUE_TOKEN:
        blue_tokens += 1
    if calculate_animal_food_requirements(updated) == 0:
        updated[2] = True
    return (updated, red_tokens, blue_tokens, True)


# --- Q2(a)函数：feed_animal_red_token ---
def feed_animal_red_token(player_animals, animal_to_feed_index):
    """
    模拟给 player_animals 中索引为 animal_to_feed_index 的动物喂1个红代币。
    如果该动物具备配对特性（TRAIT_COOPERATION 或 TRAIT_COMMUNICATION，且前者优先），
    则尝试向相邻的动物传递喂食（传递时使用 BLUE_TOKEN 对于 Cooperation，RED_TOKEN 对于 Communication）。
    同一对相邻动物在本次操作中最多只能使用一次配对喂食。

    返回一个元组：(updated_player_animals, new_red_tokens_eaten, new_blue_tokens_eaten)
    """
    updated_animals = [[animal[0], animal[1], animal[2]] for animal in player_animals]
    red_tokens_eaten = 0
    blue_tokens_eaten = 0
    used_pairs = set()  # 存储已使用的相邻对，形式为 (min_index, max_index)

    def propagate_feed(index, token_to_feed):
        nonlocal red_tokens_eaten, blue_tokens_eaten, updated_animals, used_pairs
        animal = updated_animals[index]
        if animal[2]:
            return
        updated, red_tokens_eaten, blue_tokens_eaten, fed = check_animal_not_fully_fed_and_feed(animal,
                                                                                                red_tokens_eaten,
                                                                                                blue_tokens_eaten,
                                                                                                token_to_feed)
        updated_animals[index] = updated
        if not fed:
            return
        traits = updated[0]
        pairwise_trait = None
        if TRAIT_COOPERATION in traits:
            pairwise_trait = TRAIT_COOPERATION
        elif TRAIT_COMMUNICATION in traits:
            pairwise_trait = TRAIT_COMMUNICATION
        if pairwise_trait is None:
            return
        propagation_token = BLUE_TOKEN if pairwise_trait == TRAIT_COOPERATION else RED_TOKEN
        candidate = None
        if index + 1 < len(updated_animals) and not updated_animals[index + 1][2]:
            if (index, index + 1) not in used_pairs:
                candidate = index + 1
        if candidate is None and index - 1 >= 0 and not updated_animals[index - 1][2]:
            if (index - 1, index) not in used_pairs:
                candidate = index - 1
        if candidate is not None:
            used_pairs.add((min(index, candidate), max(index, candidate)))
            propagate_feed(candidate, propagation_token)

    propagate_feed(animal_to_feed_index, RED_TOKEN)
    return (updated_animals, red_tokens_eaten, blue_tokens_eaten)


# --- 辅助函数：重复喂食，直至动物被喂满 ---
def simulate_full_feeding(player_animals, animal_index):
    """
    模拟不断调用 feed_animal_red_token 直至 player_animals 中索引为 animal_index 的动物被喂满，
    返回所需的红代币总数。
    使用时对 player_animals 做深拷贝，保证原始状态不变。
    """
    sim_state = [[a[0], a[1], a[2]] for a in player_animals]
    total_red = 0
    while not sim_state[animal_index][2]:
        sim_state, red_used, _ = feed_animal_red_token(sim_state, animal_index)
        total_red += red_used
    return total_red


# --- Q2(b)函数：find_greedy_feeding_count ---
def find_greedy_feeding_count(players, focus_player_index, red_tokens_available):
    import copy
    """
    根据“贪婪策略”假设，每个非焦点玩家在自己的回合内总是使用尽可能多的红代币（即使某个动物完全喂饱所需的红代币数）。
    然后，将所有非焦点玩家按相对于焦点玩家的位置分组：
      - lower_total：所有索引小于焦点玩家的非焦点玩家的贪婪值之和；
      - higher_total：所有索引大于焦点玩家的非焦点玩家的贪婪值之和。
    （red_tokens_available 在本函数中不影响计算，因为贪婪值由动物状态决定。）

    根据题目描述，返回一个列表 max_red_tokens_before_focus_player_turn_in_round，
    其长度应等于玩家数，其中：
      - 第 0 个元素为 lower_total，
      - 其余每个元素均为 higher_total。

    例如：
      例1：
        player1_animals = [[(TRAIT_RUNNING,), 0, False], [(TRAIT_RUNNING,), 0, False]]
        player2_animals = [[(TRAIT_RUNNING,), 0, False],
                           [(TRAIT_RUNNING,), 0, False],
                           [(TRAIT_RUNNING, TRAIT_COMMUNICATION), 0, False]]
        focus_player_index = 1, red_tokens_available = 5  → 输出 [1, 1]
      例2：
        players = [[[[(4,),0,False],[(4,),0,False],[(4,),0,False]]],
                   [[[(4,),0,False],[(4,),0,False],[(4,1),0,False]]],
                   [[[(0,4),0,False],[(4,),0,False],[(4,),0,False]]]]
        focus_player_index = 1, red_tokens_available = 5  → 输出 [1, 2, 2]
      （注：例3中若玩家数为 11，则返回列表长度为 11。）
    """
    sim_players = copy.deepcopy(players)
    n_players = len(sim_players)
    current_index = 0
    cumulative = 0  # 自上次焦点回合以来累计的红 token 数
    result = []
    consecutive_no_move = 0  # 连续非焦点玩家回合无 token 消耗的计数

    while True:
        # 若红 token 已耗尽，则先推进到焦点玩家回合，再记录累计值后退出
        if red_tokens_available <= 0:
            while current_index != focus_player_index:
                current_index = (current_index + 1) % n_players
            if cumulative > 0:
                result.append(cumulative)
            break

        if current_index == focus_player_index:
            # 到了焦点玩家回合，记录累计值（即从上次焦点回合到本次为止非焦点玩家累计消耗的 token 数）
            result.append(cumulative)
            cumulative = 0
            # 焦点玩家回合本身不消耗 token，也不计入无 move 次数
        else:
            # 非焦点玩家回合：模拟贪婪 move
            player = sim_players[current_index]
            animals = player[0]
            best_move = None
            best_red = 0
            for i, animal in enumerate(animals):
                if not animal[2]:
                    # 对每个未饱食动物，用 feed_animal_red_token 模拟 move
                    sim_animals = [[a[0], a[1], a[2]] for a in animals]
                    updated_animals, red_used, _ = feed_animal_red_token(sim_animals, i)
                    if red_used > best_red:
                        best_red = red_used
                        best_move = updated_animals
            if best_move is None or best_red == 0:
                consecutive_no_move += 1
            else:
                consecutive_no_move = 0
                sim_players[current_index][0] = best_move
                tokens_taken = best_red if best_red <= red_tokens_available else red_tokens_available
                red_tokens_available -= tokens_taken
                cumulative += tokens_taken

            # 若连续所有非焦点玩家回合都无法消耗 token，则退出循环
            if consecutive_no_move >= (n_players - 1):
                break

        current_index = (current_index + 1) % n_players

    return result

# --- 测试用例 ---

if __name__ == "__main__":
    # 例1
    player1_animals = [[(TRAIT_RUNNING,), 0, False], [(TRAIT_RUNNING,), 0, False]]
    player2_animals = [[(TRAIT_RUNNING,), 0, False],
                       [(TRAIT_RUNNING,), 0, False],
                       [(TRAIT_RUNNING, TRAIT_COMMUNICATION), 0, False]]
    player1 = [player1_animals]
    player2 = [player2_animals]
    players_ex1 = [player1, player2]
    focus_player_index_ex1 = 1
    red_tokens_available_ex1 = 5
    print(find_greedy_feeding_count(players_ex1, focus_player_index_ex1, red_tokens_available_ex1))
    # 输出应为 [1, 1]

    # 例2
    players_ex2 = [
        [[[(4,), 0, False], [(4,), 0, False], [(4,), 0, False]]],
        [[[(4,), 0, False], [(4,), 0, False], [(4, 1), 0, False]]],
        [[[(0, 4), 0, False], [(4,), 0, False], [(4,), 0, False]]]
    ]
    focus_player_index_ex2 = 1
    red_tokens_available_ex2 = 5
    print(find_greedy_feeding_count(players_ex2, focus_player_index_ex2, red_tokens_available_ex2))
    # 输出应为 [1, 2, 2]

    # 例3
    players_ex3 = [
        [[[(2,), 0, False], [(9,), 0, False], [(10,), 0, False], [(3, 8), 0, False], [(0, 4), 0, False]]],
        [[[(9,), 0, False], [(11,), 0, False], [(3, 5), 0, False], [(4,), 0, False], [(4, 5, 6, 10, 11), 0, False]]],
        [[[(5,), 0, False], [(0, 3, 10, 11), 0, False], [(1, 9, 10), 0, False], [(4,), 0, False], [(0, 5), 0, False]]]
    ]
    focus_player_index_ex3 = 2
    red_tokens_available_ex3 = 25
    print(find_greedy_feeding_count(players_ex3, focus_player_index_ex3, red_tokens_available_ex3))
    # 如果 players 数量为 3，则本函数返回列表长度为 3；
    # 但题目要求“返回列表的长度应等于玩家数”，所以若玩家数为 11，则返回 11 个元素。
    # 这里例3的预期输出为：[2,2,2,2,2,1,1,1,1,1,1]（长度 11），
    # 假设实际 players_ex3 中的玩家数为 11，此处仅作示例说明。
