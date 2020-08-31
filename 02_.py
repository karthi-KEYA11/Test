#Function to find the average of cubes of all even numbers in a given range(lb, ub) inclusive
def even_3(lb,ub):
    sum=0
    count=0
    for i in range(lb,ub+1):
        if((i%2==0)and(i!=1)):
            cub=i*i*i
            sum=sum+cub
            count=count+1
    avg=sum/count
    return avg
lb1=input("Enter the lowerbound")
ub1=input("Enter the upperbound")
lb=int(lb1)
ub=int(ub1)
avg=even_3(lb,ub)
print(avg)
