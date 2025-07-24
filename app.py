# app.py

import streamlit as st
from document_templates import *
from generate_pdf import generate_pdf

st.set_page_config(page_title="Smart Document Generator", layout="centered")

st.title("📄 Smart Document Generator")

doc_type = st.selectbox("Select the type of document to generate:", [
    "CV",
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

if doc_type == "CV":
    user_inputs['name'] = st.text_input("Full Name")
    user_inputs['email'] = st.text_input("Email")
    user_inputs['phone'] = st.text_input("Phone")
    user_inputs['address'] = st.text_area("Address")
    user_inputs['objective'] = st.text_area("Objective")
    user_inputs['education'] = st.text_area("Education")
    user_inputs['experience'] = st.text_area("Experience")
    user_inputs['skills'] = st.text_area("Skills")
    user_inputs['projects'] = st.text_area("Projects")
    generate = generate_cv

elif doc_type == "Leave Application":
    user_inputs['institution'] = st.text_input("Institution Name")
    user_inputs['class'] = st.text_input("Class")
    user_inputs['roll_number'] = st.text_input("Roll Number")
    user_inputs['leave_start'] = st.date_input("Leave Start Date")
    user_inputs['leave_end'] = st.date_input("Leave End Date")
    user_inputs['reason'] = st.text_area("Reason for Leave")
    user_inputs['name'] = st.text_input("Your Name")
    generate = generate_leave_application

elif doc_type == "Job Application":
    user_inputs['company_name'] = st.text_input("Company Name")
    user_inputs['job_title'] = st.text_input("Job Title")
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['email'] = st.text_input("Email")
    user_inputs['phone'] = st.text_input("Phone")
    generate = generate_job_application

elif doc_type == "Further Study Application":
    user_inputs['institution'] = st.text_input("Institution Name")
    user_inputs['program'] = st.text_input("Program Name")
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['roll_number'] = st.text_input("Roll Number")
    generate = generate_study_application

elif doc_type == "Character Certificate":
    user_inputs['name'] = st.text_input("Student Name")
    user_inputs['father_name'] = st.text_input("Father's Name")
    user_inputs['institution'] = st.text_input("Institution Name")
    user_inputs['class'] = st.text_input("Class")
    user_inputs['from_year'] = st.text_input("From Year")
    user_inputs['to_year'] = st.text_input("To Year")
    generate = generate_character_certificate

elif doc_type == "Internship Application":
    user_inputs['company_name'] = st.text_input("Company Name")
    user_inputs['degree'] = st.text_input("Degree Program")
    user_inputs['university'] = st.text_input("University Name")
    user_inputs['field'] = st.text_input("Field of Internship")
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['email'] = st.text_input("Email")
    user_inputs['phone'] = st.text_input("Phone")
    generate = generate_internship_application

elif doc_type == "Bank Account Opening Application":
    user_inputs['bank_name'] = st.text_input("Bank Name")
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['father_name'] = st.text_input("Father's Name")
    user_inputs['cnic'] = st.text_input("CNIC Number")
    user_inputs['address'] = st.text_area("Address")
    user_inputs['phone'] = st.text_input("Phone Number")
    generate = generate_bank_account_application

elif doc_type == "Fee Concession Application":
    user_inputs['institution'] = st.text_input("Institution Name")
    user_inputs['class'] = st.text_input("Class")
    user_inputs['roll_number'] = st.text_input("Roll Number")
    user_inputs['name'] = st.text_input("Your Name")
    generate = generate_fee_concession_application

elif doc_type == "Examination Center Change Application":
    user_inputs['university'] = st.text_input("University Name")
    user_inputs['program'] = st.text_input("Program Name")
    user_inputs['current_center'] = st.text_input("Current Exam Center")
    user_inputs['requested_center'] = st.text_input("Requested Exam Center")
    user_inputs['reason'] = st.text_area("Reason for Change")
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['roll_number'] = st.text_input("Roll Number")
    generate = generate_exam_center_change

elif doc_type == "Experience Certificate":
    user_inputs['name'] = st.text_input("Employee Name")
    user_inputs['company'] = st.text_input("Company Name")
    user_inputs['designation'] = st.text_input("Designation")
    user_inputs['start_date'] = st.date_input("Start Date")
    user_inputs['end_date'] = st.date_input("End Date")
    generate = generate_experience_certificate

elif doc_type == "Freelance Contract":
    user_inputs['client_name'] = st.text_input("Client Name")
    user_inputs['freelancer_name'] = st.text_input("Freelancer Name")
    user_inputs['project_description'] = st.text_area("Project Description")
    user_inputs['payment_terms'] = st.text_area("Payment Terms")
    user_inputs['deadline'] = st.date_input("Project Deadline")
    user_inputs['date'] = st.date_input("Agreement Date")
    generate = generate_freelance_contract

elif doc_type == "Resignation Letter":
    user_inputs['company_name'] = st.text_input("Company Name")
    user_inputs['position'] = st.text_input("Your Position")
    user_inputs['resignation_date'] = st.date_input("Resignation Date")
    user_inputs['name'] = st.text_input("Your Name")
    generate = generate_resignation_letter

elif doc_type == "Rental Agreement":
    user_inputs['landlord_name'] = st.text_input("Landlord Name")
    user_inputs['tenant_name'] = st.text_input("Tenant Name")
    user_inputs['property_address'] = st.text_area("Property Address")
    user_inputs['rent_amount'] = st.text_input("Monthly Rent Amount")
    user_inputs['rental_duration'] = st.text_input("Rental Duration (e.g. 1 year)")
    user_inputs['start_date'] = st.date_input("Start Date of Agreement")
    generate = generate_rental_agreement

# Generate document
if st.button("Generate Document"):
    try:
        content = generate(user_inputs)
        st.subheader("Generated Document:")
        st.text_area("Preview", content, height=400)

        pdf = generate_pdf(content)

        st.download_button("📥 Download as PDF", data=pdf, file_name=f"{doc_type.replace(' ', '_')}.pdf", mime="application/pdf")

    except KeyError as e:
        st.error(f"Missing field: {e}. Please fill in all required inputs.")

