# app.py
import streamlit as st
from generate_pdf import generate_pdf
from document_templates import *

st.set_page_config(page_title="AI Document Generator", layout="centered")
st.title("📄 AI Document Generator")
st.markdown("Easily generate various professional documents with a click.")

doc_type = st.selectbox("Select Document Type", [
    "Curriculum Vitae (CV)",
    "Leave Application",
    "Job Application",
    "Further Study Application",
    "Character Certificate",
    "Internship Application",
    "Bank Account Opening Application",
    "Fee Concession Application",
    "Examination Center Change Application",
    "Experience Certificate",
    "Freelance Contract",
    "Resignation Letter",
    "Rental Agreement"
])

user_inputs = {}

if doc_type == "Curriculum Vitae (CV)":
    user_inputs["name"] = st.text_input("Full Name")
    user_inputs["email"] = st.text_input("Email")
    user_inputs["phone"] = st.text_input("Phone")
    user_inputs["address"] = st.text_input("Address")
    user_inputs["education"] = st.text_area("Education")
    user_inputs["skills"] = st.text_area("Skills")
    user_inputs["experience"] = st.text_area("Experience")
    user_inputs["hobbies"] = st.text_area("Hobbies")

elif doc_type == "Leave Application":
    user_inputs["name"] = st.text_input("Your Name")
    user_inputs["reason"] = st.text_input("Reason for Leave")
    user_inputs["dates"] = st.text_input("Leave Dates")
    user_inputs["recipient"] = st.text_input("Recipient Name")

elif doc_type == "Job Application":
    user_inputs["name"] = st.text_input("Your Name")
    user_inputs["position"] = st.text_input("Position")
    user_inputs["company"] = st.text_input("Company Name")
    user_inputs["qualification"] = st.text_input("Qualification")
    user_inputs["experience"] = st.text_area("Experience")

elif doc_type == "Further Study Application":
    user_inputs["name"] = st.text_input("Your Name")
    user_inputs["institute"] = st.text_input("Institution Name")
    user_inputs["field"] = st.text_input("Field of Study")

elif doc_type == "Character Certificate":
    user_inputs["name"] = st.text_input("Applicant's Name")
    user_inputs["institute"] = st.text_input("Institution/Organization")
    user_inputs["duration"] = st.text_input("Duration")

elif doc_type == "Internship Application":
    user_inputs["name"] = st.text_input("Your Name")
    user_inputs["institute"] = st.text_input("Your Institute")
    user_inputs["company"] = st.text_input("Company")
    user_inputs["field"] = st.text_input("Field of Internship")

elif doc_type == "Bank Account Opening Application":
    user_inputs["name"] = st.text_input("Applicant's Name")
    user_inputs["bank"] = st.text_input("Bank Name")
    user_inputs["account_type"] = st.text_input("Account Type")

elif doc_type == "Fee Concession Application":
    user_inputs["name"] = st.text_input("Student's Name")
    user_inputs["reason"] = st.text_input("Reason for Concession")
    user_inputs["class"] = st.text_input("Class")
    user_inputs["institute"] = st.text_input("Institute Name")

elif doc_type == "Examination Center Change Application":
    user_inputs["name"] = st.text_input("Student's Name")
    user_inputs["current_center"] = st.text_input("Current Center")
    user_inputs["requested_center"] = st.text_input("Requested Center")

elif doc_type == "Experience Certificate":
    user_inputs["name"] = st.text_input("Employee's Name")
    user_inputs["organization"] = st.text_input("Organization Name")
    user_inputs["duration"] = st.text_input("Duration")
    user_inputs["position"] = st.text_input("Position")

elif doc_type == "Freelance Contract":
    user_inputs["freelancer"] = st.text_input("Freelancer Name")
    user_inputs["client"] = st.text_input("Client Name")
    user_inputs["service"] = st.text_input("Service Description")
    user_inputs["deadline"] = st.text_input("Deadline")
    user_inputs["amount"] = st.text_input("Payment Amount")

elif doc_type == "Resignation Letter":
    user_inputs["name"] = st.text_input("Your Name")
    user_inputs["position"] = st.text_input("Your Position")
    user_inputs["company"] = st.text_input("Company Name")
    user_inputs["reason"] = st.text_input("Reason for Resignation")

elif doc_type == "Rental Agreement":
    user_inputs["landlord"] = st.text_input("Landlord Name")
    user_inputs["tenant"] = st.text_input("Tenant Name")
    user_inputs["property"] = st.text_input("Property Address")
    user_inputs["rent"] = st.text_input("Monthly Rent")
    user_inputs["duration"] = st.text_input("Rental Duration")

# Generate Button
if st.button("Generate Document"):
    if all(user_inputs.values()):
        if doc_type == "Curriculum Vitae (CV)":
            content = generate_cv(user_inputs)
        elif doc_type == "Leave Application":
            content = generate_leave_application(user_inputs)
        elif doc_type == "Job Application":
            content = generate_job_application(user_inputs)
        elif doc_type == "Further Study Application":
            content = generate_further_study_application(user_inputs)
        elif doc_type == "Character Certificate":
            content = generate_character_certificate(user_inputs)
        elif doc_type == "Internship Application":
            content = generate_internship_application(user_inputs)
        elif doc_type == "Bank Account Opening Application":
            content = generate_bank_account_application(user_inputs)
        elif doc_type == "Fee Concession Application":
            content = generate_fee_concession_application(user_inputs)
        elif doc_type == "Examination Center Change Application":
            content = generate_center_change_application(user_inputs)
        elif doc_type == "Experience Certificate":
            content = generate_experience_certificate(user_inputs)
        elif doc_type == "Freelance Contract":
            content = generate_freelance_contract(user_inputs)
        elif doc_type == "Resignation Letter":
            content = generate_resignation_letter(user_inputs)
        elif doc_type == "Rental Agreement":
            content = generate_rental_agreement(user_inputs)

        st.subheader("📄 Generated Document")
        st.code(content, language="markdown")

        pdf = generate_pdf(content)
        st.download_button(
            label="📥 Download PDF",
            data=pdf,
            file_name=f"{doc_type.replace(' ', '_').lower()}.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please fill all the fields.")
