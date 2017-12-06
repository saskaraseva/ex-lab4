#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = ['a', 'A', 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2

kuku = Unique
for i in kuku(data1, ignore_case=True):
	print(i)