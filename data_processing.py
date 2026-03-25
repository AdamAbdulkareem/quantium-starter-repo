import os
import csv

data_folder = "data"
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_folder, filename)

        with open("processed_data.csv", "w") as file:
            csv_writer = csv.writer(file)
            header = ["sales", "date", "region"]
            csv_writer.writerow(header)

            with open(file_path, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                        if row["product"] == "pink morsel":
                            morsel_sales = float(row["price"][1:]) * float(row["quantity"])
                            csv_writer.writerow([morsel_sales, row["date"], row["region"]])