import os
import pandas as pd

direct_farmer = r"C:/Users/.../csv_data_farmerprotest.csv"

farmer = []

for dirpath, dirnames, filenames in os.walk(direct_farmer):
    for name in filenames:
        if name.endswith(".csv"):
            farmer.append(name)

print(f"Farmer protest list: {farmer}")

done_reading_msg = []
comments = pd.DataFrame()

# Get comments
failed_channels = []

for csv in farmer:
    if csv in done_reading_msg:
        continue

    else:
        print(csv)
        file = f"{direct_farmer}/{csv}"

        try:
            df = pd.read_csv(file)

            if df.empty:
                continue
            else:
                comments = pd.concat([comments, df])

        except pd.errors.EmptyDataError:
            print('CSV file is empty')
            failed_channels.append(csv)
            continue
        except FileNotFoundError:
            print('CSV file not found')
            failed_channels.append(csv)
            continue
        done_reading_msg.append(csv)

comments.to_csv("farmerprotest_comments.csv")
failed_channels = pd.DataFrame({"col": failed_channels})
failed_channels.to_csv("farmerprotest_failed_channels.csv")



