if __name__ == '__main__':
    x=int(input())
    y=int(input())
    z=int(input())
    n=int(input())
    all=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                all.append([i,j,k])
    filtered=[perm for perm in all if sum(perm)!=n]   
    print(filtered)        