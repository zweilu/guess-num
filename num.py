#產生隨機整1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大小

import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # = count + 1
	num = input('請猜數字:')
	num = int(num)
	if num == r :
		print('猜對了!')
		print('這是你猜的第' , count, '次')
		break
	elif num > r :
		print('比答案大')
	elif num < r :
		print('比答案小')
	print('這是你猜的第' , count, '次')