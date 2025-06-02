def calculate_total(price, tax_rate):
    try:
        total = price + (price * tax_rate)

        return total
    except TypeError as e:

        print(f"TypeError occurred: {e}")

        return None

def main():
    try:
        price_input = input("Enter the price: ")

        tax_rate_input = input("Enter the tax rate (e.g., 0.05 for 5%): ")

        # Convert inputs to float
        price = float(price_input)
        tax_rate = float(tax_rate_input)

        total = calculate_total(price, tax_rate)
        if total is not None:
            print(f"The total price including tax is: ${total:.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":

    main()




