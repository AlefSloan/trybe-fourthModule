def fuel_seller(liter, fuel_type):
    price = 2.50
    if fuel_type == "G":
        if liter <= 20:
            return (liter * price) * 0.96
        else:
            return (liter * price) * 0.94
    else:
        if liter <= 20:
            return (liter * price) * 0.97
        else:
            return (liter * price) * 0.95


print(fuel_seller(50, 'G'))
