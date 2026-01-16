
conversion_rates = {
    "USD": 1.00,
    "EUR": 0.84,
    "GBP": 0.72,
    "JPY": 109.98,
    "AUD": 1.33,
    "CAD": 1.26,
    "CHF": 0.92,
    "CNY": 6.46,
    "HKD": 7.76,
    "NZD": 1.43
}

amount = float(input("Enter theamount: "))
source_currency = input("Enter the source currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ").upper()

if source_currency in conversion_rates:
    usd = amount / conversion_rates[source_currency]
    target_currency = input("Enter the target currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ").upper()
    if target_currency in conversion_rates:
        converted_amount = usd * conversion_rates[target_currency]
        print(f"{amount:.2f} {source_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Invalid target currency code.")
else:
    print("Invalid source currency code.")