import pandas as pd
import random
import datetime as dt

def random_products(n):
    return [random.choice(["A", "B", "C"]) for _ in range(n)]

def random_prices(n):
    return [random.choice([10, 20, 30]) for _ in range(n)]

def random_quantities(n):
    return [random.choice([5, 10, 15]) for _ in range(n)]

def random_dates(n):
    return [dt.date.today() + dt.timedelta(days=random.randint(0, 365)) for _ in range(n)]

def random_table(n):
    product_list = random_products(n)
    prices_list = random_prices(n)
    quantities_list = random_quantities(n)
    dates = random_dates(n)

    return product_list, prices_list, quantities_list, dates
    
def the_data():
    qty = int(input("Enter the quantity: "))
    prod = input("Enter the product: ").upper()

    if prod in df["product"].values:
        df_sorted = df[df["product"] == prod].sort_values(by=["product", "date"], ascending=[True, True])
        print(f"The sorted DF:\n{df_sorted}\n")

        for idx in df_sorted.index:
            available_qty = df.at[idx, 'quantity']

            if qty <= 0:
                break  

            if available_qty >= qty:
                df.at[idx, 'quantity'] = available_qty - qty
                print(f"Updated {prod} on {df.at[idx, 'date']} to quantity {df.at[idx, 'quantity']}")
                qty = 0  
            else:
                df.at[idx, 'quantity'] = 0
                qty -= available_qty
                print(f"Set {prod} from {available_qty} on {df.at[idx, 'date']} to 0, remaining qty to subtract: {qty}")
    else:
        print("Product not found. Please enter a valid product.")

    print("\nFinal dataframe:")
    print(df)

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the DataFrame: "))
    product_list, prices_list, quantities_list, dates = random_table(n)

    dict1 = {
        "product": product_list,
        "price": prices_list,
        "quantity": quantities_list,
        "date": dates
    }

    df = pd.DataFrame(dict1)
    print(df)

    the_data()  
