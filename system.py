import random

def sorteio(): # 
    num1 = random.randint(0000,9999)
    num2 = random.randint(0000,9999)
    num3 = random.randint(0000,9999)
    num4 = random.randint(0000,9999)
    num5 = random.randint(0000,9999)

    result1 = list(str(num1))
    result1 = int(result1[2]+result1[3])

    result2 = list(str(num2))
    result2 = int(result2[2]+result2[3])

    result3 = list(str(num3))
    result3 = int(result3[2]+result3[3])

    result4 = list(str(num4))
    result4 = int(result4[2]+result4[3])
    
    result5 = list(str(num5))
    result5 = int(result5[2]+result5[3])

    return num1, num2, num3, num4, num5, result1, result2, result3, result4, result5
    

print(sorteio())






