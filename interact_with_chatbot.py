# app.py

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

# Function to interactively ask queries and get responses
def interact_with_chatbot(query):
    response_after = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": query}],
        max_tokens=500,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response_after.choices[0].message['content']

@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    data = request.json
    user_query = data.get('query')
    response = interact_with_chatbot(user_query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0' )
