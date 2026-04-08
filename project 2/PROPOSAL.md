## My Project Proposal

**What I'm building:** 
I am building a song lyrics analyzer that examines my top 5 favorite songs by Sienna Spiro to identify common emotional themes and determine if her lyrics consistently explore similar topics or if her themes have shifted over time.

**Why I chose this:** 
Sienna Spiro is my favorite artist, and while I notice all her songs feel sad, I want to understand if they're about the same emotional experiences or different ones. This analyzer will reveal thematic patterns and common threads across her work.

**Core features:** 
- Load 5 song text files by URL for API and scrapes the lyrics from a HTML
- Remove stopwords using NLTK (keep only meaningful words)
- Remove punctuation and splits text into words
- Use VADER sentiment analysis to assign scores for the emotional keywords in 5 categories: heartbreak, loneliness, regret, disappointment, grief
    - heartbreak, regret, disappointment, grief have negative sentiment scores, lonelines has neutral sentiment score
     - Negative (for each category) = (scores ranging from 0 to 1) x 100
     - Neutral (for each category) = (scores ranging from 0 to 1) x 50
- Generate a comparison table showing:
  - Song Title | Year | heartbreak% | loneliness% | regret% | 
  disappointment% | grief%
  - Print the table using print statements
  -Songs with Years:
    -Die on this Hill (2025)
    -You Stole the Show (2025)
    -The Visitor (2026)
    -Maybe (2025)
    -Back to Blonde (2024)
- Identify the dominant emotion for each song (the emotion that has the highest percentage in the comparison table)
- Compare average emotion profiles across all 5 songs to determine theme consistency
    - Count how many times each dominant emotion appears
    - Get the most frequent dominant emotion in the songs
    - If 4 songs contain the top emotion, the themes acros songs will be consistent otherwise the themes have shifted
- Find the standard deviation of each song
    - Low values means that the song's emotions are consistent or around the same level
    - High values means that the song's emotions have a mix of emotions/emotional tones.

**What I don't know yet:** 
- Exact year/release date for each song (Researched)
- Best method to manually define emotional keywords per category