import math
import csv
import argparse #this is a Python standard library module that provides a way to handle command-line arguments.

def landed_cost_myr(price_cny, shipping_cny, fx_rate, margin_pct):

    if margin_pct < 0 or margin_pct >= 1:
        raise ValueError("Margin percentage must be between 0 and 1 (exclusive).")
    elif fx_rate <= 0:
        raise ValueError("Exchange rate must be greater than 0.")
    elif price_cny < 0 or shipping_cny < 0:
        raise ValueError("Price must be non-negative.")
    elif price_cny == 0: #no frew gift/can never be zero.
        raise ValueError("Price cannot be zero.")
    
    price_myr = price_cny * fx_rate

    shipping_myr = shipping_cny * fx_rate

    total_cost = price_myr + shipping_myr

    landed_cost = total_cost / (1 - margin_pct)

    return math.ceil(landed_cost)


def quote_order(csv_path):
    # returns a list of (item, selling price in MYR), one per row in the CSV
    quotes = []
    with open(csv_path, newline='') as f:
        for row in csv.DictReader(f):
            price = landed_cost_myr(float(row['price_cny']), float(row['shipping_cny']), float(row['fx_rate']), float(row['margin_pct']))
            quotes.append((row['item'], price))
    return quotes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate landed cost in MYR.')
    parser.add_argument('--csv', help='CSV of orders with columns: item, price_cny, shipping_cny, fx_rate, margin_pct')
    # not required=True: in --csv mode these come from the file instead
    parser.add_argument('--price_cny', type=float, help='Price in CNY')
    parser.add_argument('--shipping_cny', type=float, help='Shipping cost in CNY')
    parser.add_argument('--fx_rate', type=float, help='Exchange rate from CNY to MYR')
    parser.add_argument('--margin_pct', type=float, help='Margin percentage (as a decimal, e.g., 0.2 for 20%%)')

    args = parser.parse_args()

    if args.csv:
        total = 0
        for item, price in quote_order(args.csv):
            print(f"{item}: RM{price}")
            total += price
        print(f"Order total: RM{total}")
    else:
        if None in (args.price_cny, args.shipping_cny, args.fx_rate, args.margin_pct):
            parser.error("without --csv, you must give --price_cny, --shipping_cny, --fx_rate and --margin_pct")
        final_price = landed_cost_myr(args.price_cny, args.shipping_cny, args.fx_rate, args.margin_pct)
        print (f"The selling price in MYR should be : RM{final_price}")
