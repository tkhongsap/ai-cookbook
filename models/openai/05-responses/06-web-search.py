import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ANSI color codes
BLUE = "\033[94m"
PINK = "\033[95m"
RESET = "\033[0m"

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
    input="what are the top 3 Michelin starred restaurants around Bangkok? Tell me the name, rating and a bit about the restaurant.",
)

print(f"{BLUE}=== BASIC WEB SEARCH RESULTS ==={RESET}")
print(f"{BLUE}{response.output_text}{RESET}")

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
                "country": "TH",
                "city": "Bangkok",
            },
        }
    ],
    input="what are the top 3 Michelin starred restaurants around Bangkok? Tell me the name, rating and a bit about the restaurant.",
)

print(f"{PINK}=== WEB SEARCH WITH LOCATION RESULTS ==={RESET}")
print(f"{PINK}{response.output_text}{RESET}")
# response.output[1].content[0].annotations
# response.output[1].content[0].annotations[0].url
