def tree_height(N, h):
    highest_streak = 1 
    lowest_streak = 1
    streak_high = 1 
    streak_low = 1 
    for i in range(len(h) - 1):
        if h[i] < h[i + 1]:
            streak_high+= 1 
            if streak_high > highest_streak:
                highest_streak = streak_high

        elif h[i] > h[i + 1]:
            streak_high = 1

        if h[i] > h[i + 1]:
            streak_low += 1
            if streak_low > lowest_streak:
                lowest_streak = streak_low

        elif h[i] < h[i + 1]:
            streak_low = 1

    print(highest_streak, lowest_streak)
tree_height(10, [2, 1 ,4 , 6, 8 , 2, 9, 5, 2, 3])
tree_height(4, [1, 3, 4, 2])