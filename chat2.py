def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None
	nina_word_count = 0
	nina_sticker_count = 0
	anna_word_count = 0
	anna_sticker_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Nina':
			if s[2] == '貼圖':
				nina_sticker_count += 1
			else:
				for m in s[2:]:
					nina_word_count += len(m)
		elif name == 'ANNA':
			if s[2] == '貼圖':
				anna_sticker_count += 1
			else:
				for m in s[2:]:
					anna_word_count += len(m)
	print('Nina傳了', nina_word_count, '個字', nina_sticker_count, '個貼圖')
	print('Anna傳了', anna_word_count, '個字', anna_sticker_count, '個貼圖')
 
		#print(s)
	return new


def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]ANNA.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main() 