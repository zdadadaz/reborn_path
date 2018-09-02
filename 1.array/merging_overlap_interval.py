from collections import namedtuple
## ask whether == is in the same interval
def find_busy_intervals(v1):
    out =[]
    out.append(v1[0])
    for i in xrange(1,len(v1)):
        tmp = v1[i]
        pt = len(out)-1  ## point to end
        if(out[pt][0]<tmp[0] and  tmp[0] < out[pt][1]):
            if out[pt][1] < tmp[1]:
                tmp = (out[pt][0],tmp[1])
                out[pt] = tmp
                
        elif(out[pt][0]<tmp[1] and  tmp[1] < out[pt][1]):
            if out[pt][0] > tmp[0]:
                tmp = (tmp[0],out[pt][1])
                out[pt] = tmp
        else:
            out.append(tmp)
    return out


def main():
    a = [(2,10), (4,12), (13,16), (19,20), (20,24)]
    qq = find_busy_intervals(a)
    print(qq)

if __name__ == "__main__":
    main()