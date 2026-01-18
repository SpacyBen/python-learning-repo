# Currency Converter
# by CodeChum Admin

# Create a program that allows the user to convert between different currencies using a dictionary that contains conversion rates. 
# The program should ask the user to enter an amount in one currency, then ask for the target currency, and output the converted amount. 
# The conversion rates should be stored in a dictionary, where the keys are the currency codes (e.g., USD, EUR, GBP) 
# and the values are the conversion rates. If a currency is not found, print "Invalid source currency code." or 
# "Invalid target currency code."

 

# Conversion rates:

# USD - 1.00
# EUR - 0.84
# GBP - 0.72
# JPY - 109.98
# AUD - 1.33
# CAD - 1.26
# CHF - 0.92
# CNY - 6.46
# HKD - 7.76
# NZD - 1.43
# Sample Output 1

# Enter the amount: 123
# Enter the source currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): hkd
# Enter the target currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): usd
# 123.00 HKD = 15.85 USD
# Sample Output 2

# Enter the amount: 421
# Enter the source currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): chf
# Enter the target currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): nzd
# 421.00 CHF = 654.38 NZD
# Sample Output 3

# Enter the amount: 1
# Enter the source currency code (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ssd
# Invalid source currency code.
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