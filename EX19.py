print("%11s" %"1","%9s" %"2", "%9s" %"3")
print("%10s" %"x","%9s" %"x", "%9s" %"x")
print("\t-----------------------")
for i in range(1,6):
    for j in range(1,4):
        print("%10d" %(i**j), end="")
    print()
