# Hacker News Top Stories Analyzer

A Python script that performs data analysis and sentiment analysis on the current top stories from Hacker News (news.ycombinator.com). This project demonstrates skills in working with APIs, data processing, and visualization.*THIS IS JUST A SAMPLE MODEL WITH NO CURRENT WORKING APPLICATION USEFUL ONLY AS A REFERENCE FOR KNOWN THINGS AND CONTAINS ONLY CODE ; FILES MUST BE CREATED ON OWN FOR THE USE OF CODE *

## 🚀 Features

*   **API Interaction:** Fetches real-time data from the official Hacker News API.
*   **Data Processing:** Cleans and processes story titles for analysis.
*   **Text Analysis:** Identifies the most common keywords in top story titles.
*   **Sentiment Analysis:** Uses the TextBlob library to determine the overall emotional tone (positive/negative/neutral) of the headlines.
*   **Data Visualization:** Generates informative plots:
    *   **Top Words Bar Chart:** Visualizes the most frequent words, filtering out common stop words.
    *   **Score Distribution Histogram:** Shows how upvotes are distributed across the top stories.

## 📊 Output Examples

The script generates and saves the following visualizations:
*   `assets/top_words.png` - A horizontal bar chart of the most common words.
*   `assets/score_histogram.png` - A histogram showing the distribution of story scores (upvotes).

## 🛠️ Technologies Used

*   **Python 3**
*   **Libraries:**
    *   `requests` - For making HTTP requests to the Hacker News API.
    *   `pandas` & `matplotlib`/`seaborn` - For data manipulation and creating visualizations.
    *   `TextBlob` - For performing simple sentiment analysis on text.
*   **RESTful API Consumption**

## 🔧 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone ](https://github.com/RIshi-Raj-noobie/Hacker-news-trend/tree/main)
    cd hacker-news-analysis
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

## 🚀 Usage

Run the analysis script from the command line:

```bash
python hn_analyzer.py
