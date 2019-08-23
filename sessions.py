import random

def gen_in(count):
	return [[random.randint(0, 2000), random.randint(0, 2000)] for i in range(count)]

def find_most_common(origin_list):
	sorted_list = sorted(origin_list)

	start = min(sorted_list, key=lambda t:t[0])[0]
	end = max(sorted_list, key=lambda t:t[1])[1]

	times_intersections = {}	
	for i in range(start, end + 1):
		for el in sorted_list:
			if i >= el[0] and i <= el[1]:
			# print(f'if {i} in {range(el[0], el[1])}')
				if i in times_intersections.keys():
					times_intersections[i] += 1
				else:
					times_intersections[i] = 1
			else:
				break

	print(max(times_intersections.keys(), key=(lambda k: times_intersections[k])))

find_most_common(gen_in(100000))
