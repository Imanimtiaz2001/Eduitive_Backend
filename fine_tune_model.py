import openai
import docx

# Set your OpenAI API key
openai.api_key = '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'

# Function to read training data from a Word document
def read_training_data_from_docx(file_path):
    doc = docx.Document(file_path)
    training_data = []

    for paragraph in doc.paragraphs:
        training_data.append({"role": "user", "content": paragraph.text})

    return training_data

# Read training data from the Word document
training_data = read_training_data_from_docx("Chemistry-12-chp-8-chp-15-(p-1).docx")

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
