def maximum_distance(s, t):
    max_distance = 0

    while t > 0:
        if t % 4 == 0:
            max_distance += (t // 4) * (2 * s + s + s + s)
            t = 0
        elif t % 4 == 1:
            max_distance += (t // 4) * (2 * s + s + s + s) + s
            t = 0
        elif t % 4 == 2:
            max_distance += (t // 4) * (2 * s + s + s + s) + 2 * s
            t = 0
        else:
            max_distance += (t // 4) * (2 * s + s + s + s) + 3 * s
            t = 0

        s -= 1

    return max_distance

s = int(input("Digite o valor de s (1 <= s < 1000): "))
t = int(input("Digite o valor de t (1 <= t < 1000): "))

result = maximum_distance(s, t)
print("A distância máxima é:", result)
