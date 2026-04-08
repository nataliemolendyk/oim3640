import requests
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import math


nltk.download('stopwords')
nltk.download('vader_lexicon')
stop_words = set(stopwords.words('english'))
sia = SentimentIntensityAnalyzer()


GENIUS_TOKEN = "TRW-dAC0og-QhkoOyBtc7_ZnnJYyloVwWVNZQfeLm9uprzMaHgyg37WpKhMIn0xh"  # Replace with your Genius API token

songs = [
    {"title": "Die on This Hill", "artist": "Sienna Spiro", "year": 2025},
    {"title": "You Stole The Show", "artist": "Sienna Spiro", "year": 2025},
    {"title": "The Visitor", "artist": "Sienna Spiro", "year": 2026},
    {"title": "Maybe", "artist": "Sienna Spiro", "year": 2024},
    {"title": "Back to Blonde", "artist": "Sienna Spiro", "year": 2024},
]

headers = {"Authorization": f"Bearer {GENIUS_TOKEN}"}


def search_song(title, artist):
    url = "https://api.genius.com/search"
    params = {"q": f"{title} {artist}"}
    res = requests.get(url, params=params, headers=headers).json()
    hits = res["response"]["hits"]
    if hits:
        for hit in hits:
            if title.lower() in hit["result"]["title"].lower():
                return hit["result"]["url"]
        return hits[0]["result"]["url"]
    return None

def scrape_lyrics(song_url):
    page = requests.get(song_url)
    soup = BeautifulSoup(page.text, "html.parser")
    lyrics = ""
    divs = soup.find_all("div", {"data-lyrics-container": "true"})
    if divs:
        for div in divs:
            lyrics += div.get_text(" ")
    else:
        div = soup.find("div", class_="lyrics")
        if div:
            lyrics = div.get_text(" ")
    lyrics = lyrics.lower()
    if not lyrics.strip():
        print("Warning: Genius lyrics not found!")
    return lyrics

def fallback_lyrics(title, artist):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    try:
        res = requests.get(url).json()
        lyrics = res.get("lyrics", "")
        if not lyrics:
            print("Warning: Lyrics.ovh returned empty lyrics!")
        return lyrics.lower()
    except:
        print("Warning: Lyrics.ovh API failed!")
        return ""

def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

def calculate_emotions_vader(text):
    # VADER sentiment gives pos, neg, neu, compound scores
    scores = sia.polarity_scores(text)
    # Map scores to our five categories roughly
    # heartbreak -> negative
    # loneliness -> neutral but negative
    # regret -> negative
    # disappointment -> negative
    # grief -> negative
    
    emotions = {
        "heartbreak": round(scores['neg'] * 100, 2),
        "loneliness": round(scores['neu'] * 50, 2),  # neutral partly counts
        "regret": round(scores['neg'] * 100, 2),
        "disappointment": round(scores['neg'] * 100, 2),
        "grief": round(scores['neg'] * 100, 2)
    }
    return emotions

def dominant_emotion(emotions):
    return max(emotions, key=emotions.get)

def std_dev(values):
    mean = sum(values) / len(values)
    return math.sqrt(sum((v - mean) ** 2 for v in values) / len(values))

results = []
dominants = []

for song in songs:
    print(f"Processing: {song['title']}")
    url = search_song(song["title"], song["artist"])
    lyrics = ""
    if url:
        lyrics = scrape_lyrics(url)
    if not lyrics.strip():
        lyrics = fallback_lyrics(song["title"], song["artist"])
    if not lyrics.strip():
        print(f"Skipping {song['title']} because no lyrics found.\n")
        continue

    cleaned = clean_text(lyrics)
    emotions = calculate_emotions_vader(cleaned)
    dom = dominant_emotion(emotions)

    dominants.append(dom)
    results.append({
        "title": song["title"],
        "year": song["year"],
        **emotions,
        "dominant": dom
    })

print("\nComparison Table:\n")
print("Title | Year | heartbreak% | loneliness% | regret% | disappointment% | grief% | dominant")
print("-" * 95)
for r in results:
    print(f"{r['title']} | {r['year']} | {r['heartbreak']} | {r['loneliness']} | "
          f"{r['regret']} | {r['disappointment']} | {r['grief']} | {r['dominant']}")

from collections import Counter
count = Counter(dominants)
top_emotion, freq = count.most_common(1)[0]

values = [r[top_emotion] for r in results]
avg = sum(values) / len(values)
within_range = [abs(v - avg) <= 15 for v in values]

if freq >= 4 and all(within_range):
    print("\nConclusion: Themes are CONSISTENT")
else:
    print("\nConclusion: Themes have SHIFTED")

print("\nStandard Deviation per Song:")
for r in results:
    vals = [r[e] for e in ['heartbreak','loneliness','regret','disappointment','grief']]
    print(f"{r['title']}: {round(std_dev(vals), 2)}")