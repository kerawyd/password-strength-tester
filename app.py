import streamlit as st
import re 

st.title("Password Strength Tester")
st.write("Empowering users with ethical, secure password practices.")

def evaluate_password(password):
    pass

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
    strength, feedback = evaluate_password(password)
    st.markdown(f"**Strength:** {strength}")
    if feedback:
        st.markdown("**Suggestions:**")
        for item in feedback:
            st.markdown(f"- {item}")