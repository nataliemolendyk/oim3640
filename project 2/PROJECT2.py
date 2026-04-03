import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import statistics
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

songs = [
    {"title": "Die on this Hill", "url": "https://genius.com/Sienna-spiro-die-on-this-hill-lyrics", "year": 2025},
    {"title": "You Stole the Show", "url": "https://genius.com/Sienna-spiro-you-stole-the-show-lyrics", "year": 2025},
    {"title": "Maybe", "url": "https://genius.com/Sienna-spiro-maybe-lyrics", "year": 2025},
    {"title": "Back to Blonde", "url": "https://genius.com/Sienna-spiro-back-to-blonde-lyrics", "year": 2024},
    {"title": "The Visitor", "url": "https://genius.com/Sienna-spiro-the-visitor-lyrics", "year": 2026},
]

categories = {
    "Heartbreak": ["misery", "heartache", "sorrow", "devastation"],
    "Loneliness": ["isolation", "longing", "distress", "alienation"],
    "Regret": ["remorse", "compunction", "rue", "misgiving"],
    "Disappointment": ["letdown", "unhappiness", "frustration", "disillusionment"],
    "Grief": ["anguish", "disbelievement", "guilt", "anger"]
}

def process_text(text):
    # Tokenize
    tokens = word_tokenize(text.lower())
    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Remove duplicates
    tokens = list(set(tokens))
    return tokens

results = []
all_percentages = []

for song in songs:
    response = requests.get(song['url'])
    text = response.text
    processed = process_text(text)
    total_words = len(processed)
    emotion_counts = {}
    for cat, keywords in categories.items():
        count = sum(processed.count(kw) for kw in keywords)
        emotion_counts[cat] = count
        percentage = (count / total_words * 100) if total_words > 0 else 0
        all_percentages.append(percentage)
    # Find dominant
    dominant = max(emotion_counts, key=emotion_counts.get)
    results.append({
        'title': song['title'],
        'year': song['year'],
        'percentages': {cat: (emotion_counts[cat] / total_words * 100) if total_words > 0 else 0 for cat in categories},
        'dominant': dominant
    })

# Output table
print("Song Title\tYear\tHeartbreak%\tLoneliness%\tRegret%\tDisappointment%\tGrief%\tDominant")
for res in results:
    p = res['percentages']
    print(f"{res['title']}\t{res['year']}\t{p['Heartbreak']:.2f}\t{p['Loneliness']:.2f}\t{p['Regret']:.2f}\t{p['Disappointment']:.2f}\t{p['Grief']:.2f}\t{res['dominant']}")

# Consistency
dominants = [r['dominant'] for r in results]
most_common = Counter(dominants).most_common(1)[0]
if most_common[1] >= 4:
    std_dev = statistics.stdev(all_percentages) if len(all_percentages) > 1 else 0
    if std_dev <= 15:
        print("Themes are consistent.")
    else:
        print("Themes have shifted.")
else:
    print("Themes have shifted.")