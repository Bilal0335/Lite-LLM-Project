from dotenv import load_dotenv
import os
from litellm import completion

# Step 1: Load .env file
load_dotenv()

# Step 2: Get API keys
openai_key = os.getenv("OPENAI_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEYS")

# Step 3: Safe OpenAI function
def openai():
    try:
        response = completion(
            model="openai/gpt-4o",
            messages=[{
                'role': 'user',
                'content': 'Hello, How are You?'
            }],
            api_key=openai_key
        )
        print("OpenAI GPT-4o response:")
        print(response['choices'][0]['message']['content'])

    except Exception as e:
        print("❌ OpenAI Error:", e)

# Step 4: Gemini (this already works fine)
def gemini2():
    try:
        response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{
            "role": "user", 
            "content": "What is Gemini?"
        }],
        api_key=gemini_key
        )
        print("✅ Gemini 2.0 response:")
        print(response['choices'][0]['message']['content'])

    except Exception as e:
        print("❌ Gemini Error:", e)


# Step 5: Main
if __name__ == "__main__":
    gemini2()
    openai()
