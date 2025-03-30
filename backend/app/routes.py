from flask import request, jsonify
from . import app
from openai import OpenAI
import os
from dotenv import load_dotenv

# Force reload environment variables
load_dotenv(override=True)

# Get the API key more explicitly
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Warning: OPENAI_API_KEY environment variable not found!")
else:
    # Print first 10 characters of API key for debugging
    print(f"API Key found: {api_key[:10]}...")

# Set up the OpenAI client
client = OpenAI(api_key=api_key)

def process_code_with_openai(code, action):
    """
    Process the given code using OpenAI's Chat API based on the specified action.

    :param code: The code snippet to process.
    :param action: The action to perform (e.g., 'refactor', 'docstring', 'tests').
    :return: The processed code as a string.
    """
    # Define the system prompt
    system_prompt = "You are a senior software engineer who helps developers improve code."

    # Define the user prompt based on the action
    action_prompts = {
        "refactor": "Refactor the following code for clarity, performance, and maintainability:",
        "docstring": "Add docstrings and comments to the following code:",
        "tests": "Generate unit tests for the following code:"
    }
    user_prompt = action_prompts.get(action, "Refactor the following code:")

    # Create the chat completion request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{user_prompt}\n\n{code}"}
        ],
        max_tokens=150,
        temperature=0.5,
    )

    # Extract and return the response content
    return response.choices[0].message.content.strip()

@app.route('/refactor', methods=['POST'])
def refactor_code():
    """
    Refactor the provided code using OpenAI's API.

    Expects a JSON body with 'code' and 'action'.
    Returns a JSON response with the refactored code.
    """
    data = request.json
    code = data.get('code')
    action = data.get('action', 'refactor')

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    try:
        result = process_code_with_openai(code, action)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/doc', methods=['POST'])
def generate_docstrings():
    # Placeholder for docstring generation logic
    code = request.json.get('code')
    # TODO: Insert GPT logic here
    return jsonify({'message': 'Docstring generation endpoint hit', 'code': code})

@app.route('/test', methods=['POST'])
def write_unit_tests():
    # Placeholder for unit test writing logic
    code = request.json.get('code')
    # TODO: Insert GPT logic here
    return jsonify({'message': 'Unit test endpoint hit', 'code': code})

@app.route('/')
def home():
    return jsonify({"message": "AI Dev Lab backend is running."}) 