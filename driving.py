country = input('請問你是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
# 5-9行(大的if) 6-9行(小的if)=>要先進入大的/才能進入小的
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')