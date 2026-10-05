import streamlit as st
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

st.set_page_config(
    page_title="Career Assistance System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Based Career Assistance System")

st.write(
    "Enter your interests, skills, or career goals "
    "to find suitable career options."
)

# Original career data
career_data = pd.read_csv("career_knowledge_base.csv")

# Improved technical skills
technical_data = pd.read_csv("career_knowledge_base_final.csv")

# Add improved technical skills
career_data["Technical Skills Final"] = (
    technical_data["Technical Skills Final"]
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

faiss_index = faiss.read_index(
    "career_faiss.index"
)

user_query = st.text_input(
    "💬 What career are you interested in?"
)

if st.button("🔍 Find Careers"):

    if user_query.strip():

        query_embedding = embedding_model.encode(
            [user_query],
            convert_to_numpy=True
        )

        distances, indices = faiss_index.search(
            query_embedding,
            20
        )

        query_lower = user_query.lower().strip()

        ranked_indices = []

        for idx in indices[0]:

            title = str(
                career_data.iloc[idx]["Title"]
            ).lower()

            if (
                query_lower in title
                or title in query_lower
            ):
                ranked_indices.insert(0, idx)
            else:
                ranked_indices.append(idx)

        ranked_indices = ranked_indices[:3]

        st.subheader("🎯 Recommended Careers")

        for i in ranked_indices:

            career = career_data.iloc[i]

            st.markdown("---")

            st.header(
                "💼 " + str(career["Title"])
            )

            st.subheader("📋 Career Description")
            st.write(career["Description"])

            st.subheader("💻 Technical Skills")

            technical_skills = career["Technical Skills Final"]

            if (
                pd.isna(technical_skills)
                or str(technical_skills).strip() == ""
                or str(technical_skills).lower() == "nan"
            ):
                technical_skills = career["Technical Skills"]

            st.write(technical_skills)

            st.subheader("🧠 Core Skills")
            st.write(career["Skill"])

            st.subheader("🎓 Education")
            st.write(career["Education"])

            st.subheader("📚 Suggested Related Courses")
            st.write(career["Related Courses"])

            st.subheader("📋 Typical Tasks")
            st.write(career["Task"])

    else:

        st.warning(
            "Enter your interests or career goal."
        )
