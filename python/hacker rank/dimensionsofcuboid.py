x = int(input())
y = int(input())
z = int(input())
n = int(input())

list = []    

for no in range(0,x+1):
    for nos in range(0,y+1):
        for ni in range(0,z+1):
            if (no + nos +ni) != n:
                list.append([no,nos,ni])

print(list)
