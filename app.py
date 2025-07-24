import streamlit as st
import re 

st.markdown('<h1 class="title">🔐 Password Strength Tester by Kaylhan Garcia</h1>', unsafe_allow_html=True)
st.write("Empowering users with ethical, secure password practices.")

st.info("Your privacy matters. We don’t store or share anything you type here.")

def evaluate_password(password):

    score = 0
    suggestions = []

    if len(password) >= 13:
        score += 1
    else:
        suggestions.append("Uh oh! Too short. To ensure your security, password must be at least 13 characters long. ") 
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Please include capital letters to strengthen password. ")

    if re.search(r'[a-z]', password): 
        score += 1
    else:
        suggestions.append("Please include lowercase letters to strengthen password. ")

    if re.search(r'[!@#$%^&*(),.?":{}|<>[\]~`]', password):
        score += 1
    else:
        suggestions.append("Don't be scared of special characters! Add some for a stronger password. ")
    if re.search(r'(1234567891011| qwerty | password)', password, re.IGNORECASE):
        suggestions.append("Be unique (just as yourself) with your passwords. ")

    strength_labels = ["Very Poor", "Poor", "Moderate", "Strong", "Very Strong"]
    return strength_labels[min(score, 4)], suggestions

#beginning the UI 

password = st.text_input("Enter your password", type="password")

if password:
    if password.lower().strip() == "cyberwithkay":
        st.write("🎉 Easter Egg Unlocked! Check out my blog ➜ https://cyber-with-kay.super.site/")
    
    strength, feedback = evaluate_password(password)

    strength_colors = {
        "Very Poor": "red",
        "Poor": "orange",
        "Moderate": "gold",
        "Strong": "lightgreen",
        "Very Strong": "green"
    }
    color = strength_colors.get(strength, "white")

    st.markdown(f"<h3 style='color:{color}; font-weight:bold;'>Strength: {strength}</h3>", unsafe_allow_html=True)

    if strength == "Very Strong":
        st.balloons()
        st.write("WOW... I am in tears... This is such a strong password. ")

    if feedback:
        st.markdown("### Suggestions to Improve:")
        for item in feedback:
            st.markdown(f"- {item}")
