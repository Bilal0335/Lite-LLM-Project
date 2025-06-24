from dotenv import load_dotenv
import os
from litellm import completion

# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Get the API key from environment
api_key = os.getenv("GEMINI_API_KEYS")

# Step 3: Set your question
prompt = "Who is the founder of Pakistan?"

# Step 4: Call the Gemini model
try:
    response = completion(
    model="gemini/gemini-2.0-flash",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    api_key=api_key
    )

    # Step 5: Print the response
    print("🤖 Gemini says:")
    print(response['choices'][0]['message']['content'])

except Exception as e:
    print("❌ Gemini Error:", e)