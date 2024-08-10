LDL=eval(input("enter value of LDL:"))
HDL=eval(input("enter value of HDL:"))
TRI=eval(input("enter value of TRI:"))
total= LDL+HDL+ (TRI/5.0)
if (LDL<100) and (HDL>60) and (TRI,150) and (total<200):
    print ("you gucci fam")
elif (LDL>130) or (HDL<50) or (TRI>200) or (total>240):
    print ("take serious action against your cholesterol fam!")
else:
    print("almost everyone has these problems, homeslice")

