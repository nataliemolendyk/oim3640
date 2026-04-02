## My Project Proposal

**What I'm building:** 
I am building a song lyrics analyzer that examines my top 5 favorite songs by Sienna Spiro to identify common emotional themes and determine if her lyrics consistently explore similar topics or if her themes have shifted over time.

**Why I chose this:** 
Sienna Spiro is my favorite artist, and while I notice all her songs feel sad, I want to understand if they're about the same emotional experiences or different ones. This analyzer will reveal thematic patterns and common threads across her work.

**Core features:** 
- Load 5 pre-saved song lyric text files (read URL files from GeniusLyrics)
- Remove stopwords using NLTK (keep only meaningful words)
- Remove punctuation and duplicates of words
- Count emotional keywords in 5 categories: heartbreak, loneliness, regret, disappointment, grief
    - Definitions:
        - heartbreak: misery, heartache, sorrow, devastation
        - loneliness: isolation, longing, distress, alienation
        - regret: remorse, compunction, rue, misgiving
        - disappointment: letdown, unhappiness, frustration, disillusionment
        - grief: anguish, disbelievement, guilt, anger
    - Percentage calculation: for each category, percentage = (number of matching keywords / total meaningful words after stopword removal) * 100
        - Matching keywords means the words are the exact same
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
    - If 4+ songs share the same dominant emotion (±15% variance), conclude that themes are consistent. Otherwise, themes have shifted.
        - 15 variance means that the dominant emotion's percentage must be within 15% of the group's average
    - Variance measurement: the standard deviation of the percentages across the 5 emotion categories for each song

**What I don't know yet:** 
- Exact year/release date for each song (Researched)
- Best method to manually define emotional keywords per category