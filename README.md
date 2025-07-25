# 🔐 [Password Strength Tester by Kaylhan Garcia](http://localhost:8501/#password-strength-tester)

**Empowering users with secure, ethical password practices.**  

**WATCH DEMONSTRATION HERE**

https://github.com/user-attachments/assets/9323d87b-e98b-4b6e-81cd-c98ae8890047

---

## Why I Built This

I'm currently beginning my **Master’s in Cybersecurity**, building on a background in **data science** and a passion for **ethical tech**. I wanted my first public-facing cyber project to reflect the skills I’m growing and the values I hold: transparency, playfulness, and inclusion.

This app was inspired by both my personal growth as I studied **info security**, **multi-factor authentication**, and **Sec+ fundamentals**, and by official password guidance from [Microsoft’s Security Recommendations](https://support.microsoft.com/en-us/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb#:~:text=A%20strong%20password%20is:,character%2C%20product%2C%20or%20organization.).

I also wanted this to be **interactive and fun**. That’s why strong passwords trigger 🥳 balloons, because protecting your digital life should feel like a celebration, not a chore.

In future projects, I look forward to exploring frontend development more deeply and customizing UIs to fit my personal aesthetic just for fun, because I'm a lifelong learner.

---

## Why It Matters

With the **increase in password leaks, guessable credentials, and digital breaches**, strong passwords are more critical than ever.  
This project isn’t just functional. It’s a conversation starter about how **cyber hygiene protects our communities and our identities**.

Inside the app, I include reminders that your password is key to protecting your assets, your privacy, and your story.

---

## What It Does

This Streamlit app evaluates password strength based on:
- Length (recommended minimum: 13 characters)
- Complexity (uppercase, lowercase, digits, special characters)
- Common patterns and weaknesses (e.g. `123456`, `password`, `qwerty`)
- Real-time feedback and improvement suggestions
- Celebratory balloons for very strong passwords

And a special hidden Easter egg if you type in **cyberwithkay** 😉 

---

## 🛠️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/kerawyd/password-strength-tester.git

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
