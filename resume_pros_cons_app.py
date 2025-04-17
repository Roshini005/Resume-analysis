import streamlit as st
import re

PROS_KEYWORDS = [
    "hardworking", "team", "problem-solving", "leadership", "time management",
    "communication", "adaptability", "quick learner", "organized", "responsible",
    "attention to detail", "collaboration", "curiosity to learn", "presented", "attended",
    "developed", "designed", "proficient", "skilled", "certification", "experience", "project"
]

CONS_KEYWORDS = [
    "no experience", "lack", "beginner", "unfamiliar", "limited", "difficult", "struggle"
]


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
st.set_page_config(page_title="Resume Pros & Cons Extractor", layout="centered")

st.title("📄 Resume Pros & Cons Analyzer")

uploaded_file = st.file_uploader("Upload your resume (as a .txt file)", type=["txt"])

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")

    st.subheader("🔍 Extracting insights...")
    pros, cons = extract_pros_and_cons(file_content)

    st.markdown("### ✅ Pros Identified:")
    if pros:
        for p in pros:
            st.write(f"• {p}")
    else:
        st.write("No pros found.")

    st.markdown("### ⚠️ Cons Identified:")
    if cons:
        for c in cons:
            st.write(f"• {c}")
    else:
        st.write("No cons detected — your resume looks great!")

    st.success("Analysis complete.")

else:
    st.info("Please upload a resume in .txt format to begin.")
