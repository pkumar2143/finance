# Calculators for finding the return of certain investments

# Suggestion: Keep track of multiple stocks and overall return.
def stockReturn():
    initial = float(input('Initial stock price: '))
    invest = float(input('How much did you invest?: '))
    final = float(input('Final stock price: '))
    while invest < 0:
        invest = float(input('You entered a negative value. How much did you invest?: '))

    pct_change = 1+((final - initial)/initial)
    fin_invest_worth = round(invest*pct_change, 2)
    ret = round(fin_invest_worth - invest, 2)
    if ret == 0:
        print('No change in your investment.')
    elif ret > 0:
        print('Your final investment is worth $', fin_invest_worth, ' and PROFIT is $', ret)
    else:
        print('Your final investment is worth $', fin_invest_worth, ' and LOSS is $', -ret)
    return

# Incorporate additional monthly payments
def investReturn():
    initial = float(input('Initial investment ($): '))
    ann_rate = float(input('Estimated annual rate of return: '))*0.01

    num_years = [1,2,5,7,10,12,15,20,25,30,35,40]
    for year in num_years:
        print('After ',year,'year(s), your return will be $',round(initial*(1+ann_rate)**year,2))
