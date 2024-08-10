name1=input("enter the first name:")
height_m1=eval(input("enter the first height:"))
weight_kg1=eval(input("enter the first weight:"))

name2= input("enter the second name:")
height_m2=eval(input("enter the second height:"))
weight_kg2=eval(input("enter the second weight:"))

name3=input("enter the third name:")
height_m3=eval(input("enter the third height:"))
weight_kg3=eval(input("enter the third weight:"))

name4=input("enter the forth name:")
height_m4=eval(input("enter the forth height:"))
weight_kg4=eval(input("enter the forth weight:"))

def bmi_calculator(name, height_m,weight_kg):
     bmi = weight_kg/(height_m**2)
     print("bmi:")
     print(bmi)
     if bmi<25:
          return name + " is not over weight"
     else:
           return name + " is overweight"

result1=bmi_calculator(name1, height_m1,weight_kg1)
result2=bmi_calculator(name2, height_m2,weight_kg2)
result3=bmi_calculator(name3, height_m3,weight_kg3)
result4=bmi_calculator(name4, height_m4,weight_kg4)

print(result1)
print(result2)
print(result3)
print(result4)
