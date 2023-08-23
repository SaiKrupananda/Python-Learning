import sys
print(sys.argv)

sum=0
for i in range(len(sys.argv)):
    if(i!=0):
        sum+=int(sys.argv[i])
print(sum)