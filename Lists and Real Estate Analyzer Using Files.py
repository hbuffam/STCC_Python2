# Holly Buffam
# CIT-117
# Lists and Real Estate Analyzer Version with Files

import csv

def getDataInput():
    with open("RealEstateData.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        lstData = [row for row in reader]
    return lstData

def getMedian(lstPrices):
    lstPrices.sort()
    length = len(lstPrices)
    if length % 2 == 0:
        return (lstPrices[length // 2] + lstPrices[(length // 2) - 1]) / 2
    else:
        return lstPrices[length // 2]

def main():
    lstData = getDataInput()
    lstPrices = []
    dictCity = {}
    dictPropertyType = {}

    for row in lstData:
        city = row[1]
        propertyType = row[7] if row[7] else "Unknown"
        try:
            price = float(row[8])
        except ValueError:
            continue

        lstPrices.append(price)

        if city in dictCity:
            dictCity[city] += price
        else:
            dictCity[city] = price

        if propertyType in dictPropertyType:
            dictPropertyType[propertyType] += price
        else:
            dictPropertyType[propertyType] = price

    lstPrices.sort()
    total = sum(lstPrices)
    average = total / len(lstPrices)
    median = getMedian(lstPrices)


    print(f"{'Minimum':15s}{min(lstPrices):15,.2f}")
    print(f"{'Maximum':15s}{max(lstPrices):15,.2f}")
    print(f"{'Sum':15s}{total:15,.2f}")
    print(f"{'Avg':15s}{average:15,.2f}")
    print(f"{'Median':15s}{median:15,.2f}")


    print(f"{'Summary by Property Type:':30s}")
    for ptype, value in sorted(dictPropertyType.items(), key=lambda x: x[1], reverse=True):
        print(f"{ptype:20s}{value:15,.2f}")


    print("\nSummary by City")
    for city, value in (dictCity.items()):
        print(f"{city:20s}{value:15,.2f}")

if __name__ == "__main__":
    main()
