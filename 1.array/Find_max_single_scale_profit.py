# not familiar 
import sys
def find_buy_sell_stock_prices(array):
    ibuy = 0
    glo_prof = -(2**30)
    cur_buy = array[ibuy]
    go_sell = -sys.maxint-1
    i=1
    
    while i < len(array): 
        cur_prof = array[i] - cur_buy # current buy and profit are just temporary value
        if cur_prof > glo_prof: 
            glo_prof = cur_prof   # output global profit and sell
            go_sell = i
        if cur_buy > array[i]:
            ibuy = i
            cur_buy = array[ibuy]
        i = i+1
    return array[go_sell] - glo_prof,array[go_sell]

def main():
    a = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,15,15]
    b = [8,5,12,9,19,1]
    key = 6
    qql = find_buy_sell_stock_prices(b)
    print(qql)
    #print('low %d, high %d' % (qql,qqh))


if __name__ == "__main__":
    main()