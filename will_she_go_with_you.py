import math
import pandas as pd
import numpy as np
import random

# my playground of simple implementation of decision tree classifier

def entropy(all_values, elem=None):
	lenght = len(all_values)

	if elem is not None:
		prob = all_values.count(elem) / lenght
		return -prob * math.log(prob, 2) if prob else 0

	unique = set(all_values)
	if len(unique) == lenght:
		return 0
	
	probabilities = {i : all_values.count(i) / lenght for i in unique}

	res = 0
	for k, v in probabilities.items():
		res -= v * math.log(v,2)

	return res


def get_subset(full_set, filter_set, attribute):
	return [full_set[idx] for idx, i in enumerate(filter_set) if i == attribute]


queue_of_answers = list()

def find_best_gain(target, dict_param):
	length = len(target)
	En_X = entropy(target)

	if En_X == 0:
		queue_of_answers.append(tuple((target[0], 'she_will' if target[0] else 'she_will_not')))
		return
	
	gain = 0
	gain_key = 0

	for key, attribute in dict_param.items():				# loop through list of lists
		entropies = []
		for a in set(attribute):
			# put target results of that category(0 or 1) of current attribute(hair or eyes) to another list
			sub_target = [target[idx] for idx, i in enumerate(attribute) if i == a]

			# count all entropies for every category
			entropies.append(len(sub_target) * entropy(sub_target) / length)

		# find best gain
		if En_X - sum(entropies) > gain:
			gain = En_X - sum(entropies)
			gain_key = key


	if not gain_key:
		queue_of_answers.append(tuple((target[0], 'she_will' if target[0] else 'she_will_not')))
		return

	# pop it from dictionary
	feature_with_best_gain = dict_param.pop(gain_key, None)

	for a in set(feature_with_best_gain):
		# push in tree
		queue_of_answers.append(tuple((gain_key, a)))

		# split target and train set
		sub_target = get_subset(target, feature_with_best_gain, a)
		sub_params = {k : get_subset(dict_param[k], feature_with_best_gain, a) for k in dict_param.keys()}
		
		# recursively find best gain
		find_best_gain(sub_target, sub_params)

	return


def will_she(params):
	current_level = 0
	queue_length = len(queue_of_answers)

	while current_level <= queue_length:
		# increment while parameteres match
		while params[queue_of_answers[current_level][0]] == queue_of_answers[current_level][1]:
			current_level += 1

			# print result if we have faced it
			if queue_of_answers[current_level][0] in [0, 1]:
				return queue_of_answers[current_level][1]

		# find next index of current parameter in tree
		idx_next = current_level + 1
		while idx_next < queue_length:
			if queue_of_answers[idx_next][0] == queue_of_answers[current_level][0]:
				current_level = idx_next
				break
			else:
				idx_next += 1

		if queue_of_answers[current_level][0] in [0, 1]:
				return queue_of_answers[current_level][1]


def transform(array, future_zero):
	return [0 if i == future_zero else 1 for i in array]

# train set
train = {}
train['Appearance'] = ['nice', 'nice', 'nice', 'ugly', 'ugly', 'ugly', 'nice'] 
train['Alchohol'] = ['yes', 'yes', 'nope', 'nope', 'yes', 'yes', 'yes']
train['Oratory'] = ['high', 'low', 'high', 'high', 'low', 'high', 'high']
train['Money_spent'] = ['a lot', 'little', 'a lot', 'little', 'a lot', 'a lot', 'a lot']
target = transform(['+', '-', '+', '-', '-', '+', '+'], '-')

# build tree
find_best_gain(target, train)

# predict
print(will_she({'Appearance' : 'nice', 'Alchohol' : 'yes', 'Oratory' : 'high', 'Money_spent' : 'little'}))