import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --------------------------------------------------------------
# Basic web search
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "web_search_preview",
        }
    ],
    input="What are the best restaurants around de Dam?",
)

print(response.output_text)

# --------------------------------------------------------------
# Basic web search with location
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "web_search_preview",
            "user_location": {
                "type": "approximate",
                "country": "NL",
                "city": "Amsterdam",
            },
        }
    ],
    input="What are the best restaurants around de Dam?",
)

print(response.output_text)
response.output[1].content[0].annotations
response.output[1].content[0].annotations[0].url
