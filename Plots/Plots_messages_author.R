library("dplyr")
library("ggplot2")
library("ggExtra")
library("readr")

setwd("C:/Users/.../gpt_hatestoxicspeech")

# Plots for data section 

# Read in datasets

# Original dataset
covid_orig <- read_csv("corona_comments_na_rem.csv")
farmer_orig <- read_csv("farmerprotest_comments_na_rem.csv")

# Subsample small
covid_sub_small <- read_csv("sample_covid.csv")
farmer_sub_small <- read_csv("sample_farmer.csv")

# Subsample big
covid_sub_big <- read_csv("sample_covid_big.csv")
farmer_sub_big <- read_csv("sample_farmer_big.csv")



### Original Sample


# Post count for Covidskeptics & Farmer Protests; top 3 & bottom 3
# Covidskeptics
pst_cnt_covid <- covid_orig %>%
  count(channel_name, name = "post_count") %>%
  arrange(desc(post_count))

top_bottom_channels_covid <- pst_cnt_covid %>%
  slice_head(n = 3) %>%
  bind_rows(slice_tail(pst_cnt_covid, n = 3))

# Farmer Protest
pst_cnt_farmer <- farmer_orig %>%
  count(channel_name, name = "post_count") %>%
  arrange(desc(post_count))

top_bottom_channels_farmer <- pst_cnt_farmer %>%
  slice_head(n = 3) %>%
  bind_rows(slice_tail(pst_cnt_farmer, n = 3))





# Bar plot for top and bottom 3 channels

# Covid
# Calculate  median
median_posts <- median(pst_cnt_covid$post_count)

# Plot of top 3 & bottom 3 accounts + median
cov_orig_3bot3top <- ggplot(top_bottom_channels_covid, aes(x = reorder(channel_name, -post_count), y = post_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_hline(yintercept = median_posts, linetype = "dashed", color = "red", size = 0.8) +
  geom_text(aes(label = post_count), vjust = -0.5, size = 3, fontface = "bold") +
  labs(
    title = "Top 3 and Bottom 3 Covidskeptics Channels by Number of Posts",
    subtitle = paste("Median number of posts:", median_posts),
    x = "Channel Name",
    y = "Number of Posts"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("orig_top3bot3_covid.jpg", plot= cov_orig_3bot3top, bg = "white")


# Farmer
# Calculate  median
median_posts <- median(pst_cnt_farmer$post_count)

# Plot of top 3 & bottom 3 accounts + median
far_orig_3bot3top <- ggplot(top_bottom_channels_farmer, aes(x = reorder(channel_name, -post_count), y = post_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_hline(yintercept = median_posts, linetype = "dashed", color = "red", size = 0.8) +
  geom_text(aes(label = post_count), vjust = -0.5, size = 3, fontface = "bold") + 
  labs(
    title = "Top 3 and Bottom 3 Farmer Protest Channels by Number of Posts",
    subtitle = paste("Median number of posts:", median_posts),
    x = "Channel Name",
    y = "Number of Posts"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("orig_top3bot3_farmer.jpg", plot= far_orig_3bot3top, bg = "white")




### Sub sample 500


# Covidskeptics
pst_cnt_covid_sub500 <- covid_sub_small %>%
  count(channel_name, name = "post_count") %>%
  arrange(desc(post_count))

top_bottom_channels_covid_sub500 <- pst_cnt_covid_sub500 %>%
  slice_head(n = 3) %>%
  bind_rows(slice_tail(pst_cnt_covid_sub500, n = 3))


median_posts <- median(pst_cnt_covid_sub500$post_count)

# Plot of top 3 & bottom 3 accounts + median
cov_sub500_3bot3top <- ggplot(top_bottom_channels_covid_sub500, aes(x = reorder(channel_name, -post_count), y = post_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_hline(yintercept = median_posts, linetype = "dashed", color = "red", size = 0.8) +
  geom_text(aes(label = post_count), vjust = -0.5, size = 3, fontface = "bold") + 
  labs(
    title = "Top 3 and Bottom 3 Covidskeptics Channels in small subsample by Number of Posts",
    subtitle = paste("Median number of posts:", median_posts),
    x = "Channel Name",
    y = "Number of Posts"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("sub500_top3bot3_covid.jpg", plot= cov_sub500_3bot3top, bg = "white")



# Farmer Protests
pst_cnt_farmer_sub500 <- farmer_sub_small %>%
  count(channel_name, name = "post_count") %>%
  arrange(desc(post_count))

top_bottom_channels_farmer_sub500 <- pst_cnt_farmer_sub500 %>%
  slice_head(n = 3) %>%
  bind_rows(slice_tail(pst_cnt_farmer_sub500, n = 3))

median_posts <- median(pst_cnt_farmer_sub500$post_count)

# Plot of top 3 & bottom 3 accounts + median
far_sub500_3bot3top <- ggplot(top_bottom_channels_farmer_sub500, aes(x = reorder(channel_name, -post_count), y = post_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_hline(yintercept = median_posts, linetype = "dashed", color = "red", size = 0.8) +
  geom_text(aes(label = post_count), vjust = -0.5, size = 3, fontface = "bold") + 
  labs(
    title = "Top 3 and Bottom 3 Farmer Protest Channels in small subsample by Number of Posts",
    subtitle = paste("Median number of posts:", median_posts),
    x = "Channel Name",
    y = "Number of Posts"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("sub500_top3bot3_farmer.jpg", plot= far_sub500_3bot3top, bg = "white")




### Sub sample 25000

# Covidskeptics
pst_cnt_covid_sub25000 <- covid_sub_big %>%
  count(channel_name, name = "post_count") %>%
  arrange(desc(post_count))

top_bottom_channels_covid_sub25000 <- pst_cnt_covid_sub25000 %>%
  slice_head(n = 3) %>%
  bind_rows(slice_tail(pst_cnt_covid_sub25000, n = 3))


median_posts <- median(pst_cnt_covid_sub25000$post_count)

# Plot of top 3 & bottom 3 accounts + median
cov_sub25000_3bot3top <- ggplot(top_bottom_channels_covid_sub25000, aes(x = reorder(channel_name, -post_count), y = post_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_hline(yintercept = median_posts, linetype = "dashed", color = "red", size = 0.8) +
  geom_text(aes(label = post_count), vjust = -0.5, size = 3, fontface = "bold") + 
  labs(
    title = "Top 3 and Bottom 3 Covidskeptics Channels in large subsample by Number of Posts",
    subtitle = paste("Median number of posts:", median_posts),
    x = "Channel Name",
    y = "Number of Posts"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

cov_sub25000_3bot3top
ggsave("sub25000_top3bot3_covid.jpg", plot= cov_sub25000_3bot3top, bg = "white")



# Farmer Protests
pst_cnt_farmer_sub25000 <- farmer_sub_big %>%
  count(channel_name, name = "post_count") %>%
  arrange(desc(post_count))

top_bottom_channels_farmer_sub25000 <- pst_cnt_farmer_sub25000 %>%
  slice_head(n = 3) %>%
  bind_rows(slice_tail(pst_cnt_farmer_sub25000, n = 3))

median_posts <- median(pst_cnt_farmer_sub25000$post_count)

# Plot of top 3 & bottom 3 accounts + median
far_sub25000_3bot3top <- ggplot(top_bottom_channels_farmer_sub25000, aes(x = reorder(channel_name, -post_count), y = post_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_hline(yintercept = median_posts, linetype = "dashed", color = "red", size = 0.8) +
  geom_text(aes(label = post_count), vjust = -0.5, size = 3, fontface = "bold") + 
  labs(
    title = "Top 3 and Bottom 3 Farmer Protest Channels in large subsample by Number of Posts",
    subtitle = paste("Median number of posts:", median_posts),
    x = "Channel Name",
    y = "Number of Posts"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

far_sub25000_3bot3top
ggsave("sub25000_top3bot3_farmer.jpg", plot= far_sub25000_3bot3top, bg = "white")


