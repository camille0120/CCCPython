a=input("Height(cm)?")
b=input("Weight(kg)?")
c=int(b)/((int(a)/100)**2)
if(c<=18.5):
    print("Underweight")
elif c>24:
    print("Overweight")
else:
    print("Normal")