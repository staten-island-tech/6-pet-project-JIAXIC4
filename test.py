def tree_height(N, h):
    highest_streak = 0 
    lowest_streak = 0
    streak_high = 0 
    streak_low = 0 
    for i in range(h):
        if i in range(h):
            if h[i] > h[i] + 1:
                streak_high+= 1 
                h[i] = h[i] + 1
                if streak_high > highest_streak:
                    highest_streak = streak_high

            if h[i] < h[i] + 1:
                streak_high = 0
                h[i] = h[i] + 1

            elif h[i] > h[i] + 1:
                streak_low += 1
                h[i] = h[i] +1
                if streak_low > lowest_streak:
                    lowest_streak = streak_low

            if h[i] > h[i] + 1:
                streak_high = 0
                h[i] = h[i] + 1

tree_height(5, [3, 2, 5, 4, 1])