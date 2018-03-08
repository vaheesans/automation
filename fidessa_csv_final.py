# import csv library and import defaultdict from collections
import csv
from collections import defaultdict

# initiating a defaultdict to handle collections in dictionary
data = defaultdict(list)

# opening csv file
with open("transaction2.csv") as input_file:
    reader = csv.DictReader(input_file)

    # iterating through the csv file
    for column in reader:
        # assigning variables to columns "Exchange_Id" and "Gross_Considerations"
        tradingVenue = column["Exchange_Id"]
        grossVolume = float(column["Gross_Consideration"])
        # initiating new dictionary
        d = dict()
        # assigning tradingVenue entries as keys and grossVolume entries as values
        d[tradingVenue] = grossVolume

        # iterating through each dictionary keys, creating a data set and assigning all
        # values to one key
        for item in d.keys():
            data[item].append(d[item])

# closing input csv file
input_file.close()

# writing results to output csv file
with open('FidessaReport.csv', 'w') as output_file:
    fieldnames = ["Trading Venue", "Gross Volume"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    # iterating through the collection set created above and displaying
    # each key with the sum of its values, rounded to 2 decimal points
    for key in data:
        writer.writerow({fieldnames[0]: key, fieldnames[1]: round(sum(data[key]), 2)})

# closing output csv file
output_file.close()