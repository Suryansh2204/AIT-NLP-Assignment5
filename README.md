# 📜 Textpectations Reloaded - Preference Optimization with GPT-2

This project fine-tunes a GPT-2 model using Direct Preference Optimization (DPO) on the Anthropic/hh-rlhf dataset. The trained model is uploaded to Hugging Face and is fetched in a Flask API to generate responses based on user input.

<hr>

## 🚀 **Features**

- 🖥️ **Frontend:** A React-based UI where users enter a phrase and specify the sequence length for text generation.<br>

- 🧠 **Backend:** A Flask-based API that processes the input, loads an LSTM language model, and generates text.<br>

- 📖 **Model:** GPT-2 fine-tuning with DPO – Optimized for human preference alignment.<br>

- ✅ **Pretrained Tokenizer & Model** – Uses transformers from Hugging Face.<br>

- ✅ **Hugging Face Integration** – Automatically loads Suryansh-bit/a5-dpo-st124997.<br>

<hr>

## 🎥 App Demo

![Recording2025-03-02134947-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/a4bc5094-328c-4b68-a646-d1c4eeaa7643)

<hr>

The structure is organized as follows:

```
AIT-NLP-Assignment5/
│── app/
│   ├── client/   # React frontend
│   │   ├── Dockerfile
│   │   ├── public/
│   │   ├── src/
│   ├── server/   # Flask backend
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   ├── docker-compose.yml  # Docker Compose configuration
│── notebooks/
│   ├── DPO.ipynb
│── README.md
```

<hr>

## 📊 Model Training - GPT-2 on Anthropic/hh-rlhf

- Dataset: Anthropic/hh-rlhf
- Training Method: Direct Preference Optimization (DPO)
- Library Used: transformers, trl (Hugging Face's RLHF framework)
  - Hyperparameters:
  - Model: gpt2
  - Learning Rate: 1e-5
  - Batch Size: 2
  - Epochs: 3
  - Warmup Ratio: 0.1
- Trained Model: Uploaded to Hugging Face as [Suryansh-bit/a5-dpo-st124997](https://huggingface.co/Suryansh-bit/a5-dpo-st124997/tree/main)

<hr>

## 🛠️ How It Works

### Frontend (React)

- The user enters:
  - A phrase (prompt) to generate text .
- The input is sent as query parameters to the Flask backend (/predict-next endpoint).
- The generated text is displayed on the website.

### Backend (Flask)

- The Flask server receives the request at /predict with:
  - prompt → The starting phrase for text generation.
- The server loads:
  - Fetches the trained GPT-2 model alongwith tokenizer, etc from Hugging Face (Suryansh-bit/a5-dpo-st124997).
- The predict function:
  - Passes the prompt to the model and receives a response.
- The generated text is returned as JSON to the frontend.

<hr>

### Application Endpoints

- **Frontend (React app):** Runs on http://localhost:3000
- **Backend (Flask API):** Runs on http://localhost:5000

### API Endpoints

#### **`GET /`**- Returns author information.

#### **`GET /predict`** - Takes a prompt and sequence length, passes it to the model for prediction, and returns the result.

- Description: Generates text based on a user-provided prompt.
- Parameters:
  - prompt (string) → Starting phrase.
- Example Request:
  ```
  curl "http://localhost:5000/predict?prompt=Once%upon%a%time"
  ```
- Response Format:
  ```
  {
      "genText": "Once upon a time, the world was a place of great beauty and great danger. The world was a place of great danger. The world was a place of great danger."
  }
  ```

## Installation and Setup

### Step 1: Clone the Repository

```
git clone https://github.com/Suryansh2204/AIT-NLP-Assignment5.git
cd AIT-NLP-Assignment5
```

## Setup and Running the Application

This project can be run using Docker. Follow the steps below to set up and run the application.

### Running the Application

1. Navigate to the app directory:

   ```
   cd app
   ```

2. Run Docker Compose:

   ```
   docker compose up -d
   ```

This command will build the images and start the containers in detached mode.

#### Running the services separately (Alternative)

##### Install Backend Dependencies

```
cd server
pip install -r requirements.txt
```

#### Install Frontend Dependencies

```
cd client
npm install
```

#### Run the Flask Backend

```
cd server
python app.py
```

#### Run the React Frontend

```
cd client
npm start
```

- Open http://localhost:3000/ in your browser.
