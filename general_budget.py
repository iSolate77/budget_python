import re
import csv
from sys import argv


class TransactionCategorizer:
    def __init__(self):
        self.categories = {
            "groceries": (
                "HYPERMARKET|SUPERMARKET|LHM|FOOD WO|ALJAZIRA|MIDWAY|CARREFOUR|ALNOOR",
                0.0,
            ),
            "eat_out": (
                "Talabat|STARBUCKS|CARIBOU|YOUNIS|YASALAM|SHAKE SHACK|URBAN SLICE|FIVE GUYS",
                0.0,
            ),
            "deliveries": ("ARAMEX|Aramex|aramex", 0.0),
            "bills": ("Batelco|stc", 0.0),
            "cash": ("WDL", 0.0),
            "coffee": ("CRUST", 0.0),
            "cleaner": ("BH25NBOB00000276923162", 0.0),
            "rent": ("200000983477", 0.0),
            "car": ("200005196913", 0.0),
            "savings": ("200006043230|200004304353", 0.0),
            "fuel": ("7896941550852504000", 0.0),
            "fuel_2": ("ila", 0.0),
            "ikea": ("IKEA", 0.0),
            "creditcard": ("CrediMax", 0.0),
            "income": ("", 0.0),
            "other": ("", 0.0),
            "susie": ("", 0.0),
        }

    def update_category(self, category_name, amount):
        current_amount = self.categories[category_name][1]
        self.categories[category_name] = (
            self.categories[category_name][0],
            current_amount + amount,
        )

    def categorize_transaction(self, row):
        for category, (pattern, amount) in self.categories.items():
            if re.search(pattern, row[1]) is not None:
                if (
                    category == "income"
                    and re.search("([0-9]*\.[0-9]{3})$", row[4]) is not None
                ):
                    match = re.search("([0-9]*\.[0-9]{3})$", row[4])
                    transaction = float(match.group(0))
                    self.update_category(category, transaction)
                elif category != "income":
                    match = re.search("([0-9]*\.[0-9]{3})(\-)$", row[4])
                    transaction = float(match.group(2) + match.group(1))
                    self.update_category(category, transaction)
                break
        else:
            match = re.search("([0-9]*\.[0-9]{3})(\-)$", row[4])
            transaction = float(match.group(2) + match.group(1))
            self.update_category("other", transaction)


def get_date(row):
    date = []
    match = re.search("^FDR.*([A-Z]{3})([0-9]{2})", row[1])
    if match:
        day = match.group(2) + "/" + match.group(1) + "/2020"
        date.append(day)
    else:
        date.append(row[0])
    return date


def main():
    transaction_categorizer = TransactionCategorizer()
    dates = []
    with open(argv[1], newline="") as csvfile:
        reader = csv.reader(csvfile)
    for row in reader:
        dates.append(get_date(row)[0])
        transaction_categorizer.categorize_transaction(row)

    for category, (_, amount) in transaction_categorizer.categories.items():
        print(f"{category.capitalize()}: {amount:.3f}")


if __name__ == "__main__":
    main()
