# Calculate the return (profit/loss) of an investment in a stock.
import math as m

def investReturn():
    initial = float(input('Initial stock price: '))
    invest  = float(input('How much did you invest?: '))
    final   = float(input('Final stock price: '))

    chnge = 1+((final - initial)/initial)
    fin_invest_worth = round(invest*chnge,2)
    ret = round(fin_invest_worth - invest,2)
    if ret == 0:
        print('No change in your investment.')
    elif ret > 0:
        print('Your final investment is worth $',fin_invest_worth,' and PROFIT is $',ret)
    else:
        print('Your final investment is worth $',fin_invest_worth,' and LOSS is $',-ret)
    return

print(investReturn())