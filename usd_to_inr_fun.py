# Function to convert USD to INR
def usd_to_inr(usd_amount, exchange_rate):
    return usd_amount * exchange_rate

# Example usage
usd_amount = float(input("Enter the amount in USD: "))
exchange_rate = float(input("Enter the exchange rate (USD to INR): "))
inr_amount = usd_to_inr(usd_amount, exchange_rate)
print(f"The amount in INR is: {inr_amount}")