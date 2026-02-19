import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score

basic_path = r"C:/Users/.../my_and_gpt_annot/"


# Load in the annotations
# Round 1: Covid & Farmer protests
round1_cov_both = pd.read_csv(basic_path + "sample_covid_gpt_annot.csv", encoding="utf-8")
round1_farm_both = pd.read_csv(basic_path + "sample_farmer_gpt_annot.csv", encoding="utf-8")

# Round 2: Covid & Farmer protests
round2_cov_3_5 = pd.read_csv(basic_path + "sample_covid_gpt_annot_v2.csv", encoding="utf-8")
round2_farm_3_5 = pd.read_csv(basic_path + "sample_farmer_gpt_annot_v2.csv", encoding="utf-8")


# Replace NaN values with 'None' (as Excel just puts nan for every "None") in all relevant columns

# Covid
# Round 1
round1_cov_both["Toxicity/Hatespeech/None"] = round1_cov_both["Toxicity/Hatespeech/None"].fillna("None").str.strip()
round1_cov_both["Label 3.5 turbo"] = round1_cov_both["Label 3.5 turbo"].fillna("None").str.strip()
round1_cov_both["Label 4.0"] = round1_cov_both["Label 4.0"].fillna("None").str.strip()

# Round 2
round2_cov_3_5["Toxicity/Hatespeech/None"] = round2_cov_3_5["Toxicity/Hatespeech/None"].fillna("None").str.strip()
round2_cov_3_5["Label 3.5 turbo"] = round2_cov_3_5["Label 3.5 turbo"].fillna("None").str.strip()


# Farmer
# Round 1
round1_farm_both["Toxicity/Hatespeech/None"] = round1_farm_both["Toxicity/Hatespeech/None"].fillna("None").str.strip()
round1_farm_both["Label 3.5 turbo"] = round1_farm_both["Label 3.5 turbo"].fillna("None").str.strip()
round1_farm_both["Label 4.0"] = round1_farm_both["Label 4.0"].fillna("None").str.strip()

# Round 2
round2_farm_3_5["Toxicity/Hatespeech/None"] = round2_farm_3_5["Toxicity/Hatespeech/None"].fillna("None").str.strip()
round2_farm_3_5["Label 3.5 turbo"] = round2_farm_3_5["Label 3.5 turbo"].fillna("None").str.strip()





# Define the labels of interest
labels = ["None", "Toxicity", "Hate Speech"]


# define accuracy dic
title = ""
accur = float
accuracies = {title: accur}

# Create confusion matrix for annotation comparisons
def create_confusion_matrix(annotator1, annotator2):
    # Filter to only include rows where both annotations are one of the specified labels
    filtered_data = pd.DataFrame({'My Annotation': annotator1, 'GPT Annotation': annotator2})
    filtered_data = filtered_data[filtered_data['My Annotation'].isin(labels) & filtered_data['GPT Annotation'].isin(labels)]
    # Create the confusion matrix, restricting to the specified labels
    return pd.crosstab(filtered_data['My Annotation'], filtered_data['GPT Annotation'], rownames=['My Annotation'], colnames=['GPT Annotation']).reindex(index=labels, columns=labels, fill_value=0)


# Create heatmap
def plot_heatmap(conf_matrix, title):
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="YlGnBu", cbar=False)
    plt.title(title)
    plt.xlabel("GPT Annotation")
    plt.ylabel("My Annotation")
    plt.show()


def save_dataframe_as_png(df, output_path):
    # Reset the index so the row labels (e.g., "None", "Toxicity", "Hate Speech") are included in the table
    df_reset = df.reset_index()

    # Set up a figure with appropriate size
    fig, ax = plt.subplots(figsize=(10, len(df) * 0.6))  # Adjust height based on rows
    ax.axis('tight')
    ax.axis('off')

    # Create a table with the DataFrame's values and column labels
    table = plt.table(
        cellText=df_reset.values,
        colLabels=df_reset.columns,
        cellLoc='center',
        loc='center',
        colLoc='center'
    )

    # Adjust table properties for better appearance
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(df_reset.columns))))

    # Save the table as a PNG image
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()



def generate_classification_report(annotator1, annotator2, title, movement, round_num):
    print(f"Classification Report - {title}")
    print(accuracy_score(annotator1, annotator2))
    print(classification_report(annotator1, annotator2, labels=labels, zero_division=0))
    print("\n")

    report = classification_report(annotator1, annotator2, labels=labels, zero_division=0, output_dict=True)
    df = pd.DataFrame(report).transpose()

    name = ""
    if annotator2.name == "Label 3.5 turbo":
        name = "3_5_turbo"
    if annotator2.name == "Label 4.0":
        name = "4_0"


    title = f"{movement}_{round_num}_GroundTruth_{name}"

    # Define output paths
    output_dir = r"C:/Users/whatt/.../HeatPlots_Results_Compare_Annot/"
    csv_output_path = f"{output_dir}{title}.csv"
    png_output_path = f"{output_dir}{title}.png"

    # Save the classification report as a CSV
    df.to_csv(csv_output_path, encoding="utf-8")
    print(f"CSV saved at {csv_output_path}")

    # Save the classification report as a PNG
    save_dataframe_as_png(df, png_output_path)
    print(f"PNG saved at {png_output_path}")
    #df.to_csv(f"C:/Users/.../HeatPlots_Results_Compare_Annot/{title}.csv")


# Confusion matrices and heatmaps

# Round 1 (w/ 3.5 turbo & 4.0)
# Covid annotation comparisons
conf_matrix_covid_35_r1 = create_confusion_matrix(round1_cov_both["Toxicity/Hatespeech/None"], round1_cov_both["Label 3.5 turbo"])
plot_heatmap(conf_matrix_covid_35_r1, "Covid: My Annotation vs GPT-3.5-turbo, Round 1")

conf_matrix_covid_40_1 = create_confusion_matrix(round1_cov_both["Toxicity/Hatespeech/None"], round1_cov_both["Label 4.0"])
plot_heatmap(conf_matrix_covid_40_1, "Covid: My Annotation vs GPT-4.0, Round 1")

# Farmer annotation comparisons
conf_matrix_farmer_35_1 = create_confusion_matrix(round1_farm_both["Toxicity/Hatespeech/None"], round1_farm_both["Label 3.5 turbo"])
plot_heatmap(conf_matrix_farmer_35_1, "Farmer: My Annotation vs GPT-3.5-turbo, Round 1")

conf_matrix_farmer_40_1 = create_confusion_matrix(round1_farm_both["Toxicity/Hatespeech/None"], round1_farm_both["Label 4.0"])
plot_heatmap(conf_matrix_farmer_40_1, "Farmer: My Annotation vs GPT-4.0, Round 1")


# Round 2 (only 3.5 turbo)
# Covid annotation comparisons
conf_matrix_covid_35_2 = create_confusion_matrix(round2_cov_3_5["Toxicity/Hatespeech/None"], round2_cov_3_5["Label 3.5 turbo"])
plot_heatmap(conf_matrix_covid_35_2, "Covid: My Annotation vs GPT-3.5-turbo, Round 2")

# Farmer annotation comparisons
conf_matrix_farmer_35_2 = create_confusion_matrix(round2_farm_3_5["Toxicity/Hatespeech/None"], round2_farm_3_5["Label 3.5 turbo"])
plot_heatmap(conf_matrix_farmer_35_2, "Farmer: My Annotation vs GPT-3.5-turbo, Round 2")



#### CLASSIFICATION reports
generate_classification_report(round1_cov_both["Toxicity/Hatespeech/None"], round1_cov_both["Label 3.5 turbo"], "Covid: My Annotation vs GPT-3.5-turbo, Round 1", "covid", "round1")
generate_classification_report(round1_cov_both["Toxicity/Hatespeech/None"], round1_cov_both["Label 4.0"], "Covid: My Annotation vs GPT-4.0, Round 1", "covid", "round1")
generate_classification_report(round1_farm_both["Toxicity/Hatespeech/None"], round1_farm_both["Label 3.5 turbo"], "Farmer: My Annotation vs GPT-3.5-turbo, Round 1", "farmer", "round1")
generate_classification_report(round1_farm_both["Toxicity/Hatespeech/None"], round1_farm_both["Label 4.0"], "Farmer: My Annotation vs GPT-4.0, Round 1", "farmer", "round1")
generate_classification_report(round2_cov_3_5["Toxicity/Hatespeech/None"], round2_cov_3_5["Label 3.5 turbo"], "Covid: My Annotation vs GPT-3.5-turbo, Round 2", "covid", "round2")
generate_classification_report(round2_farm_3_5["Toxicity/Hatespeech/None"], round2_farm_3_5["Label 3.5 turbo"], "Farmer: My Annotation vs GPT-3.5-turbo, Round 2", "farmer", "round2")


def save_dataframe_as_png(df, output_path):
    # Set up a figure
    fig, ax = plt.subplots(figsize=(10, len(df) * 0.5))  # Adjust height based on rows
    ax.axis('tight')
    ax.axis('off')

    # Create a table
    table = plt.table(cellText=df.values,
                      colLabels=df.columns,
                      cellLoc='center',
                      loc='center',
                      colLoc='center')

    # Adjust table properties
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(df.columns))))

    # Save as PNG
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()



