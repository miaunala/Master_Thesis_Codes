library(dplyr)
library(readr)
library(gridExtra)
library(ggplot2)

base_small <- "C:/Users/.../my_and_gpt_annot/"
base_big <- "C:/Users/.../gpt_hatestoxicspeech/"

covid_small_round1 <- read_csv(file.path(base_small, "sample_covid_gpt_annot.csv"))
farmer_small_round1 <- read_csv(file.path(base_small, "sample_farmer_gpt_annot.csv"))

covid_small_round2 <- read_csv(file.path(base_small, "sample_covid_gpt_annot_v2.csv"))
farmer_small_round2 <- read_csv(file.path(base_small, "sample_farmer_gpt_annot_v2.csv"))

covid_big <- read_csv(file.path(base_big, "sample_covid_gpt_annot_BIG.csv"))
farmer_big <- read_csv(file.path(base_big, "sample_farmer_gpt_annot_BIG.csv"))



# go back to right file location
setwd(base_small)


# Small

# Covid

# Covid Small Round 1 My annotations

filtered_covdf_small_r1_mine <- covid_small_round1 %>%
  filter(covid_small_round1$`Toxicity/Hatespeech/None` %in% c("Toxicity", "Hate Speech"))

count_authors_covdf_small_r1 <- filtered_covdf_small_r1_mine %>%
  group_by(filtered_covdf_small_r1_mine$sender) %>%
  summarise(count = n(), .groups="drop")

# tableGrob suggested by GPT
table_count_authors_covdf_small_r1 <- tableGrob(count_authors_covdf_small_r1)

# Save the table as a PNG
output_file <- "count_authors_covdf_small_r1.png"
ggsave(output_file, plot = table_count_authors_covdf_small_r1, width = 6, height = 10, dpi = 300)



# Covid Small Round 2 My annotations

filtered_covdf_small_r2_mine <- covid_small_round2 %>%
  filter(covid_small_round2$`Toxicity/Hatespeech/None` %in% c("Toxicity", "Hate Speech"))

count_authors_covdf_small_r2 <- filtered_covdf_small_r2_mine %>%
  group_by(filtered_covdf_small_r2_mine$sender) %>%
  summarise(count = n(), .groups="drop")

table_count_authors_covdf_small_r2 <- tableGrob(count_authors_covdf_small_r2)

# Save the table as a PNG
output_file <- "count_authors_covdf_small_r2.png"
ggsave(output_file, plot = table_count_authors_covdf_small_r2, width = 6, height = 10, dpi = 300)



# Farmer

# Farmer Small Round 1 My annotations

filtered_farmdf_small_r1_mine <- farmer_small_round1 %>%
  filter(farmer_small_round1$`Toxicity/Hatespeech/None` %in% c("Toxicity", "Hate Speech"))

count_authors_farmdf_small_r1 <- filtered_farmdf_small_r1_mine %>%
  group_by(filtered_farmdf_small_r1_mine$sender) %>%
  summarise(count = n(), .groups="drop")

table_count_authors_farmdf_small_r1 <- tableGrob(count_authors_farmdf_small_r1)

# Save the table as a PNG
output_file <- "count_authors_farmdf_small_r1.png"
ggsave(output_file, plot = table_count_authors_farmdf_small_r1, width = 6, height = 12, dpi = 300)



# Farmer Small Round 2 My annotations

filtered_farmdf_small_r2_mine <- farmer_small_round2 %>%
  filter(farmer_small_round2$`Toxicity/Hatespeech/None` %in% c("Toxicity", "Hate Speech"))

count_authors_farmdf_small_r2 <- filtered_farmdf_small_r2_mine %>%
  group_by(filtered_farmdf_small_r2_mine$sender) %>%
  summarise(count = n(), .groups="drop")

table_count_authors_farmdf_small_r2 <- tableGrob(count_authors_farmdf_small_r2)

# Save the table as a PNG
output_file <- "count_authors_farmdf_small_r2.png"
ggsave(output_file, plot = table_count_authors_farmdf_small_r2, width = 6, height = 12, dpi = 300)



# BIG

# Covid
filtered_covdf_big_3_5 <- covid_big %>%
  filter(covid_big$`Label 3.5 turbo` %in% c("Toxicity", "Hate Speech"))

count_authors_covdf_big <- filtered_covdf_big_3_5 %>%
  group_by(filtered_covdf_big_3_5$sender) %>%
  summarise(count = n(), .groups="drop") %>%
  filter(count >= 10)

table_count_authors_covdf_big <- tableGrob(count_authors_covdf_big)

# Save the table as a PNG
output_file <- "count_authors_covdf_big.png"
ggsave(output_file, plot = table_count_authors_covdf_big, width = 6, height = 30, dpi = 300)


# Farmer
filtered_farmdf_big_3_5 <- farmer_big %>%
  filter(farmer_big$`Label 3.5 turbo` %in% c("Toxicity", "Hate Speech"))

count_authors_farmdf_big <- filtered_farmdf_big_3_5 %>%
  group_by(filtered_farmdf_big_3_5$sender) %>%
  summarise(count = n(), .groups="drop") %>%
  filter(count >= 10)

table_count_authors_farmdf_big <- tableGrob(count_authors_farmdf_big)

# Save the table as a PNG
output_file <- "count_authors_farmdf_big.pdf"
ggsave(output_file, plot = table_count_authors_farmdf_big, width = 6, height = 43, dpi = 300)

