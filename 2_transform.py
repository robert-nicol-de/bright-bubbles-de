# 2_transform.py - Makes your data analytics-ready
import pandas as pd

# Load the raw data you just pulled
df = pd.read_csv("raw_youtube_data.csv")

# Convert published date to real date
df['published'] = pd.to_datetime(df['published'])

# Calculate Views Per Hour (VPH)
now = pd.Timestamp.now()
df['hours_since_upload'] = (now - df['published']).dt.total_seconds() / 3600
df['vph'] = df['views'] / df['hours_since_upload'].replace(0, 0.001)

# Calculate CTR Multiplier (how many times better than average)
avg_views = df['views'].mean()
df['ctr_multiplier'] = df['views'] / avg_views

# Sort by views (best first)
df = df.sort_values('views', ascending=False)

# Save as Parquet (Power BI loves this format)
df.to_parquet("gold_bright_bubbles.parquet", index=False)

print("Gold layer ready: gold_bright_bubbles.parquet")