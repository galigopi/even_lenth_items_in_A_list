a=["gopi","krishna","love","python","ilovemyindia"]
b_even=[]
c_odd=[]
index=1
for item in a:
    if len(item) % 2 == 0:
        b_even.append(item)
    else:
        c_odd.append(item)
    index+=1
print ("even lenth words",b_even)
print ("odd lenth words",c_odd)
