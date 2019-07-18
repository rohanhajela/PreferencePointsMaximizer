from itertools import combinations 
import sys
import math


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben



def leftoverPeople(used, total):
	leftover = []
	for i in range(total):
		if i not in used:
			leftover.append(i)
	return tuple(leftover)

def findScore(arrangement):
	curScore = 0
	for division in range(len(arrangement)):
		for person in arrangement[division]:
			#print(pts[person][division])
			curScore += pts[person][division]
	return curScore

#trial
#pts = [[30, 50, 20], [20, 20, 60], [35, 40, 25], [10, 40, 50], [10, 5, 85], [20, 50, 30], [35, 10, 55], [30, 40, 30]]
#grp_init = (0, 1, 2, 3, 4, 5, 6, 7)

#mockdata	1					2						3					4							5					6					7					8					9						10					11					12					13					14
pts = [[20, 40, 20, 5, 5], [10, 20, 30, 40, 0], [20, 50, 0, 10, 20], [20, 20, 10, 10, 40], [10, 25, 20, 35, 10], [20, 0, 0, 50, 30], [15, 10, 45, 10, 20], [10, 40, 10, 20, 20], [20, 20, 20, 30, 10], [10, 40, 40, 5, 5], [20, 30, 10, 20, 20], [0, 0, 30, 40, 30], [50, 10, 5, 30, 5], [20, 0, 20, 55, 5]]
grp_init = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
div1_size = 5
div2_size = 5
div3_size = 2
div4_size = 1
div5_size = 1

#smaller mockdata

# pts = [[20, 40, 20, 5, 5], [10, 20, 30, 40, 0], [20, 50, 0, 10, 20], [20, 20, 10, 10, 40], [10, 25, 20, 35, 10], [20, 0, 0, 50, 30], [15, 10, 45, 10, 20], [10, 40, 10, 20, 20], [20, 20, 20, 30, 10], [10, 40, 40, 5, 5]]
# grp_init = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# div1_size = 2
# div2_size = 2
# div3_size = 2
# div4_size = 3
# div5_size = 1


grpSize = len(grp_init)

arrangements = []

# TRIAL <>
# for grp1 in list(combinations(grp_init, 3)):

# 	leftover1 = (leftoverPeople(grp1, 8))
	
# 	for grp2 in list(combinations(list(leftover1), 3)):
# 		grp3 = (leftoverPeople(grp1 + grp2, 8))
# 		arrangements.append([grp1, grp2, grp3])
# TRIAL <>

# MOCK <>
count = 0
total = (math.factorial(grpSize) / (math.factorial(div1_size) * math.factorial(div2_size) * math.factorial(div3_size) * math.factorial(div4_size) * math.factorial(div5_size)))

for grp1 in list(combinations(grp_init, div1_size)):
	
	leftover1 = (leftoverPeople(grp1, grpSize))

	for grp2 in list(combinations(list(leftover1), div2_size)):

		leftover2 = leftoverPeople(grp1 + grp2, grpSize)

		for grp3 in list(combinations(list(leftover2), div3_size)):

			leftover3 = leftoverPeople(grp1 + grp2 + grp3, grpSize)

			for grp4 in list(combinations(list(leftover3), div4_size)):

				leftover4 = leftoverPeople(grp1 + grp2 + grp3 + grp4, grpSize)

				for grp5 in list(combinations(list(leftover4), div5_size)):
					# print([grp1, grp2, grp3, grp4, grp5])
					arrangements.append([grp1, grp2, grp3, grp4, grp5])
					count += 1;
					progress(count, total)
print()

# MOCK <>


best_arrangements = sorted(arrangements, key = findScore, reverse = True)
for i in range(10):
	print(best_arrangements[i], findScore(best_arrangements[i]))

