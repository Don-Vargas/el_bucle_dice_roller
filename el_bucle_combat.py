import random

def roll_dice():
    """Roll a six-sided die."""
    return random.randint(1, 6)

def apply_low_life_penalty(character):
    """Apply penalty if life_points == 1."""
    if character["life_points"] == 1:
        character["body_points"] = max(0, character["body_points"] - 1)
        character["mind_points"] = max(0, character["mind_points"] - 1)

def calculate_combat_score(
    match_type,
    body_points,
    mind_points,
    hand_weapon_points=0,
    long_distance_weapon_points=0,
    use_hand_weapon=False,
    use_long_distance_weapon=False
):
    roll = roll_dice()

    if match_type == "hand_to_hand":
        score = roll + body_points
        if use_hand_weapon:
            score += hand_weapon_points

    elif match_type == "gun_fight":
        score = roll + mind_points
        if use_long_distance_weapon:
            score += long_distance_weapon_points

    else:
        raise ValueError("Invalid match type")

    return score, roll

def fight(match_type, me, opponent):
    # Apply life-point penalty before the fight
    apply_low_life_penalty(me)
    apply_low_life_penalty(opponent)

    # Step 1: My roll
    my_score, my_roll = calculate_combat_score(
        match_type,
        body_points=me["body_points"],
        mind_points=me["mind_points"],
        hand_weapon_points=me["hand_weapon_points"],
        long_distance_weapon_points=me["long_distance_weapon_points"],
        use_hand_weapon=me["use_hand_weapon"],
        use_long_distance_weapon=me["use_long_distance_weapon"],
    )



    # Step 2: Opponent roll
    opp_score, opp_roll = calculate_combat_score(
        match_type,
        body_points=opponent["body_points"],
        mind_points=opponent["mind_points"],
        hand_weapon_points=opponent["hand_weapon_points"],
        long_distance_weapon_points=opponent["long_distance_weapon_points"],
        use_hand_weapon=opponent["use_hand_weapon"],
        use_long_distance_weapon=opponent["use_long_distance_weapon"],
    )
    

    # Display results
    print(f"My roll: {my_roll} → total score: {my_score}")
    print(f"Opponent roll: {opp_roll} → total score: {opp_score}")

    # Step 3: Compare results
    if my_score > opp_score:
        opponent["life_points"] -= 1
        print("I win the match! Opponent loses 1 life point.")

    elif opp_score > my_score:
        me["life_points"] -= 1
        print("Opponent wins the match! I lose 1 life point.")

    else:
        print("It's a tie! No life points lost.")

    return me, opponent

# -----------------------------
# Example Usage
# -----------------------------

me = {
    "life_points": 1,
    "body_points": 3,
    "mind_points": 4,
    "hand_weapon_points": 1,
    "long_distance_weapon_points": 0,
    "use_hand_weapon": True,
    "use_long_distance_weapon": False
}

opponent_1 = {
    "life_points": 2,
    "body_points": 4,
    "mind_points": 0,
    "hand_weapon_points": 1,
    "long_distance_weapon_points": 0,
    "use_hand_weapon": True,
    "use_long_distance_weapon": False
}

opponent_2 = {
    "life_points": 0,
    "body_points": 2,
    "mind_points": 0,
    "hand_weapon_points": 1,
    "long_distance_weapon_points": 0,
    "use_hand_weapon": True,
    "use_long_distance_weapon": False
}
opponent = opponent_1
# hand_to_hand or gun_fight
fight("hand_to_hand", me, opponent)\

print("\nLife points after fight:")
print("Me:", me["life_points"])
print("Opponent:", opponent["life_points"])
