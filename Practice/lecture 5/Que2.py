# Grade as per marks obtained
m=int(input("Enter Your marks\n"))
if m>90 and m<=100:
    print("A-Grade")
elif m>80 and m<=90:
    print("B-Grade")
elif m>70 and m<=80:
    print("C-Grade")
elif m>60 and m<=70:
    print("D-Grade")
elif m>=50 and m<=60:
    print("E-Grade")
else:
    print("F-Grade")
    