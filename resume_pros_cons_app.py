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
    "no experience", "lack", "beginner", "unfamiliar", "limited", "difficult", "struggle"
]

# Function to extract pros and cons
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


# --- Streamlit UI ---
st.set_page_config(page_title="Resume Pros & Cons Extractor", layout="wide")
st.title("📄 Resume Pros & Cons Analyzer")

uploaded_file = st.file_uploader("Upload your resume (as a .txt file)", type=["txt"])

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    pros, cons = extract_pros_and_cons(file_content)

    st.markdown("---")
    st.subheader("🔍 Resume Analysis")

    # Create two columns
    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown("### 📄 Uploaded Resume")
        st.text_area("Your Resume Content:", file_content, height=500)

    with right_col:
        st.markdown("### ✅ Pros Identified")
        if pros:
            for p in pros:
                st.markdown(f"✔️ {p}")
        else:
            st.info("No strong pros found.")

        st.markdown("### ⚠️ Cons Identified")
        if cons:
            for c in cons:
                st.markdown(f"❌ {c}")
        else:
            st.success("No cons detected — your resume looks solid!")

else:
    st.info("📥 Please upload a `.txt` file to analyze your resume.")
