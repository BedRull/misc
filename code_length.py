import random
import string

def count_origin_length(seq):
	origin_seq_length = 0
	for idx,let in enumerate(seq):
		if let.isalpha():
			i = idx + 1
			while i < len(seq) and not seq[i].isalpha():
				i += 1

			if i > idx + 1:
				origin_seq_length += int(seq[idx+1:i])
			else:
				origin_seq_length += 1

	print(origin_seq_length)

def gen_seq(letters):
	return "".join([i + str(random.randint(1000000, 2000000)) for i in letters])

count_origin_length(gen_seq(string.ascii_uppercase))
