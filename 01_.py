#Function to print all numbers divisible by 6 and not a factor of 100 in a given range(lb, ub) inclusive
def fun_6(lb,ub):
    for i in range(lb,ub+1):
        if ((i%6==0)and(i%100!=0)):
            print(i)
lb1=input("Enter the lowerbond")
ub1=input("Enter the upperbond")
lb=int(lb1)
ub=int(ub1)
fun_6(lb,ub)
