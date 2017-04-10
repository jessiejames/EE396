import random
import csv
from itertools import izip
labels = ["dogs", "cats"]
dogs = []
cats = []

k =0
while k < 10:
	i = random.randint(0, 50)
	dogs.append(i)
	i = random.randint(0, 50)
	cats.append(i)
	k=k +1

import csv
with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(labels)
    writer.writerows(izip(dogs, cats))
print i
