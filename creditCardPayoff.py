# Compute how long it will take to payoff credit card debt
# Compute the monthly payment in order to pay off a credit card within a certain time



def payoffTime():
    cc_balance = float(input('Enter your credit card balance ($): '))
    apr = float(input('Enter your credit card APR (%): '))*0.01
    mon_pmt = float(input('Monthly payments ($): '))

    n = [31, 28, 31, 30, 31, 30, 30, 31, 30, 31, 30, 31]
    #n = [31, 30, 31]*4
    i = 0
    mon_count = 0
    interest = 0
    while cc_balance > 0:
        mon_count += 1                                  # Counting months/payments
        cur_int = cc_balance*(apr)/365*n[i]             # Interest for current month
        interest += cur_int                             # Accumulating interest
        new_balance = round(cur_int + cc_balance, 2)    # Balance + interest
        if new_balance < mon_pmt:
            mon_pmt = new_balance                       # Last month's balance
        cc_balance = new_balance - mon_pmt              # Subtract monthly payment
        i = (i + 1) % 12
        #print('Month ', mon_count, ' new balance =', new_balance)

    print('Full payoff in ',mon_count,' months.',' Total interest paid = ', round(interest,2))
