import random
maratons = []
f = open('maratons.txt', 'w')
for _ in range(365):
    maratons.append(str(random.choices([0,1], [0.3, 0.7])[0]))
f.write(','.join(maratons))
f.close()