import streamlit as st
import re

def check_password_strength(password):
    strength = "Weak"
    score = 0
    requirements = []
    
    # Length check
    if len(password) >= 8:
        score += 1
        requirements.append("✔️ Minimum 8 characters")
    else:
        requirements.append("❌ At least 8 characters required")
    
    if len(password) >= 12:
        score += 1
    
    # Upper and lower case check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
        requirements.append("✔️ Contains uppercase letters")
    else:
        requirements.append("❌ Must include uppercase letters")
    
    # Number check
    if re.search(r"\d", password):
        score += 1
        requirements.append("✔️ Contains at least one number")
    else:
        requirements.append("❌ Must include at least one number")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        requirements.append("✔️ Contains at least one special character")
    else:
        requirements.append("❌ Must include at least one special character")
    
    # Determine strength based on score
    if score == 1 or score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score >= 4:
        strength = "Strong"
    
    return strength, requirements

# Streamlit UI
st.markdown("<h1 style='color: #696969'>🔒PASSWORD STRENGTH CHECKER</h1>", unsafe_allow_html=True)
password = st.text_input("Enter your password:", type="password")


if password:
    strength, requirements = check_password_strength(password)
    
    if strength == "Weak":
        st.error(f"Password Strength: {strength} 😟")
    elif strength == "Moderate":
        st.warning(f"Password Strength: {strength} 😐")
    else:
        st.success(f"Password Strength: {strength} 💪")
    
    # Streamlit UI with color in st.write
    st.write("<h4 style='color: #696976;'>REQUIREMENTS:</h4>", unsafe_allow_html=True)

    for req in requirements:
        st.write(req)
