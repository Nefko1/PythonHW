def taxiFee (distance_km):
    distance_m = distance_km * 1000
    tariffUnits = distance_m / 140
    totalFee = 4 + 0.25 * tariffUnits
    return totalFee

print(round((taxiFee(5)), 2))