"""
Hacker News Top Stories Analyzer
Author: Rishiraj Singh Tomar

This script fetches the top stories from Hacker News, analyzes trends in titles
(common words, sentiment), and creates visualizations.
"""

import requests
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from textblob import TextBlob
import pandas as pd
import time

# Configure styling for our plots
sns.set_style("whitegrid")
plt.rcParams['font.size'] = 10

def fetch_top_story_ids(limit=30):
    """
    Fetches the IDs of the top stories from the Hacker News API.
    """
    print("📡 Fetching top story IDs from Hacker News...")
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()
    return story_ids[:limit]  # Return only the top 'limit' stories

def fetch_story_details(story_id):
    """
    Fetches the full details (title, score, by, etc.) for a single story.
    """
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(story_url)
    # Add a small delay to be polite to the API
    time.sleep(0.1)
    return response.json()

def analyze_sentiment(text):
    """
    Performs sentiment analysis on a text string.
    Returns a polarity score between -1 (negative) and 1 (positive).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def plot_common_words(titles, num_words=15):
    """
    Generates a bar plot of the most common words in the story titles.
    """
    print("📊 Analyzing common words...")
    # Combine all titles into one string and split into words
    all_text = ' '.join(titles).lower()
    words = all_text.split()

    # Filter out common stop words and short words
    stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'is', 'with', 'by', 'this', 'that', 'from', 'it', 'as', 'are', 'be'}
    filtered_words = [word for word in words if word not in stop_words and len(word) > 3]

    # Count word frequency
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(num_words)

    # Create DataFrame for easy plotting
    words_df = pd.DataFrame(most_common_words, columns=['Word', 'Count'])

    # Plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Count', y='Word', data=words_df, palette="viridis")
    plt.title(f'Top {num_words} Most Common Words in Hacker News Titles')
    plt.tight_layout()
    plt.savefig('assets/top_words.png', dpi=100, bbox_inches='tight')
    print("💾 Saved plot: assets/top_words.png")
    plt.show()

def plot_score_distribution(stories):
    """
    Generates a histogram of the story scores.
    """
    print("📈 Analyzing score distribution...")
    scores = [story.get('score', 0) for story in stories]

    plt.figure(figsize=(10, 5))
    plt.hist(scores, bins=15, edgecolor='black', alpha=0.7, color='skyblue')
    plt.xlabel('Score (Upvotes)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Hacker News Story Scores')
    plt.grid(True, alpha=0.3)
    plt.savefig('assets/score_histogram.png', dpi=100, bbox_inches='tight')
    print("💾 Saved plot: assets/score_histogram.png")
    plt.show()

def main():
    """Main function to run the Hacker News analysis."""
    print("🚀 Starting Hacker News Top Stories Analysis\n")

    # Step 1: Fetch Data
    top_story_ids = fetch_top_story_ids(limit=40) # Get a few extra in case of errors
    stories = []

    print("🔍 Fetching details for each story...")
    for i, story_id in enumerate(top_story_ids, 1):
        try:
            story_data = fetch_story_details(story_id)
            # Only process stories with a title
            if story_data and 'title' in story_data:
                stories.append(story_data)
                print(f"   [{i}/{len(top_story_ids)}] Fetched: {story_data.get('title')[:50]}...")
            else:
                print(f"   Skipping story ID {story_id} (no title).")
        except requests.RequestException as e:
            print(f"   Error fetching story {story_id}: {e}")

    print(f"\n✅ Successfully fetched {len(stories)} stories.")

    # Step 2: Perform Analysis
    titles = [story['title'] for story in stories]

    # Perform sentiment analysis on each title
    for story in stories:
        story['sentiment'] = analyze_sentiment(story['title'])

    # Calculate average sentiment
    avg_sentiment = sum(story['sentiment'] for story in stories) / len(stories)
    print(f"\n😊 Average Sentiment of Titles: {avg_sentiment:.3f}")
    # Simple interpretation
    if avg_sentiment > 0.1:
        print("   Overall tone: Positive")
    elif avg_sentiment < -0.1:
        print("   Overall tone: Negative")
    else:
        print("   Overall tone: Neutral")

    # Find the highest scored article
    top_story = max(stories, key=lambda x: x.get('score', 0))
    print(f"\n🏆 Top Story: \"{top_story['title']}\"")
    print(f"   👍 Score: {top_story.get('score', 'N/A')} | 👤 By: {top_story.get('by', 'Unknown')}")

    # Step 3: Create Visualizations
    plot_common_words(titles)
    plot_score_distribution(stories)

    # (Optional) Save the data to a JSON file for later inspection
    import json
    with open('output/top_stories.json', 'w') as f:
        json.dump(stories, f, indent=4)
    print("\n💾 Raw data saved to: output/top_stories.json")

    print("\n🎉 Analysis complete!")

if __name__ == "__main__":
    main()