import streamlit as st
import re

# window + . press krny ce emoji show hoti hian.

# Now we create a strength password create in python with use of streamlit libaray .

st.set_page_config(page_title="strength password checker", page_icon="🔒")

st.title("Wellcome")

st.markdown("""

## Welcome to New User 
            
""")
password = st.text_input("Enter your password", type="password")

feedback = []

score = 0
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain upper and lower case characters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append('❌ Password should contain at least one digit.')

    if re.search(r'[!@*&#% ]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")

    if score == 4:
        feedback.append("✔ Your password is strong")
    elif score == 3:
        feedback.append("🟡 Your password is medium strong")
    else:
        feedback.append("🔴 Your password is weak, please make it strong")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
    else:
        st.info("Please set your password and start your work")
                    



