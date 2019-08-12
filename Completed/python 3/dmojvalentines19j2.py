totalSub = input()

pink = 0

for color in range(int(totalSub)):
    colors = list(map(int, input().split()))
    if colors[0] >= 240 and colors[0] <= 255:
        if colors[1] >= 0 and colors[1] <= 200:
            if colors[2] >= 95 and colors[2] <= 220:
                pink += 1

print(pink)

#completed 8-11-19 (MM/DD/YY)