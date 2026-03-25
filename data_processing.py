import os
import csv

data_folder = "data"
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_folder, filename)

        with open(file_path, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            heading = csv_reader.fieldnames
            for row in csv_reader:
                with open("processed_data.csv", "a") as file:
                    fieldnames = ["sales", heading[3], heading[4]]
                    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                    csv_writer.writeheader()

                    if row["product"] == "pink morsel":
                        morsel_sales = float(row["price"].replace("$", "")) * float(row["quantity"].replace("$", ""))
                        csv_writer.writerow({
                            "sales": morsel_sales,
                            "date": row["date"],
                            "region": row["region"]
                        })