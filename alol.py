import copy

block = '''X1XXXX1XX1
XXXX1XX0XX
XX1XXXXXXX
XXXXXXXXXX
XX11XX0X1X
0XXXXXXXX0
X1XXXX0XXX
X1XXXXXXXX
XXXX11XXX1
0X1XX1X0XX'''

block = block.split("\n")
s = list(); blocks = list()
for b in block:
	for c in b:
		s.append(c)
	blocks.append(s)
	s = list()

org = copy.deepcopy(blocks)

width = len(blocks)

def reverse(i):
	if i == '1': return '0'
	if i == '0': return '1'
	if i == 'X': return 'X'

def total():
	c = 0
	for i in blocks:
		c += i.count('X')
	return c

def jia(loc):
	#被两个相同的夹在中间
	i = loc[0]; j = loc[1]
	if i in range(1, width - 1):
		if blocks[i-1][j] == blocks[i+1][j] != 'X': blocks[i][j] = reverse(blocks[i+1][j])
	if j in range(1, width - 1):
		if blocks[i][j-1] == blocks[i][j+1] != 'X': blocks[i][j] = reverse(blocks[i][j+1])

def lin(loc):
	#与两个相同的相邻
	i = loc[0]; j = loc[1]
	if i in range(2, width):
		if blocks[i-1][j] == blocks[i-2][j] != 'X': blocks[i][j] = reverse(blocks[i-1][j])
	if i in range(0, width - 2):
		if blocks[i+1][j] == blocks[i+2][j] != 'X': blocks[i][j] = reverse(blocks[i+1][j])
	if j in range(2, width):
		if blocks[i][j-1] == blocks[i][j-2] != 'X': blocks[i][j] = reverse(blocks[i][j-1])
	if j in range(0, width - 2):
		if blocks[i][j+1] == blocks[i][j+2] != 'X': blocks[i][j] = reverse(blocks[i][j+1])

def hlc():
	#行列个数
	revBlocks = list(map(list, zip(*blocks)))
	for i in range(width):
		hang = blocks[i]
		lie = revBlocks[i]
		if hang.count('0') == width / 2: 
			for h in range(width):
				if hang[h] == 'X': blocks[i][h] = '1'
		if hang.count('1') == width / 2: 
			for h in range(width):
				if hang[h] == 'X': blocks[i][h] = '0'
		if lie.count('0') == width / 2: 
			for h in range(width):
				if lie[h] == 'X': blocks[h][i] = '1'
		if lie.count('1') == width / 2: 
			for h in range(width):
				if lie[h] == 'X': blocks[h][i] = '0'

def bu():
	#必要补项
	revBlocks = list(map(list, zip(*blocks)))
	for i in range(width):
		hang = "".join(blocks[i])
		lie = "".join(revBlocks[i])
		if ('XX' in hang) and ('XXX' not in hang):
			for t in ('0', '1'):
				tr = reverse(t)
				if hang.count(t) == (width / 2 - 1) and hang.count(tr) == (width / 2 - 2):
					xxloc = list(); xloc = list()
					for m in range(width):
						if hang[m] == 'X': xloc.append(m)
					for m in range(width - 1):
						if hang[m] == hang[m+1] == 'X': xxloc.append(m); xxloc.append(m+1)
					single = [n for n in xloc if n not in xxloc][0]
					if (xxloc[0] < width - 2 and hang[xxloc[0]+2] == tr) or (xxloc[0] > 0 and hang[xxloc[0]-1] == tr):
						blocks[i][single] = tr
		if ('XX' in lie) and ('XXX' not in lie):
			for t in ('0', '1'):
				tr = reverse(t)
				if lie.count(t) == (width / 2 - 1) and lie.count(tr) == (width / 2 - 2):
					xxloc = list(); xloc = list()
					for m in range(width):
						if lie[m] == 'X': xloc.append(m)
					for m in range(width - 1):
						if lie[m] == lie[m+1] == 'X': xxloc.append(m); xxloc.append(m+1)
					single = [n for n in xloc if n not in xxloc][0]
					if (xxloc[0] < width - 2 and lie[xxloc[0]+2] == tr) or (xxloc[0] > 0 and lie[xxloc[0]-1] == tr):
						blocks[single][i] = tr
		if 'XXX' in hang:
			for t in ('0', '1'):
				tr = reverse(t)
				if hang.count(t) == (width / 2 - 1) and hang.count(tr) == (width / 2 - 2):
					xloc = 0
					for m in range(width - 2):
						if hang[m] == 'X' == hang[m+1] == hang[m+2]: xloc = m
					if xloc < width - 3 and hang[xloc+3] == tr:
						blocks[i][xloc] = tr
					if xloc > 0 and hang[xloc-1] == tr:
						blocks[i][xloc+2] = tr
		if 'XXX' in lie:
			for t in ('0', '1'):
				tr = reverse(t)
				if lie.count(t) == (width / 2 - 1) and lie.count(tr) == (width / 2 - 2):
					xloc = 0
					for m in range(width - 2):
						if lie[m] == 'X' == lie[m+1] == lie[m+2]: xloc = m
					if xloc < width - 3 and lie[xloc+3] == tr:
						blocks[xloc][i] = tr
					if xloc > 0 and hang[xloc-1] == tr:
						blocks[xloc+2][i] = tr

def printf():
	xcount = 0
	for i in range(width):
		for j in range(width):
			if blocks[i][j] == 'X': xcount += 1
			print('[' + str(blocks[i][j]) + '] ', end = '')
		print(blocks[i].count('0'),'\n')
	print("XCount: " + str(xcount))
	if(xcount == 0): 
		if chacuo() > 0:
			print("Impossible")
	return xcount

def huajian():
	while total() != 0:
		com = copy.deepcopy(blocks)
		for i in range(width):
			for j in range(width):
				if blocks[i][j] == 'X':
					jia((i,j))
		for i in range(width):
			for j in range(width):
				if blocks[i][j] == 'X':
					lin((i,j))
		hlc()
		bu()
		if blocks == com: break
	xcount = 0
	for i in range(width):
		for j in range(width):
			if blocks[i][j] == 'X': xcount += 1
	return str(xcount)

def chacuo():
	hang = list(); lie = list()
	revBlocks = list(map(list, zip(*blocks)))
	for h in blocks:
		hang.append("".join(h))
	for l in revBlocks:
		lie.append("".join(l))
	count = 0
	for i in range(width):
		if "000" in "".join(hang[i]): count = 1
		if "111" in "".join(hang[i]): count = 1
		if "000" in "".join(lie[i]): count = 1
		if "111" in "".join(lie[i]):  count = 1
		if ("X" not in hang[i]) and ("".join(hang[i]).count("0") != width / 2): count = 1
		if ("X" not in lie[i]) and ("".join(lie[i]).count("0") != width / 2): count = 1
		for j in range(width):
			if ("X" not in hang[i]) and (hang[i] == hang[j]) and i < j: count = 1
			if ("X" not in lie[i]) and (lie[i] == lie[j]) and i < j: count = 1
	return count

huajian()
printf()
org = copy.deepcopy(blocks)
tarcount = 0; loopcount = 1
while True:
	tar = list()
	for i in range(width):
		for j in range(width):
			if blocks[i][j] == 'X':
				tar.append((i,j))
	if tarcount == len(tar) or len(tar) == 0: break
	print("\nLoop " + str(loopcount))
	for t in tar:
		x = t[0]; y = t[1]
		blocks[x][y] = '0'
		xc = huajian(); im = False
		print("(" + str(x) + "," + str(y) + ") = 0: Xcount: " + xc, end = "")
		if chacuo() > 0: 
			print(" Impossible.", end = "")
			org[x][y] = '1'; im = True
		if im == False and xc == '0':
			org[x][y] = '0'
		blocks = copy.deepcopy(org)
		print()
	printf()
	tarcount = len(tar); loopcount += 1