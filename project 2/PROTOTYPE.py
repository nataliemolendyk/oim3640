import requests

response = requests.get("https://genius.com/Sienna-spiro-die-on-this-hill-lyrics")
response2 = requests.get("https://genius.com/Sienna-spiro-you-stole-the-show-lyrics")
response3 = requests.get("https://genius.com/Sienna-spiro-maybe-lyrics")
response4 = requests.get("https://genius.com/Sienna-spiro-back-to-blonde-lyrics")
response5 = requests.get("https://genius.com/Sienna-spiro-the-visitor-lyrics")
reader = response.text + response2.text + response3.text + response4.text + response5.text

def count_keywords(reader):
    keywords = ["heartbreak", "loneliness", "regret", "disappointment", "grief"]
    count = 0
    for keyword in keywords:
        if keyword in reader.lower():
            count += reader.lower().count(keyword)
    return count

keyword_count = count_keywords(reader)
print(f"Total keyword count: {keyword_count}")