# 1_ingest.py - Pulls your YouTube stats
import requests
import pandas as pd

# === YOUR SETTINGS (DO NOT CHANGE ANYTHING ELSE) ===
API_KEY = "AIzaSyCGf9igk6s5wu3gA8Oxgw8HDqxh1nlkA9w"   # Your key
CHANNEL_ID = "UCnN3bOvFoCZ4Zwzqe9Bt4Nw"              # Your channel ID
# ===================================================

url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "key": API_KEY,
    "channelId": CHANNEL_ID,
    "part": "snippet,id",
    "order": "date",
    "maxResults": 50
}

data = []
response = requests.get(url, params=params).json()

# Check for errors
if "error" in response:
    print("API Error:", response["error"]["message"])
    exit()

for item in response.get("items", []):
    if item["id"]["kind"] != "youtube#video":
        continue  # Skip non-video items

    video_id = item["id"]["videoId"]

    # Get view/like/comment counts
    stats_url = "https://www.googleapis.com/youtube/v3/videos"
    stats = requests.get(stats_url, params={
        "key": API_KEY,
        "id": video_id,
        "part": "statistics"
    }).json()

    if not stats.get("items"):
        continue

    stats = stats["items"][0]["statistics"]

    data.append({
        'title': item["snippet"]["title"],
        'published': item["snippet"]["publishedAt"][:10],  # YYYY-MM-DD
        'views': int(stats.get("viewCount", 0)),
        'likes': int(stats.get("likeCount", 0)),
        'comments': int(stats.get("commentCount", 0))
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("raw_youtube_data.csv", index=False)
print(f"Success: {len(df)} videos saved to raw_youtube_data.csv!")