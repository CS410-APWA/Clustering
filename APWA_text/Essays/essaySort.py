import os

essays = open('essayGroups', 'r')
essayList = eval(essays.read())
for i in range(len(essayList)):
	print(i)
	for essay in essayList[i]:
		essay = '.' + essay[essay.rfind('\\'):]
		print(essay)
		print(essay[:2] + str(i) + essay[1:])
		os.rename(essay, (essay[:2] + str(i) + essay[1:]))