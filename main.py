import random

maratons = []
with open('maratons.txt', 'w') as f:
    for _ in range(365):
        maratons.append(str(random.choices([0,1], [0.3, 0.7])[0]))
    f.write(','.join(maratons))

with open('maratons.txt', 'r') as f:
    data = f.read().split(",")

skrej = data.count("1")

periods = 0
kolPer = 0

for i in data:
    if i == "0":
        periods += 1
    else:  # i == "1"
        if periods >= 4:
            kolPer += 1
        periods = 0

# Ja fails beidzas ar nullēm
if periods >= 4:
    kolPer += 1

print("Dienas kad Marta devas skriet:", skrej)
print("Periodi ar vismaz 4 dienam, kad Marta ne skreja:", kolPer)