import streamlit as st

def check_eligibility():
    st.header("✅ Voting Eligibility Checker")
    st.write("Answer a few quick questions to see if you meet the basic requirements to vote.")
    
    age = st.number_input("What is your age?", min_value=0, max_value=120, value=18)
    citizen = st.radio("Are you a citizen of the country?", ("Yes", "No"))
    registered = st.radio("Are you currently registered to vote?", ("Yes", "No", "Not Sure"))
    
    if st.button("Check Eligibility"):
        if age >= 18 and citizen == "Yes":
            if registered == "Yes":
                st.success("🎉 You appear to be fully eligible and registered to vote! Check your local polling station.")
            else:
                st.info("⚠️ You meet the basic age and citizenship requirements, but you need to register! Do it before the deadline.")
        else:
            st.error("❌ Unfortunately, you do not meet the basic eligibility requirements (must be 18+ and a citizen).")
