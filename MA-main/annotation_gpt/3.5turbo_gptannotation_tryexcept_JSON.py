import json
import os.path
import time
import openai
import pandas as pd
import pdfplumber

# Paths to datasets and codebook
base = "C:/Users/.../gpt_hatestoxicspeech/"
covid_path = base + "sample_covid_big.csv"
covid_raw_path = base + "covid_raw/"
farmer_path = base + "sample_farmer_big.csv"
farmer_raw_path = base + "farmer_raw/"
openai.api_key = "YOUR_KEY"



# Covid stuff
# Load COVID  first (later also farmer)
covid_msg = pd.read_csv(covid_path, encoding='utf-8')
covid_txts = covid_msg["raw_text"].tolist()


# Read in codebook
codebook = ""
# GPT suggested pdfpblumber for better read-in quality
with pdfplumber.open("codebook_v1_manualcoding.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            codebook += page_text + "\n"


# Content for System prompt
content = f"Entscheide in dieser Aufgabe, ob die Nachricht 'Hate Speech' (Hassrede), 'Toxic Speech' (toxische Rede) oder weder noch enthält. Die meisten Nachrichten sind auf Deutsch, können aber auch andere Sprachen enthalten. Folge diesen Richtlinien beim Labeln der Nachrichten:\n{codebook} \nDas Label sollte sich auf folgende Kategorien beschränken: Hate Speech, Toxicity oder None. Stelle sicher, dass die Antwort nur das Label enthält."


# Annotation function with retry mechanism and incremental saving
def annotate_texts(model, df, content, csv_path, raw_path, num_msg=None):
    if num_msg is not None:
        df = df.head(num_msg)

    for idx, txt in enumerate(df["raw_text"], start=1):
        response = None
        raw_file = raw_path + str(idx) + ".json"

        if os.path.isfile(raw_file):
            with open(raw_file, "r") as file:
                response = json.load(file)
        else:
            success = False
            for retry in range(5):
                try:
                    # Call the API with the required message
                    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[{"role": "system", "content": content},
                                  {"role": "user", "content": ("Label die Nachrichten nur mit 'Hate Speech', 'Toxicity', oder 'None'. Falls du unsicher bist, wähle 'None': " + txt + ". Wenn eine Nachricht einen Link enthält, schau dir an ob die Wörter in dem Link eine toxische Bedeutung haben bzw. Hatespeech sind.")}]
                    )

                    with open(raw_file, "w+") as file:
                        json.dump(response, file)

                    success = True
                    break

                # because of server errors etc.
                except Exception as e:
                    print(f"Error encountered for message {idx}. Retrying in 3secs Error: {e}")

                    # make sure that the system waits a bit
                    time.sleep(3)

            if not success:
                print(f"Retried idx {idx} 5 times without success.")

        # Extract label from GPT's response
        label = response["choices"][0]["message"]["content"].strip()

        # Add the label to the dataframe (index from for loop starts at 1 but lines at 0 which is why I need to subtract 1 from the enumerated index
        df.at[idx - 1, "Label 3.5 turbo"] = label

        if idx % 200 == 0:
            print(f"Message {idx}: Label = {label}")

    df.to_csv(csv_path)
    return df

# Covidskeptics things
# Run annotations for COVID data
num_covid_messages = 25000
covid_csv_path = "sample_covid_gpt_annot_BIG.csv"
covid_msg = annotate_texts("gpt-3.5-turbo", covid_msg, content, covid_csv_path, covid_raw_path, num_msg=num_covid_messages)
print("COVID data annotation and saving in CSV done")



# Farmer Protest things
# Load Farmer dataset and process annotations
farmer_msg = pd.read_csv(farmer_path, encoding='utf-8')
farmer_txts = farmer_msg["raw_text"].tolist()

# Run annotations for Farmer data
num_farmer_messages = 25000
farmer_csv_path = "sample_farmer_gpt_annot_BIG.csv"
farmer_msg = annotate_texts("gpt-3.5-turbo", farmer_msg, content, farmer_csv_path, farmer_raw_path, num_msg=num_farmer_messages)
print("Farmer data annotation and saving in CSV done")
