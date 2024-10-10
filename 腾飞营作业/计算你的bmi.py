height = float(input('请输入你的身高（米）：'))
weight = float(input('请输入你的体重（千克）：'))



def calculate_your_bmi(your_height, your_weight):
    bmi = your_weight / (your_height ** 2)
    if bmi < 18.5:
        print('你的BMI指数为:', bmi, '过轻')
    elif  18.5 <= bmi < 24: 
        print('你的BMI指数为:', bmi, '正常')
    elif 24 <= bmi < 28:
        print('你的BMI指数为:', bmi, '超重')
    elif 28 <= bmi < 32:
        print('你的BMI指数为:', bmi, '肥胖')
    

calculate_your_bmi(height, weight)

