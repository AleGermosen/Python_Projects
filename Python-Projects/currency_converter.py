### Currency Converter

# # User inputs:
# Amount to convert
# Source and Target currency from given options
# Fixed conversion from source to target
# Display currency converted in multiple currencies
# Display a history of conversions

nested_dict = {
    "USD": {'EUR': 0.95, 'CAD': 1.40, 'GBP': 0.79},
    "EUR": {'USD': 1.06, 'CAD': 0.68, 'GBP': 0.83},
    "CAD": {'USD': 0.71, 'EUR': 1.48, 'GBP': 0.56},
    "GBP": {'USD': 1.27, 'EUR': 1.20, 'CAD': 1.78}
}

def get_user_input():
    amount_to_convert = float(input("Enter the amount: "))
    source_currency = (input("(USD/EUR/CAD/GBP): ")).upper()
    target_currency = (input("(USD/EUR/CAD/GBP), separated with commas: ")).upper()
    target_currency = target_currency.split(",")
    return amount_to_convert, source_currency, target_currency


def convert_to_currency(d, amount_to_convert, source_currency, target_currency):    
    conversion = []
    
    count_items = 0
    total_items = len(target_currency)
    while (count_items < total_items):
        target = d[source_currency][target_currency[count_items]]
        convert = amount_to_convert * target
        conversion.append(convert)
        count_items += 1
    return conversion

def currency_converter():
    user_amount, user_source, user_target = get_user_input()
    user_conversion = convert_to_currency(nested_dict, user_amount, user_source, user_target)
    
    count_items = 0
    total_items = len(user_target)
    while (count_items < total_items):
        converted_currency = user_conversion[count_items]
        print(f"{user_amount} {user_source} is equal to {converted_currency} {user_target[count_items]}")
        count_items += 1