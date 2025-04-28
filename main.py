import pandas as pd
import random
import datetime as dt

rng = 10

products = ["A", "B", "C"]
product_list = [random.choice(products) for _ in range(rng)]

prices = [10, 20, 30]
prices_list = [random.choice(prices) for _ in range(rng)]

quantities = [5, 10, 15]
quantities_list = [random.choice(quantities) for _ in range(rng)]

dates = []
start_date = dt.date(2024, 1, 1)
end_date = dt.date(2024, 12, 31)
delta = end_date - start_date
for i in range(rng):
    random_days = random.randint(0, delta.days)
    random_date = start_date + dt.timedelta(days=random_days)
    dates.append(random_date)

dict1 = {
    "product": product_list,
    "price": prices_list,
    "quantity": quantities_list,
    "date": dates,
}

df = pd.DataFrame(dict1)
print(df)

qty = int(input("Enter the quantity: "))
prod = input("Enter the product: ").upper()

if prod in df["product"].values:
    # Sort by product and date ascending (oldest first)
    df_sorted = df[df["product"] == prod].sort_values(by=["product", "date"], ascending=[True, True])
    print(f"The sorted DF:\n{df_sorted}\n")

    for idx in df_sorted.index:
        available_qty = df.at[idx, 'quantity']

        if qty <= 0:
            break  # Done

        if available_qty >= qty:
            df.at[idx, 'quantity'] = available_qty - qty
            print(f"Updated {prod} on {df.at[idx, 'date']} to quantity {df.at[idx, 'quantity']}")
            qty = 0  # All quantity used
        else:
            df.at[idx, 'quantity'] = 0
            qty -= available_qty
            print(f"Set {prod} from {available_qty} on {df.at[idx, 'date']} to 0, remaining qty to subtract: {qty}")
else:
    print("Product not found. Please enter a valid product.")

print("\nFinal dataframe:")
print(df)
