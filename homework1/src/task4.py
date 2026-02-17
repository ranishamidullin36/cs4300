# function to take 2 inputs which are the price and the discount % for the price
def calculate_discount(originalPrice, discountPercent):
    discountPercent = (100 - discountPercent)/100
    discountedPrice = originalPrice * discountPercent
    return round(discountedPrice, 2)


print(calculate_discount(38, 19))
