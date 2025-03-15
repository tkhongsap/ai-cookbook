import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

"""
Model spec: https://model-spec.openai.com/2025-02-12.html
Dashboard: https://platform.openai.com/logs?api=responses
"""

# --------------------------------------------------------------
# Introducing instructions
# --------------------------------------------------------------

"""
Inputs can now be a single string or a list of messages.

The list of roles can now be:
- system
- developer
- user
- assistant
"""

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)

print(response.output_text)


# --------------------------------------------------------------
# Which would be similar to:
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)

# --------------------------------------------------------------
# The chain of command (hierarchical instructions)
# --------------------------------------------------------------

"""
https://model-spec.openai.com/2025-02-12.html#chain_of_command
"""

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "Talk like a pirate."},
        {"role": "developer", "content": "don't talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)  # talks like a pirate

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "Don't talk like a pirate."},
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)  # doesn't talk like a pirate
