import streamlit as st
from openai import OpenAI

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Astrology App",
    page_icon="🔮",
    layout="centered"
)

# ---------- CUSTOM LIGHT GREEN CSS ----------
st.markdown("""
<style>
.stApp {
    background-color: #F4FFF8;
}
h1, h2, h3 {
    color: #2F855A;
}
.stButton > button {
    background-color: #6BCF9D;
    color: white;
    border-radius: 8px;
    font-size: 16px;
}
.stTextInput input, .stTextArea textarea {
    background-color: #ECFDF5;
}
</style>
""", unsafe_allow_html=True)

# ---------- OPENAI CLIENT ----------
key='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'

client = OpenAI(api_key=key)

# ---------- UI ----------
st.title("🔮 AI Astrology App")
st.caption("Personalized insights powered by AI ✨")

name = st.text_input("👤 Your Name")
dob = st.date_input("📅 Date of Birth")
tob = st.text_input("⏰ Time of Birth (HH:MM)")
place = st.text_input("📍 Place of Birth")

# ---------- FUNCTION ----------
def get_astrology_reading(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced Vedic astrologer. "
                    "Give insightful, positive, and non-deterministic guidance."
                )
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# ---------- ACTION ----------
if st.button("✨ Get My Astrology Reading"):
    if not all([name, dob, tob, place]):
        st.warning("⚠️ Please fill all details")
    else:
        user_prompt = f"""
        Name: {name}
        Date of Birth: {dob}
        Time of Birth: {tob}
        Place of Birth: {place}

        Provide:
        1. Personality traits
        2. Career guidance
        3. Financial outlook
        4. Relationship insights
        5. One practical life suggestion
        """

        with st.spinner("Reading your stars... 🌟"):
            result = get_astrology_reading(user_prompt)

        st.markdown("## 🌿 Your Astrology Reading")
        st.write(result)

st.markdown("---")
st.caption("⚠️ For guidance purposes only • Built with Python & OpenAI")
