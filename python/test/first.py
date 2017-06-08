n = 10
sum = 0
count = 0

while count<n:
	num = float(input())
	sum += num
	count = count +1
	
average = sum / n
print("N={}, sum={}".format(n,sum))
print("average is : {:.2f}".format(average))