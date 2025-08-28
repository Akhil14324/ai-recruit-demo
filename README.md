# ai-recruit-demo
# AI Recruit Demo 🤖💼

An **AI-powered recruitment demo** that showcases how machine learning and NLP can be used to assist in resume parsing, candidate-job matching, and ranking.  

Built with **Python + FastAPI**, this project demonstrates how recruiters can automate initial candidate screening.

---

## 🚀 Features
- 📄 **Resume Parsing** – Extracts skills, education, and experience  
- 🎯 **Job Matching** – Compares candidate profiles with job descriptions  
- 📊 **Ranking System** – Generates similarity scores between candidates and job requirements  
- ⚡ **FastAPI Backend** – Interactive API docs with Swagger UI and ReDoc  
- 🔑 **Environment Config** – Secure `.env` for API keys and secrets  

---

## 📂 Project Structure
ai-recruit-demo/
│── app/
│ └── main.py # FastAPI entrypoint
│── requirements.txt # Python dependencies
│── .env.example # Example environment file
│── .gitignore # Git ignore rules
│── README.md # Project documentation
---

## 🛠️ Installation & Setup

### 1. Clone the Repo

git clone https://github.com/Akhil14324/ai-recruit-demo.git
cd ai-recruit-demo

Create Virtual Environment
python -m venv venv


Activate it:

# Mac/Linux
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the root directory:

touch .env


Inside .env, add any required secrets/configs. Example:

OPENAI_API_KEY=your_api_key_here
DEBUG=True

▶️ Running the Project

Start the FastAPI app with Uvicorn:

uvicorn app.main:app --reload


App runs at: 👉 http://127.0.0.1:8000/

Interactive Swagger Docs: 👉 http://127.0.0.1:8000/docs

Alternative ReDoc UI: 👉 http://127.0.0.1:8000/redoc

📖 API Documentation

FastAPI automatically generates interactive docs:

Swagger UI

ReDoc

🧪 Example Workflow

Upload a resume (text/PDF)

API parses skills & experience

Compare against job description

Returns matching score + ranked candidates

🔧 Requirements

Install from requirements.txt:

pip install -r requirements.txt


Common dependencies used:

fastapi – Web framework

uvicorn – ASGI server

scikit-learn, numpy, pandas – ML/Data handling

python-dotenv – Manage .env

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature-xyz)

Commit changes and open a PR

📜 License

This project is licensed under the MIT License.

✨ Author

Akhil
👨‍💻 Built with love, Python, FastAPI, and way too much coffee ☕


---

Do you also want me to **generate the `.env.example` file** (w
