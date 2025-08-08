print("HALF PYRAMID PATTERN OF STARS")
print("-----------------------------")
row=int(input("Enter number of rows:"))
#outer loop manage row
for i in range (row):
    #inner loop manage column
    for j in range(i+1):
        print("🍇", end="")
    print()