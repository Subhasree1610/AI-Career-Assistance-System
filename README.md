🎓 **AI-Based Career Assistance System**

An AI-powered career assistance web application that helps users explore suitable career options based on their interests, skills, and career goals.

The system uses **real O*NET occupational data**, semantic embeddings, **FAISS similarity search**, and a **pretrained language model** as part of the career-assistance architecture. The application is deployed using Streamlit Community Cloud.

🌐 Live Demo

👉 https://ai-career-assistance-system-by6wypdhrjcryszbgapk9k.streamlit.app/

📌Project Overview

Choosing the right career can be difficult because users need to understand different career roles, required technical skills, education, core skills, courses, and typical job responsibilities.
This project provides a simple web-based career assistance system where users can enter a career interest or goal and receive relevant career information from a real occupational dataset.
 ✨ Features

* 🔍 Career recommendations based on user queries
* 💻 Technical skills required for different careers
* 🧠 Core skills associated with careers
* 🎓 Education requirements
* 📚 Suggested related courses
* 📋 Typical tasks and responsibilities
* 📊 Real occupational data from O*NET
* ⚡ Semantic search using sentence embeddings
* 🔎 Fast similarity search using FAISS
* 🌐 Interactive Streamlit web interface

🧠 Technologies Used

 **Python**
 **Pandas**
 **Sentence Transformers**
 **FAISS**
 **Streamlit**
 **Pretrained Language Model**
 **O*NET Occupational Database**

📊 Dataset

The project uses the **O*NET 31.0 Database**, a real occupational information database developed by the U.S. Department of Labor.
The dataset provides information such as:
* Occupation titles
* Career descriptions
* Technical/software skills
* Core skills
* Education requirements
* Job tasks

O*NET: https://www.onetcenter.org/database.html

🔄 System Workflow

User Career Query
       ↓
Text Embedding
       ↓
FAISS Similarity Search
       ↓
Relevant Career Information
       ↓
Career Recommendations
       ↓
Detailed Career Information

🏗️ Project Structure
AI-Career-Assistance-System/
│
├── app (1).py
├── career_knowledge_base.csv
├── career_knowledge_base_final.csv
├── career_faiss.index
├── requirements.txt
└── README.md
```

🚀 How to Run Locally

1. Clone the repository
git clone https://github.com/Subhasree1610/AI-Career-Assistance-System.git

 2. Open the project folder
cd AI-Career-Assistance-System

3. Install the required packages
pip install -r requirements.txt

 4. Run the Streamlit application
streamlit run "app (1).py"
The application will open in your browser.

 🌐 Deployment
The application is deployed using **Streamlit Community Cloud**.
Live Application

https://ai-career-assistance-system-by6wypdhrjcryszbgapk9k.streamlit.app/

🎯 Example Career Queries
Users can search for careers such as:

* Data Scientist
* Software Developer
* Web Developer
* Database Administrator
* Computer Programmer
* Information Security Analyst
* Mechanical Engineer
* Civil Engineer
* Electrical Engineer

🎓 Purpose
This project demonstrates how **AI, natural language processing, semantic search, real-world career data, and web technologies** can be combined to build a practical career assistance application.

👩‍💻 Author

Subhasree 

AI & Data Science Student

---

⭐ If you find this project useful, consider giving the repository a star.
