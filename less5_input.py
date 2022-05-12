hight = input('請輸入你的身高: ')
weight = input('請輸入你的體重: ')
hight = float(hight)
weight = float(weight)
bmi = weight / ((hight / 100) * (hight / 100))
if bmi < 18.5 :
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24 :
    print('正常範圍')
elif bmi >= 24 and bmi < 27 :
    print('過重')
elif bmi >= 27 and bmi < 30 :
    print('輕度肥胖')
elif bmi >= 30 and bmi < 35 :
    print('中度肥胖')  
else:
    print('重度肥胖')  