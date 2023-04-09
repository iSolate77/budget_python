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
cleaner = 0.0
other = 0.0
ikea = 0.0
susie = 0.0


def get_date():
    match = re.search("^FDR.*([A-Z]{3})([0-9]{2})", row[1])
    if match:
        day = match.group(2) + "/" + match.group(1) + "/2020"
        date.append(day)
    else:
        date.append(row[0])


# TODO
def trans_calc(var):
    match = re.search("([0-9]*\.[0-9]{3})(\-)$", row[4])
    transaction = float(match.group(2) + match.group(1))
    var = var + transaction
    return var


def categorise():
    global creditcard
    global fuel
    global ikea
    global rent
    global car
    global cleaner
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
    groceries_pattern = re.compile(
        "HYPERMARKET|SUPERMARKET|LHM|FOOD WO|ALJAZIRA|MIDWAY|CARREFOUR|ALNOOR"
    )
    if re.search(groceries_pattern, row[1]) is not None:
        groceries = trans_calc(groceries)
    elif (
        re.search(
            "Talabat|STARBUCKS|CARIBOU|YOUNIS|YASALAM|SHAKE SHACK|URBAN SLICE|FIVE GUYS",
            row[1],
        )
        is not None
    ):
        eout = trans_calc(eout)
    elif re.search("([0-9]*\.[0-9]{3})$", row[4]) is not None:
        match = re.search("([0-9]*\.[0-9]{3})$", row[4])
        transaction = float(match.group(0))
        income += transaction
    elif re.search("ARAMEX|Aramex|aramex", row[1]) is not None:
        deliveries = trans_calc(deliveries)
    elif re.search("Batelco|stc", row[1]) is not None:
        bills = trans_calc(bills)
    elif re.search("WDL", row[1]) is not None:
        cash = trans_calc(cash)
    elif re.search("CRUST", row[1]) is not None:
        coffee = trans_calc(coffee)
    elif re.search("BH25NBOB00000276923162", row[1]) is not None:
        cleaner = trans_calc(cleaner)
    elif re.search("200000983477", row[1]) is not None:
        rent = trans_calc(rent)
    elif re.search("200005196913", row[1]) is not None:
        car = trans_calc(car)
    elif re.search("200006043230|200004304353", row[1]) is not None:
        savings = trans_calc(savings)
    elif re.search("7896941550852504000", row[1]) is not None:
        fuel = trans_calc(fuel)
    elif re.search("ila", row[1]) and re.match("10", row[4]) is not None:
        fuel = trans_calc(fuel)
    elif re.search("IKEA", row[1]) is not None:
        ikea = trans_calc(ikea)
    elif re.search("CrediMax", row[1]) is not None:
        creditcard = trans_calc(creditcard)
    else:
        other = trans_calc(other)


with open(argv[1], newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row[0])
        # date_match = re.search("^FDR", row[1])
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
print("Cleaner: %.3f" % cleaner)
print("IKEA: %.3f" % ikea)
print("Other? = %.3f" % other)
