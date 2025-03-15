import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file
load_dotenv()

# Initialize the client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to simulate sending an email (for testing purposes)
def send_email(to, subject, body):
    try:
        # In a real implementation, we would use SMTP to send the email
        # But for testing, we'll just print the email details
        print("\n----- EMAIL WOULD BE SENT -----")
        print(f"To: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        print("----- END OF EMAIL -----\n")
        
        print(f"Email simulation successful for {to}")
        return True
    except Exception as e:
        print(f"Error in email simulation: {str(e)}")
        return False

tools = [
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email to a given recipient with a subject and message.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "The recipient email address."},
                "subject": {"type": "string", "description": "Email subject line."},
                "body": {"type": "string", "description": "Body of the email message."},
            },
            "required": ["to", "subject", "body"],
            "additionalProperties": False,
        },
    }
]

# Using the Responses API
response = client.responses.create(
    model="gpt-4o-mini",
    input="Can you send an email to 'ta.khongsap@gmail.com' saying hi? with subject 'Hello' and body 'This is a test email.'",
    tools=tools,
)

# Print the text response
print("Text response:", response.output_text)

# Process function calls in the response.output list
print("\nChecking for function calls...")
if hasattr(response, 'output') and response.output:
    for item in response.output:
        print(f"Output item type: {type(item)}")
        
        # Check if this is a function call
        if hasattr(item, 'type') and item.type == 'function_call':
            print(f"Function call found: {item.name}")
            
            # Check if it's the send_email function
            if item.name == "send_email":
                # Parse the arguments (which is a JSON string)
                try:
                    args = json.loads(item.arguments)
                    print(f"Function arguments: {args}")
                    
                    # Call the actual function
                    send_email(
                        to=args.get("to"),
                        subject=args.get("subject"),
                        body=args.get("body")
                    )
                    print(f"Executed function: {item.name}")
                except Exception as e:
                    print(f"Error parsing arguments: {str(e)}")
else:
    print("No output items found in the response")

