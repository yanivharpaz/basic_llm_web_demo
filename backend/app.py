from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
from vector_store import VectorStore

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv('OPENAI_API_KEY')
vector_store = VectorStore()

# Initialize with some example texts
example_texts = [
    "Insurance policies provide financial protection against various risks.",
    "Life insurance helps protect your family's financial future.",
    "Health insurance covers medical expenses and healthcare costs.",
    "Property insurance protects against damage to physical assets.",
    "Auto insurance provides coverage for vehicle-related incidents."
]
vector_store.add_texts(example_texts)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message')
        
        # Retrieve relevant context using FAISS
        relevant_texts = vector_store.search(message)
        context = "\n".join(relevant_texts)
        
        # Create the prompt with context
        prompt = f"""Context information: {context}

User question: {message}

Please provide a response based on the context information if relevant. If the context isn't relevant, you can respond based on your general knowledge."""

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a chatbot based on GPT-4o with access to specific insurance-related information."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return jsonify({
            "response": response.choices[0].message.content,
            "context_used": relevant_texts  # Optional: return the used context for transparency
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/add-text', methods=['POST'])
def add_text():
    try:
        data = request.json
        texts = data.get('texts', [])
        
        vector_store.add_texts(texts)
        return jsonify({"message": "Texts added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
