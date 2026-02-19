import openai
import pandas as pd
import pdfplumber
import tiktoken


# Paths to datasets and codebook
base = "C:/Users/.../gpt_hatestoxicspeech/"
covid_path = base + "sample_covid.csv"
farmer_path = base + "sample_farmer.csv"
openai.api_key = "YOUR_API_KEY"

# Covid Stuff
covid_msg = pd.read_csv(covid_path, encoding='utf-8')
covid_txts = covid_msg["raw_text"].tolist()

#Farmer Stuff
farmer_msg = pd.read_csv(farmer_path, encoding='utf-8')
farmer_txts = farmer_msg["raw_text"].tolist()

# Read in codebook
codebook = ""
# GPT suggested pdfpblumber for better read-in quality
with pdfplumber.open("codebook_v1_manualcoding.pdf") as pdf:
    # Extract text from each page and concatenate it
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            codebook += page_text + "\n"

# Content for annotation task (incl. codebook)
content = f"Entscheide in dieser Aufgabe, ob die Nachricht 'Hate Speech' (Hassrede), 'Toxic Speech' (toxische Rede) oder weder noch enthält. Die meisten Nachrichten sind auf Deutsch, können aber auch andere Sprachen enthalten. Folge diesen Richtlinien beim Labeln der Nachrichten:\n{codebook}"

# Version 1 to check how expensive each model is
# calculate tokens
'''def count_tokens(model, text):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)


# calculate cost based on tokens
def calculate_gpt_cost(model, prompt_tokens, completion_tokens):
    prices_per_1k_tokens_inc = {
        'gpt-4': 0.03,
        'gpt-3.5-turbo': 0.002,
    }

    prices_per_1k_tokens_outc = {
        'gpt-4': 0.06,
        'gpt-3.5-turbo': 0.002
    }

    # Get the correct prices for input and output tokens
    price_per_1k_inc = prices_per_1k_tokens_inc[model]
    price_per_1k_outc = prices_per_1k_tokens_outc[model]  # Fixed this line to use the output prices dictionary

    # Calculate cost separately for input and output tokens
    input_cost = (prompt_tokens / 1000) * price_per_1k_inc
    output_cost = (completion_tokens / 1000) * price_per_1k_outc

    # Total cost is the sum of input and output costs
    total_cost = input_cost + output_cost
    return round(total_cost, 4)'''


def annotate_texts(model, texts, content, num_msg=None):
    labels = []
    total_cost = 0

    if num_msg is not None:
        texts = texts[:num_msg]

    enum = 0
    for txt in texts:
        enum += 1
        print(f"Nachricht {enum}: {txt}")

        # Count tokens for prompt
        #prompt_tokens = count_tokens(model, content + txt)

        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": content},
                      {"role": "user",
                       "content": ("Label die Nachrichten nur mit 'Hate Speech', 'Toxicity', oder 'None', auch wenn du unsicher bist: "+ txt +". Wenn eine Nachricht einen Link enthält, schau dir an ob die Wörter in dem Link eine toxische Bedeutung haben bzw. Hatespeech sind. Gebe eine Erklärung zu deiner Entscheidung in Klammern '()'.")}])

        print(f'Label: {response["choices"][0]["message"]["content"]}')
        label = response["choices"][0]["message"]["content"]
        labels.append(label)

        # count response tokens
        #completion_tokens = count_tokens(model, label)

        # Calculate cost and add up
        #cost = calculate_gpt_cost(model, prompt_tokens, completion_tokens)
        #total_cost += cost

    #print(f"Total cost for all annotations with model {model}: ${total_cost}")
    return labels


# Run annotations
# how many texts get annotated
num_covid_messages =500  # how many COVID messages
num_farmer_messages =500  # how many Farmer messages


#Covid
covid_labels_3_5_turbo = annotate_texts("gpt-3.5-turbo", covid_txts, content, num_msg=num_covid_messages)
covid_labels_4 = annotate_texts("gpt-4", covid_txts, content, num_msg=num_covid_messages)

#Farmer
farmer_labels_3_5_turbo = annotate_texts("gpt-3.5-turbo", farmer_txts, content, num_msg=num_farmer_messages)
farmer_labels_4 = annotate_texts("gpt-4", farmer_txts, content, num_msg=num_farmer_messages)
print(farmer_labels_3_5_turbo)





# bring labels and other data in data frame
#Covid
df_covid = pd.DataFrame({
    "text": covid_txts[:num_covid_messages],
    # split & strip expressions suggested by GPT
    "label_3_5_turbo": [i.split("(", 1)[0].strip() for i in covid_labels_3_5_turbo],
    "explanation_3_5_turbo": [j.split("(", 1)[1].strip(")") if "(" in j else "" for j in covid_labels_3_5_turbo],
    "label_4": [k.split("(", 1)[0].strip() for k in covid_labels_4],
    "explanation_4": [l.split("(", 1)[1].strip(")") if "(" in l else "" for l in covid_labels_4],
})


# Farmer
df_farmer = pd.DataFrame({
    "text": farmer_txts[:num_farmer_messages],
    # split & strip expressions suggested by GPT
    "label_3_5_turbo": [p.split("(", 1)[0].strip() for p in farmer_labels_3_5_turbo],
    "explanation_3_5_turbo": [q.split("(", 1)[1].strip("(") if "(" in q else "" for q in farmer_labels_3_5_turbo],
    "label_4": [r.split("(", 1)[0].strip() for r in farmer_labels_4],
    "explanation_4": [s.split("(", 1)[1].strip(")") if "(" in s else "" for s in farmer_labels_4]
})


print(df_covid.head())
print(df_farmer.head())




# add anotations and explanations to csv that contains the rest of the data
# Covid
covid_msg["Label 3.5 turbo"] = df_covid["label_3_5_turbo"]
covid_msg["Explanation 3.5 turbo"] = df_covid["explanation_3_5_turbo"]
covid_msg["Label 4.0"] = df_covid["label_4"]
covid_msg["Explanation 4.0"] = df_covid["explanation_4"]
print(covid_msg)

# Farmer
farmer_msg["Label 3.5 turbo"] = df_farmer["label_3_5_turbo"]
farmer_msg["Explanation 3.5 turbo"] = df_farmer["explanation_3_5_turbo"]
farmer_msg["Label 4.0"] = df_farmer["label_4"]
farmer_msg["Explanation 4.0"] = df_farmer["explanation_4"]
print(farmer_msg)



# convert changed df to csv w/o index
covid_msg.to_csv("sample_covid_gpt_annot.csv", index=False)
farmer_msg.to_csv("sample_farmer_gpt_annot.csv", index=False)

