# import csv library and import defaultdict from collections
import sys
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
# input_file.close()

        # importing EPDF libary to work with PDF files
        from fpdf import FPDF
        from datetime import date, timedelta
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(50, 10, "Haitong International (UK) Ltd: Fidessa Transaction Report")
        pdf.ln(15)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(35, 10, "Trading Venue")
        pdf.cell(50, 10, "Gross Volume")
        pdf.ln(8)
        # iterating through the collection set created above and displaying
        # each key with the sum of its values, rounded to 2 decimal points, and adding commas for '000s
        yday = date.today() - timedelta(1)
        filename = "FidessaReport_{}.pdf".format(yday.strftime("%m_%d_%Y"))
        for key in data:
            pdf.set_font("Arial", "", 10)
            pdf.cell(35, 5, key)
            value = "{:,}".format((round(sum(data[key]), 2)))
            pdf.multi_cell(50, 5, str(value))
            pdf.ln(0.5)
        pdf.output(filename, "F")

# writing results to output csv file
    with open("FidessaReport_{}.csv".format(yday.strftime("%m_%d_%Y")), 'w') as output_file:
        header = ["Trading Venue", "Gross Volume"]
        writer = csv.DictWriter(output_file, fieldnames=header)
        writer.writeheader()
        # iterating through the collection set created above and displaying
        # each key with the sum of its values, rounded to 2 decimal points, and adding commas for '000s
        for key in data:
            value = "{:,}".format((round(sum(data[key]), 2)))
            writer.writerow({header[0]: key, header[1]: value})

# closing output csv file
# output_file.close()