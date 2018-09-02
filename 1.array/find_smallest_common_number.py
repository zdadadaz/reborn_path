def find_least_common_number(v1,v2,v3):
    p1 = 0
    p2 = 0
    p3 = 0
    # condition should be more general
    #while p1 < len(v1) and p2 < len(v2) and p3 < len(v3)
    while v1[p1] != v2[p2] or v1[p1] != v3[p3] or v2[p2] != v3[p3]:
        if v1[p1] < v2[p2] and v1[p1] < v3[p3]:
            p1 = p1+1
        elif v2[p2] < v1[p1] and v2[p2] < v3[p3]:
            p2 = p2 +1
        elif v3[p3] < v1[p1] and v3[p3] < v2[p2]:
            p3 = p3 +1
    if v1[p1] == v2[p2] and v2[p2] == v3[p3]:
        return v1[p1]
    else:
        return -1
def main():
    v1 = [1,6,10,14,50]
    v2 = [-1,6,7,8,50]
    v3 = [0,6,7,10,25,30,50]
    qq = find_least_common_number(v1,v2,v3)
    print(qq)

if __name__ == "__main__":
    main()