def get_score(bananas, apples, has_poison_apple,cherries):
    """Returns a player's total score based on their cards of each type."""
    banana_score = get_banana_score(bananas)
    apple_score = get_apple_score(apples, has_poison_apple)
    cherry_score = get_cherry_score(cherries)
    total = banana_score + apple_score + cherry_score
    return total

def get_banana_score(num_bananas):
    """Returns a player's score based on the number of banana cards."""
    # Bananas are worth more in bunches.
    if num_bananas == 1:
        return 1
    elif num_bananas == 2:
        return 4
    elif num_bananas >= 3:
        return 10
    else:
        return 0

def get_apple_score(num_apples, has_poison_apple):
    """Returns a player's score based on the number of apple cards."""
    if has_poison_apple is True:
        return num_apples * -2
    else:
        return num_apples * 2

def get_cherry_score(num_cherry):
    """Returns a player's score based on the number of cherry cards."""
    num_cherry_pairs = num_cherry // 2
    return num_cherry_pairs * 5 

# Calculate the final score for each player.
player1_score = get_score(3, 2, True , 3)
player2_score = get_score(1, 5, False, 4)
print("Scores: p1=" + str(player1_score) + ", p2=" + str(player2_score))
