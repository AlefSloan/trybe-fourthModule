def longest_name(arr):
    winner_name = ''
    for n in arr:
        if len(n) > len(winner_name):
            winner_name = n
    return winner_name


print(longest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
