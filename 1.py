
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Function to interactively ask queries and get responses
def interact_with_chatbot():
   

    print("\nAfter Fine-Tuning:")
    query_after = input("Enter your query: ")

    response_after = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": query_after}],
        max_tokens=500,
        temperature=0,
        n=1,
        stop=None
    )

    print("Response:", response_after.choices[0].message['content'])

# Define your fine-tuning data
training_data = [
    {"role": "system", "content": "Relationship of biology to other sciences."},
    {"role": "user", "content": "The interrelationship among different branches of science cannot be denied. Biology includes information on various aspects of living things but these information relate to the other branches of science as well. Each branch of science has relationship with all other branches. For example, when studying the process of movement in animals, the biologists have to refer to the laws of motion in physics. This forms the basis of interdisciplinary sciences (Figure 1.1).Biophysics:It deals with the study of the principles of physics, which are applicable to biological phenomena. For example there is a similarity between the working principles of lever in physics and limbs of animals in biology.Biochemistry: It deals with the study of the chemistry of different compounds and processes occurring in living organisms. For example the study of basic metabolism of photosynthesis and respiration involves the knowledge of chemistry.Biomathematics / Biometry: It deals with the study of biological processes using mathematical techniques and tools. For example to analyze the data gathered after experimental work, biologists have to apply the rules of mathematics.Biogeography: It deals with study of the occurrence and distribution of different species of living organisms in different geographical regions of the world. It applies the knowledge of the characteristics of particular geographical regions to determine the characteristics of living organisms found there.Bioeconomics:It deals with the study of organisms from economical point of view. For example the cost value and profit value of the yield of wheat can be calculated through bioeconomics and benefits or losses can be determined."},
     {"role": "system", "content": "Categories of Application software?"},
    {"role": "user", "content": "•	Custom-built software: This is the software that is designed and developed for particular customer. •	Packaged software: This software is a kind of off-the-shelf program or components. developed for sale to the potential software developer/users for their use. The examples are: MS-Word, MS-power point. personal Oracle etc. "},
     # Add more examples as needed
]

# Fine-tune the model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=training_data,
    max_tokens=100,
    temperature=0,
    n=1,
    stop=None
)

# Save the fine-tuned model
with open("fine_tuned_model.json", "w") as f:
    f.write(response['model'])

# Interact with the chatbot before and after fine-tuning
interact_with_chatbot()
