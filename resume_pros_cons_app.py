import streamlit as st
import re

# Define keywords
PROS_KEYWORDS = [
    "hardworking", "team", "problem-solving", "leadership", "time management",
    "communication", "adaptability", "quick learner", "organized", "responsible",
    "attention to detail", "collaboration", "curiosity to learn", "presented", "attended",
    "developed", "designed", "proficient", "skilled", "certification", "experience", "project"
]

CONS_KEYWORDS = [
    "no experience", "lack", "beginner", "unfamiliar", "limited", "difficult", "struggle"
]

# Extraction function
def extract_pros_and_cons(text):
    text_lower = text.lower()
    sentences = re.split(r'[\n.]\s*', text_lower)

    pros = []
    cons = []

    for sentence in sentences:
        for keyword in PROS_KEYWORDS:
            if keyword in sentence:
                pros.append(sentence.strip())
                break
        for keyword in CONS_KEYWORDS:
            if keyword in sentence:
                cons.append(sentence.strip())
                break

    return pros, cons


# --- Streamlit App ---
st.set_page_config(page_title="Resume Pros & Cons Analyzer", layout="wide")
st.title("📋 Paste Your Resume Below to Analyze Pros & Cons")

# Text box for pasting resume
resume_text = st.text_area("Paste your resume here (plain text)", height=300)

if st.button("🔍 Analyze"):
    if resume_text.strip() == "":
        st.warning("Please paste your resume text to proceed.")
    else:
        pros, cons = extract_pros_and_cons(resume_text)

        # Show results side-by-side
        left_col, right_col = st.columns(2)

        with left_col:
            st.markdown("### ✅ Pros Identified")
            if pros:
                for p in pros:
                    st.markdown(f"✔️ {p}")
            else:
                st.info("No strong pros found.")

        with right_col:
            st.markdown("### ⚠️ Cons Identified")
            if cons:
                for c in cons:
                    st.markdown(f"❌ {c}")
            else:
                st.success("No cons detected — your resume looks solid!")
