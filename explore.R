library("data.table")
library("ggplot2")

dt <- fread("/Users/stephaniedodd/Downloads/revelio_user_pos_fortune500US_7.csv")
dt <- dt[, !duplicated(names(dt)), with = FALSE]


## histogram of prob of being female (bin 0.01)
hist <- ggplot(as.data.frame(dt), aes(x=f_prob)) + 
  geom_histogram(binwidth = 0.01, fill = "deeppink3", color = "black") +
  labs(title = "Histogram of f_prob",
       x = "Probability Female",
       y = "Frequency") + 
  theme_classic()

## CDF of probability of being female (mark classification threshold)
# extract cumulative density up to threshold 
gender_thresh <- dt[, mean(m_prob < 0.50)] # get cumulative density at threshold 
cdf <- ggplot(as.data.frame(dt), aes(x = m_prob)) +
  stat_ecdf(geom = "step", color="deeppink3") +
  annotate("point", x = 0.5, y = gender_thresh, color = "black", size = 3) + 
  annotate("text", x = 0.5, y = gender_thresh, 
           label = paste0("Prop. classified as \n female = ", round(gender_thresh, 3)), 
           vjust = -1, color = "black") +
  labs(title = "CDF of Probability Female",
       x = "Probability Female",
       y = "Cumulative Probability") + 
  theme_classic()


# Binarize gender at 50% threshold
dt[, f_bin := as.integer(f_prob > 0.5)]   # mean(f_bin) = gender_thresh 
