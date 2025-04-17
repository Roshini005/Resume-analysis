import streamlit as st
import re

# Define keyword lists
PROS_KEYWORDS = [
    "hardworking", "team", "problem-solving", "leadership", "time management",
    "communication", "adaptability", "quick learner", "organized", "responsible",
    "attention to detail", "collaboration", "curiosity to learn", "presented", "attended",
    "developed", "designed", "proficient", "skilled", "certification", "experience", "project"
]

CONS_KEYWORDS = [
    "no experience", "lack of experience", "beginner", "unfamiliar", "limited knowledge",
    "difficult", "struggling", "trying to improve", "novice", "inexperienced", "in progress",
    "learning phase", "not confident", "needs improvement", "basic knowledge", "still learning",
    "lack of confidence", "requires guidance", "room for improvement", "under development", 
    "not well-versed", "has potential but"
]

# Function to extract pros and cons
def extract_pros_and_cons(text):
    text_lower = text.lower()
    sentences = re.split(r'[\n.]\s*', text_lower)

    pros = []
    cons = []

    for sentence in sentences:
        # Check for pros
        for keyword in PROS_KEYWORDS:
            if keyword in sentence:
                pros.append(sentence.strip())
                break
        
        # Check for cons
        for keyword in CONS_KEYWORDS:
            if keyword in sentence:
                cons.append(sentence.strip())
                break

    return pros, cons


# --- Streamlit UI ---
st.set_page_config(page_title="Resume Analyzer", layout="wide")
st.title("📄 Resume Analyzer: Pros & Cons")

# Divide screen into 2 columns: input (left), output (right)
left_col, right_col = st.columns([1, 2])

with left_col:
    st.subheader("📝 Paste Resume Text")
    resume_text = st.text_area("Paste your resume here (plain text)", height=400)

with right_col:
    st.subheader("📊 Analysis Result")
    if resume_text.strip():
        pros, cons = extract_pros_and_cons(resume_text)

        st.markdown("#### ✅ Pros")
        if pros:
            for p in pros:
                st.markdown(f"- {p}")
        else:
            st.info("No strong pros detected.")

        st.markdown("#### ⚠️ Cons")
        if cons:
            for c in cons:
                st.markdown(f"- {c}")
        else:
            st.success("No cons detected — your resume looks solid!")

    else:
        st.info("Paste your resume on the left to see results here ➡️")
