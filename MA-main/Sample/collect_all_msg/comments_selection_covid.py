import os
import pandas as pd

direct_covid1 = r"C:/Users/.../csv_data_1_corona"
direct_covid2 = r"C:/Users/.../csv_data_2_corona"


covid1 = []
covid2 = []


for dirpath, dirnames, filenames in os.walk(direct_covid1):
    for name in filenames:
        if name.endswith(".csv"):
            covid1.append(name)

print(f"Covid 1st List: {covid1}")

for dirpath, dirnames, filenames in os.walk(direct_covid2):
    for name in filenames:
        if name.endswith(".csv"):
            #print(name)
            covid2.append(name)

print(f"Covid 2nd List: {covid2}")



done_reading_msg = []
comments = pd.DataFrame()

# Get comments
failed_channels = []
for csv1 in covid1:

    if csv1 in done_reading_msg:
        continue

    else:
        print(csv1)
        file = f"{direct_covid1}/{csv1}"

        # try and except logic as hint from Chat GPT
        try:
            df = pd.read_csv(file)

            if df.empty:
                continue
            else:
                comments = pd.concat([comments, df])

        # Errors from GPT
        except pd.errors.EmptyDataError:
            print('CSV file is empty')
            failed_channels.append(csv1)
            continue
        except FileNotFoundError:
            print('CSV file not found')
            failed_channels.append(csv1)
            continue
        done_reading_msg.append(csv1)




print("2nd covid list")
for csv2 in covid2:
    if csv2 in done_reading_msg:
        continue

    else:
        print(csv2)
        file = f"{direct_covid2}/{csv2}"

        try:
            df = pd.read_csv(file)

            if df.empty:
                continue
            else:
                comments = pd.concat([comments, df])
        except pd.errors.EmptyDataError:
            print('CSV file is empty')
            failed_channels.append(csv2)
            continue


        except FileNotFoundError:
            print('CSV file not found')
            failed_channels.append(csv2)
            continue
        done_reading_msg.append(csv2)

print(comments)
print(done_reading_msg)
print(len(list(set(done_reading_msg))))


comments.to_csv("corona_comments.csv")
failed_channels = pd.DataFrame({"col": failed_channels})
failed_channels.to_csv("corona_failed_channels.csv")


