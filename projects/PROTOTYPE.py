# calculating with Massachusetts tax for a restaurant
def calc_tax(amount):
    tax = amount * 0.07
    tax_bill = amount + tax
    return(tax_bill)

# adding tip into calculator
def calc_tip(tax_bill):
    tip = tax_bill * 0.20
    bill = tax_bill + tip
    return(bill)

# input amount and tip
amount = 20
tax_bill = calc_tax(amount)
final_bill = calc_tip(tax_bill)


print(f'Total bill: ${final_bill}')

