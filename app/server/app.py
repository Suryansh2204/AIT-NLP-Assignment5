from flask import Flask,request,jsonify
from flask_cors import CORS
import torch
from transformers import (
    AutoModelForCausalLM, 
    AutoTokenizer
)


app=Flask(__name__)

# Enable CORS
CORS(app,resources={r"/*": {"origins": "http://localhost:3000"}})

# Load the model from hugging face
model_name = "Suryansh-bit/a5-dpo-st124997"  

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

model.to(torch.device('cpu'))

@app.route('/predict-next', methods=['GET'])
def predict():
    try:
        prompt =  request.args.get('prompt') 
        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt").to(torch.device('cpu'))

        with torch.no_grad():
            output = model.generate(**inputs, max_length=100)

        # Decode and print output
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return jsonify({'genText': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/', methods=['GET'])
def call():
    return jsonify({'Name':"Suryansh Srivastava", 'ID':124997,'proglib':'NLP Assignment 5'})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)