import openai

# Set your OpenAI API key
openai.api_key = ''

# Function to interactively ask queries and get responses
def interact_with_chatbot():
    query_after = input("Enter your query: ")

    response_after = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": query_after}],
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None
    )

    print("Response:", response_after.choices[0].message['content'])

# Interact with the chatbot after loading the fine-tuned model
interact_with_chatbot()
