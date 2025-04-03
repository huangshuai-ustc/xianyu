import copy

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


# --- 辅助函数 ---

def calculate_animal_food_requirements(animal):
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


def count_animal_victory_points(animal):
    if not animal[2]:
        return 0
    traits = animal[0]
    base = 2
    trait_pts = len(traits)
    if TRAIT_HIBERNATION in traits:
        extra = 0
    else:
        total_required = 1
        if TRAIT_CARNIVORE in traits:
            total_required += 1
        if TRAIT_HIGH_BODY_WEIGHT in traits:
            total_required += 1
        if TRAIT_PARASITE in traits:
            total_required += 2
        extra = total_required - 1
    return base + trait_pts + extra


def check_animal_not_fully_fed_and_feed(animal, red_tokens_eaten_count, blue_tokens_eaten_count, token_to_feed):
    updated_animal = [animal[0], animal[1], animal[2]]
    if updated_animal[2]:
        return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, False)
    updated_animal[1] += 1
    if token_to_feed == RED_TOKEN:
        red_tokens_eaten_count += 1
    elif token_to_feed == BLUE_TOKEN:
        blue_tokens_eaten_count += 1
    if calculate_animal_food_requirements(updated_animal) == 0:
        updated_animal[2] = True
    return (updated_animal, red_tokens_eaten_count, blue_tokens_eaten_count, True)


def feed_animal_red_token(player_animals, animal_to_feed_index):
    updated_animals = [[a[0], a[1], a[2]] for a in player_animals]
    red_tokens_eaten = 0
    blue_tokens_eaten = 0
    used_pairs = set()

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
            pair = (min(index, candidate), max(index, candidate))
            used_pairs.add(pair)
            propagate_feed(candidate, propagation_token)

    propagate_feed(animal_to_feed_index, RED_TOKEN)
    return (updated_animals, red_tokens_eaten, blue_tokens_eaten)


def can_predator_attack_prey(predator, prey):
    predator_traits = predator[0]
    prey_traits = prey[0]
    if TRAIT_CARNIVORE not in predator_traits:
        return False
    if predator[2]:
        return False
    if TRAIT_HIBERNATION in prey_traits:
        return False
    if TRAIT_POISONOUS in prey_traits:
        return False
    if TRAIT_CAMOUFLAGE in prey_traits and TRAIT_SHARP_VISION not in predator_traits:
        return False
    if TRAIT_RUNNING in prey_traits and TRAIT_RUNNING not in predator_traits:
        return False
    if TRAIT_HIGH_BODY_WEIGHT in prey_traits and TRAIT_HIGH_BODY_WEIGHT not in predator_traits:
        return False
    if (TRAIT_SWIMMING in predator_traits or TRAIT_SWIMMING in prey_traits) and not (
            TRAIT_SWIMMING in predator_traits and TRAIT_SWIMMING in prey_traits):
        return False
    if TRAIT_BURROWING in prey_traits and prey[2]:
        return False
    return True


def create_attack_map(players):
    animal_can_attack = {}
    animal_attacked_by = {}
    for p, player in enumerate(players):
        animals = player[0]
        for a, animal in enumerate(animals):
            key = (p, a)
            animal_can_attack[key] = []
            animal_attacked_by[key] = []
    for p, player in enumerate(players):
        animals_p = player[0]
        for a, predator in enumerate(animals_p):
            attacker_key = (p, a)
            for q, other_player in enumerate(players):
                if q == p:
                    continue
                animals_q = other_player[0]
                for b, prey in enumerate(animals_q):
                    prey_key = (q, b)
                    if can_predator_attack_prey(predator, prey):
                        animal_can_attack[attacker_key].append(prey_key)
                        animal_attacked_by[prey_key].append(attacker_key)
    return (animal_can_attack, animal_attacked_by)


def calculate_food_crisis_survival_chance(players, player_index, animal_index, animal_can_attack, animal_attacked_by):
    animal = players[player_index][0][animal_index]
    if animal[2]:
        return 1.0
    if TRAIT_CARNIVORE not in animal[0]:
        return 0.0
    r = calculate_animal_food_requirements(animal)
    required_attacks = (r + 1) // 2
    required_prey = required_attacks * 2
    prey_list = animal_can_attack.get((player_index, animal_index), [])
    num_prey = len(prey_list)
    feeding_chance = 1.0 if num_prey >= required_prey else num_prey / float(required_prey)
    attackers = animal_attacked_by.get((player_index, animal_index), [])
    survival_multiplier = 1.0
    for attacker in attackers:
        attacker_prey = animal_can_attack.get(attacker, [])
        n = len(attacker_prey)
        if n > 0:
            not_attacked_prob = 0.5 + 0.5 * ((n - 1) / float(n))
        else:
            not_attacked_prob = 1.0
        survival_multiplier *= not_attacked_prob
    return feeding_chance * survival_multiplier


# --- 主函数 simulate_optimal_feeding_phase_gameplay ---
def simulate_attacks(final_players):
    """
    模拟攻击阶段：
    对于每个玩家中所有拥有 TRAIT_CARNIVORE 且未饱食的动物（认为它们需要更多食物），依次进行攻击，
    攻击目标为对手中得分（使用 count_animal_victory_points 计算）最低的动物。
    一次攻击中：
      - 攻击者：标记为饱食（此处仅更新 is_fully_fed 为 True）
      - 被攻击者：视为死亡，从所属玩家的动物列表中移除
    为避免列表移除导致索引混乱，我们先将被攻击目标置为 None，最后清除 None 值。
    返回更新后的 final_players 状态（其中已删除死亡动物）。
    """
    n_players = len(final_players)
    new_players = []
    # 复制每个玩家的动物列表
    for p in range(n_players):
        new_players.append(copy.deepcopy(final_players[p][0]))

    # 遍历每个玩家的动物（按玩家顺序、动物顺序）
    for p in range(n_players):
        for idx in range(len(new_players[p])):
            animal = new_players[p][idx]
            # 如果当前动物已经被标记为 None，跳过
            if animal is None:
                continue
            # 检查动物是否拥有食肉属性且未饱食
            if (animal[0] is not None and TRAIT_CARNIVORE in animal[0] and not animal[2]):
                # 收集所有对手的动物（排除己方）
                candidate_list = []
                for q in range(n_players):
                    if q == p:
                        continue
                    for j, opp_animal in enumerate(new_players[q]):
                        if opp_animal is None:
                            continue
                        candidate_list.append((q, j, count_animal_victory_points(opp_animal)))
                if not candidate_list:
                    continue
                # 按候选动物得分从低到高排序，选择得分最低的动物
                candidate_list.sort(key=lambda x: x[2])
                target_player, target_idx, _ = candidate_list[0]
                # 攻击成功：攻击者标记为饱食
                new_players[p][idx][2] = True
                # 被攻击者标记为死亡（用 None 表示）
                new_players[target_player][target_idx] = None

    # 清除每个玩家列表中被标记为 None 的动物
    for p in range(n_players):
        new_players[p] = [animal for animal in new_players[p] if animal is not None]

    # 封装回 players 格式（这里只更新动物列表）
    final_state = []
    for p in range(n_players):
        final_state.append([new_players[p]])
    return final_state


# --- 递归搜索，确定焦点玩家最佳 feeding choices ---
def simulate_optimal_feeding_phase_gameplay(players, focus_player_index, red_tokens_available):
    """
    模拟 feeding 阶段，搜索焦点玩家的最佳喂食决策序列（best_turns），使得经过 feeding 和后续攻击后，
    焦点玩家能获得最优结果（这里采用最终存活动物的总胜利点之和作为评价指标）。

    返回值为一个元组：(best_turns, final_state)
      - best_turns 为焦点玩家各回合选择喂食的动物索引序列（tie-break时选索引较小者）
      - final_state 为模拟结束后所有玩家的动物状态（已去除死亡动物）

    非焦点玩家采用贪婪策略，其动物状态保持为初始状态。
    焦点玩家在其回合时分支尝试所有可行 move（喂食未饱食的动物）。
    """
    n_players = len(players)
    # 记录非焦点玩家初始状态（深拷贝），保持不变
    initial_players = copy.deepcopy(players)
    focus_initial = copy.deepcopy(players[focus_player_index][0])

    # 递归搜索函数
    def search(red, current, focus_state, moves):
        """
        red: 剩余红 token 数
        current: 当前轮到的玩家索引
        focus_state: 当前焦点玩家动物状态（列表）
        moves: 焦点玩家至今作出的喂食决策（列表，每个元素为动物索引）

        当红 token 耗尽或无可行 move 时，执行后续攻击模拟，计算焦点玩家的总胜利点，
        作为评分（评价指标）。返回 (score, moves, final_state)
        """
        # 终止条件：红 token 耗尽
        if red <= 0:
            # 构造最终状态：非焦点玩家保持初始状态，焦点玩家使用 focus_state
            final_players = []
            for i in range(n_players):
                if i == focus_player_index:
                    final_players.append([focus_state])
                else:
                    final_players.append(copy.deepcopy(initial_players[i]))
            # 先模拟攻击阶段
            attacked_state = simulate_attacks(final_players)
            # 计算焦点玩家得分：取所有存活动物胜利点之和（count_animal_victory_points），也可取平均
            total = 0.0
            for animal in attacked_state[focus_player_index][0]:
                total += count_animal_victory_points(animal)
            score = total  # 此处评价指标为总分
            return score, moves, attacked_state

        # 如果当前不是焦点玩家，则采用贪婪策略（非焦点玩家状态不变）
        if current != focus_player_index:
            # 对当前非焦点玩家，尝试所有未饱食动物，选择能获得最多红 token 的 move
            player = initial_players[current]
            animals = player[0]
            best_red = 0
            for i, animal in enumerate(animals):
                if not animal[2]:
                    sim_animals = [[a[0], a[1], a[2]] for a in animals]
                    _, red_used, _ = feed_animal_red_token(sim_animals, i)
                    if red_used > best_red:
                        best_red = red_used
            tokens = best_red
            if tokens > red:
                tokens = red
            new_red = red - tokens
            next_player = (current + 1) % n_players
            return search(new_red, next_player, focus_state, moves)
        else:
            # 当前为焦点玩家回合：分支尝试所有可行的喂食 move
            best_score = -1.0
            best_seq = None
            best_state = None
            move_possible = False
            for i, animal in enumerate(focus_state):
                if not animal[2]:
                    move_possible = True
                    sim_focus = [[a[0], a[1], a[2]] for a in focus_state]
                    new_focus_state, red_used, _ = feed_animal_red_token(sim_focus, i)
                    if red_used > 0 and red_used <= red:
                        new_red = red - red_used
                        next_player = (current + 1) % n_players
                        score, seq, state = search(new_red, next_player, new_focus_state, moves + [i])
                        # tie-break: 相同时选择本回合喂食索引较小的
                        if score > best_score or (
                                score == best_score and seq is not None and best_seq is not None and seq < best_seq):
                            best_score = score
                            best_seq = seq
                            best_state = state
            # 如果焦点玩家没有可行 move，则视为 pass（直接进入下一回合，状态不变）
            if not move_possible:
                next_player = (current + 1) % n_players
                return search(red, next_player, focus_state, moves)
            return best_score, best_seq, best_state

    final_score, best_turns, final_state = search(red_tokens_available, 0, focus_initial, [])
    # 我们只返回 best_turns 与最终状态（去除死亡动物的状态已经在 simulate_attacks 中完成）
    return best_turns, final_state

# --- 示例测试 ---

if __name__ == "__main__":
    # 示例1
    player1_animals = [[(TRAIT_RUNNING,), 0, False], [(TRAIT_RUNNING,), 0, False]]
    player2_animals = [[(TRAIT_RUNNING, TRAIT_COMMUNICATION), 0, False], [(TRAIT_RUNNING,), 0, False]]
    player1 = [player1_animals]
    player2 = [player2_animals]
    players = [player1, player2]
    focus_player_index = 1
    red_tokens_available = 4
    best_turns, final_state = simulate_optimal_feeding_phase_gameplay(players, focus_player_index, red_tokens_available)
    point = 0
    for player in final_state:
        for animal in player[0]:
            print(count_animal_victory_points(animal))
            point += count_animal_victory_points(animal)
    print(point)
    # 预期输出：(7.0, [0])

    # 示例2
    player1_animals = [[(TRAIT_RUNNING, TRAIT_CARNIVORE), 0, False], [(TRAIT_RUNNING,), 0, False]]
    player2_animals = [[(TRAIT_RUNNING,), 0, False], [(TRAIT_RUNNING,), 0, False]]
    player1 = [player1_animals]
    player2 = [player2_animals]
    players = [player1, player2]
    focus_player_index = 1
    red_tokens_available = 4
    print(simulate_optimal_feeding_phase_gameplay(players, focus_player_index, red_tokens_available))
    # 预期输出：(4.5, [0, 1])

    # 示例3
    player1_animals = [[(4, 0), 0, False], [(4,), 0, False]]
    player2_animals = [[(4,), 0, False], [(4,), 0, False]]
    player3_animals = [[(0, 1), 0, False], [(4, 1), 0, False], [(4, 5), 0, False], [(9, 8), 0, False]]
    player1 = [player1_animals]
    player2 = [player2_animals]
    player3 = [player3_animals]
    players = [player1, player2, player3]
    focus_player_index = 2
    red_tokens_available = 15
    print(simulate_optimal_feeding_phase_gameplay(players, focus_player_index, red_tokens_available))
    # 预期输出：(16.875, [0, 0, 2, 3])
