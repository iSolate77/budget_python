from sys import argv
import re
import csv

date = []
creditcard = 0.0
fuel = 0.0
rent = 0.0
car = 0.0
coffee = 0.0
cash = 0.0
bills = 0.0
deliveries = 0.0
groceries = 0.0
eout = 0.0
savings = 0.0
income = 0.0
leslie = 0.0
other = 0.0
ikea = 0.0
susie = 0.0

#patterns
groceries_pattern = re.compile('HYPERMARKET|SUPERMARKET|LHM|FOOD WO|ALJAZIRA|MIDWAY|CARREFOUR|ALNOOR')
eat_out_pattern = re.compile('Talabat|STARBUCKS|CARIBOU|YOUNIS|YASALAM|SHAKE SHACK|URBAN SLICE|FIVE GUYS')
deliveries_pattern = re.compile('ARAMEX|Aramex|aramex')
bills_pattern = re.compile('Batelco|stc')
cash_pattern = re.compile('WDL')
coffee_pattern = re.compile('CRUST')
leslie_pattern = re.compile('BH25NBOB00000276923162')
rent_pattern = re.compile('200000983477')
car_pattern = re.compile('200005196913')
savings_pattern = re.compile('200006043230|200004304353')
fuel_pattern = re.compile('7896941550852504000')
fuel_pattern_2 = re.compile('ila')
ikea_pattern = re.compile('IKEA')
creditcard_pattern = re.compile('CrediMax')

#date function to get the date
#TODO specify dates to get calculated expenditure
def get_date():
    match = re.search('^FDR.*([A-Z]{3})([0-9]{2})', row[1])
    if match:
        day = match.group(2) + '/' + match.group(1) + "/2020"
        date.append(day)
    else:
        date.append(row[0])
# function to calculate transaction amount
def trans_calc(var):
    match = re.search('([0-9]*\.[0-9]{3})(\-)$', row[4])
    transaction = float(match.group(2) + match.group(1))
    var = var + transaction
    return var

def categorise():
    global creditcard
    global fuel
    global ikea
    global rent
    global car
    global leslie
    global coffee
    global cash
    global bills
    global deliveries
    global income
    global groceries
    global eout
    global savings
    global susie
    global other
    if re.search(groceries_pattern, row[1]) is not None:
        groceries = trans_calc(groceries)
    elif re.search(eat_out_pattern, row[1]) is not None:
        eout = trans_calc(eout)
    elif re.search('([0-9]*\.[0-9]{3})$', row[4]) is not None:
        match = re.search('([0-9]*\.[0-9]{3})$', row[4])
        transaction = float(match.group(0))
        income += transaction
    elif re.search(deliveries_pattern, row[1]) is not None:
        deliveries = trans_calc(deliveries)
    elif re.search(bills_pattern, row[1]) is not None:
        bills = trans_calc(bills)
    elif re.search(cash_pattern, row[1]) is not None:
        cash = trans_calc(cash)
    elif re.search(coffee_pattern, row[1]) is not None:
        coffee = trans_calc(coffee)
    elif re.search(leslie_pattern, row[1]) is not None:
        leslie = trans_calc(leslie)
    elif re.search(rent_pattern, row[1]) is not None:
        rent = trans_calc(rent)
    elif re.search(car_pattern, row[1]) is not None:
        car = trans_calc(car)
    elif re.search(savings_pattern, row[1]) is not None:
        savings = trans_calc(savings)
    elif re.search(fuel_pattern, row[1]) is not None:
        fuel = trans_calc(fuel)
    elif re.search(fuel_pattern_2, row[1]) and re.match('10|15', row[4]) is not None:
        fuel = trans_calc(fuel)
    elif re.search(ikea_pattern, row[1]) is not None:
        ikea = trans_calc(ikea)
    elif re.search(creditcard_pattern, row[1]) is not None:
        creditcard = trans_calc(creditcard)
    else:
        other = trans_calc(other)


with open(argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #print(row[0])
        #date_match = re.search("^FDR", row[1])
        get_date()
        categorise()

print("Income: %.3f" % income)
print("Savings: %.3f" % savings)
print("Groceries: %.3f" % groceries)
print("Eating out: %.3f" % eout)
print("Susie: %.3f" % susie)
print("Coffee: %.3f" % coffee)
print("Car payment: %.3f" % car)
print("Bills: %.3f" % bills)
print("Credit card: %.3f" % creditcard)
print("Fuel: %.3f" % fuel)
print("Deliveries from Aramex: %.3f" % deliveries)
print("Cash withdrawals: %.3f" % cash)
print("Leslie: %.3f" % leslie)
print("IKEA: %.3f" % ikea)
print("Other? = %.3f" % other)

