import io
import re

def get_score(str):
	score = 0
	for char in str:
		score += (ord(char) - 64)
	return score

def get_triangle_words(lst):
	triangle_words = []
	triangle_list = [(i*(i+1))/2 for i in range(1,10)]

	for word in lst:
		if get_score(word) in triangle_list:
			triangle_words.append(word)

	return triangle_words

if __name__ == '__main__':
	f = io.open('words.txt', 'r')
	content = f.read()
	word_list = re.findall(r'\w+', content)
	triangle_words = get_triangle_words(word_list)
	print len(triangle_words)