import random
maratons = []
f = open('maratons.txt', 'w')
for _ in range(365):
    maratons.append(str(random.choices([0,1], [0.3, 0.7])[0]))
f.write(','.join(maratons))
f.close()

f = open('maratons.txt', 'r')
data = f.read().split(",")
f.close()

skrej = data.count("1")
periods = 0
pause = 0

for diena in data:
    if diena == "0": pause += 1
    else:
        if pause >= 4:
            periods += 1
            pause = 0

if pause >= 4: periods += 1

print("Dienas kad Marta devas skriet:", skrej)
print("Periodi ar vismaz 4 dienam kad Marta ne skreja:", periods)