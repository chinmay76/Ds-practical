list1 = [12,3,4,55,65,66,45,22,98]
size = len(list1)
def searching(n):
	print("SEARCHING")
	print(list1)
	if n not in list1:
		print(n,"not in the list")
	else:
		for i in range(size):
			if list1[i]==n:
				print("index of ", n," is ",i)

def sorting():
	print("SORTING")
	print(list1)
	for i in range(len(list1)):
		for j in range(i):
			if list1[i] < list1[j]:
				list1[i], list1[j] = list1[j], list1[i]
	print("sorted = ",list1)

def merging():
	print("MERGING")
	list2 = [6,3,45,23,56,67,77,65]
	print("list1 = ",list1)
	print("list2 = ",list2)
	merge = list1+list2
	print("merged list = ",merge)
	
def revrse():
	print("REVERSED")
	print(list1)
	size = len(list1)-1
	i = 0
	while size >0:
		list1[i], list1[size] = list1[size], list1[i]
		size -= 1
		i += 1
		if size<=i:
			break
	print(list1)

searching(57)
sorting()
merging()
revrse()
