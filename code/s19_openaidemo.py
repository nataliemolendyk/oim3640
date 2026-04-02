from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

# response = client.responses.create(
#    model="gpt-5-nano", input="Write a one-sentence bedtime story about a unicorn."
# )
# print(response.output_text)


# Can you modify the code to ask the user for a topic and generate a story about that topic? (Hint: you can use input() function to get user input)
# topic = input("Enter a topic for the bedtime story: ")
# response = client.responses.create(
#    model="gpt-5-nano", input=f"Write a one-sentence bedtime story about {topic}."
# )
#print(response.output_text)

# or a real chatbot, talking back and forth with the user.
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = client.responses.create(
        model="gpt-5-nano", input=f"You: {user_input}\nAI:"
    )
    print(f"AI: {response.output_text}") 