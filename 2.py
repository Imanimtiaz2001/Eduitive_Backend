import openai
import docx

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
        n=2,
        stop=None
    )

    print("Response:", response_after.choices[0].message['content'])

# Function to read training data from a Word document
def read_training_data_from_docx(file_path):
    doc = docx.Document(file_path)
    training_data = []

    for paragraph in doc.paragraphs:
        training_data.append({"role": "user", "content": paragraph.text})

    return training_data

# Read training data from the Word document
training_data = read_training_data_from_docx("Computer 6 SNC 2023-24 - Punjab.docx")

# Fine-tune the model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=training_data,
    max_tokens=100,
    temperature=0.9,
    n=1,
    stop=None
)

# Save the fine-tuned model
with open("fine_tuned_model.json", "w") as f:
    f.write(response['model'])

# Interact with the chatbot after fine-tuning
interact_with_chatbot()
