import streamlit as st
from document_templates import *
from generate_pdf import create_pdf

st.set_page_config(page_title="Smart Document Generator", layout="centered")
st.title("📄 Smart Document Generator")

doc_types = {
    "CV": generate_cv,
    "Leave Application": generate_leave_application,
    "Job Application": generate_job_application,
    "Further Study Application": generate_study_application,
    "Character Certificate": generate_character_certificate,
    "Internship Application": generate_internship_application,
    "Bank Account Opening Application": generate_bank_account_application,
    "Fee Concession Application": generate_fee_concession_application,
    "Examination Center Change Application": generate_exam_center_change_application,
    "Experience Certificate": generate_experience_certificate,
    "Freelance Contract": generate_freelance_contract,
    "Resignation Letter": generate_resignation_letter,
    "Rental Agreement": generate_rental_agreement
}

doc_type = st.selectbox("Select Document Type", list(doc_types.keys()))
user_inputs = {}

st.subheader(f"Enter details for {doc_type}")

if doc_type == "CV":
    user_inputs["name"] = st.text_input("Full Name")
    user_inputs["email"] = st.text_input("Email")
    user_inputs["phone"] = st.text_input("Phone Number")
    user_inputs["address"] = st.text_area("Address")
    user_inputs["summary"] = st.text_area("Career Summary")
    user_inputs["education"] = st.text_area("Education (with years)")
    user_inputs["experience"] = st.text_area("Experience (with years and companies)")
    user_inputs["skills"] = st.text_area("Skills")
    user_inputs["projects"] = st.text_area("Projects")
    user_inputs["certifications"] = st.text_area("Certifications")

elif doc_type == "Leave Application":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["class"] = st.text_input("Your Class or Department")
    user_inputs["institution"] = st.text_input("Institution Name")
    user_inputs["start_date"] = st.text_input("Start Date of Leave")
    user_inputs["end_date"] = st.text_input("End Date of Leave")
    user_inputs["reason"] = st.text_area("Reason for Leave")
    user_inputs["authority"] = st.text_input("Authority Title (e.g., Principal)")

elif doc_type == "Job Application":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["position"] = st.text_input("Position You're Applying For")
    user_inputs["company"] = st.text_input("Company Name")
    user_inputs["experience"] = st.text_area("Your Experience Summary")
    user_inputs["skills"] = st.text_area("Relevant Skills")
    user_inputs["email"] = st.text_input("Your Email Address")

elif doc_type == "Further Study Application":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["current_program"] = st.text_input("Current Program (e.g., BSCS)")
    user_inputs["institution"] = st.text_input("Current Institution")
    user_inputs["reason"] = st.text_area("Reason for Further Study")
    user_inputs["desired_program"] = st.text_input("Program You Wish to Pursue")
    user_inputs["desired_institution"] = st.text_input("Institution You Wish to Apply To")

elif doc_type == "Character Certificate":
    user_inputs["name"] = st.text_input("Student Name")
    user_inputs["father_name"] = st.text_input("Father's Name")
    user_inputs["institution"] = st.text_input("Institution Name")
    user_inputs["duration"] = st.text_input("Duration of Study (e.g., 2020-2024)")
    user_inputs["behavior"] = st.text_area("Behavior Remarks")

elif doc_type == "Internship Application":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["institution"] = st.text_input("Institution Name")
    user_inputs["program"] = st.text_input("Program or Department")
    user_inputs["company"] = st.text_input("Company Name")
    user_inputs["reason"] = st.text_area("Why You Want This Internship")

elif doc_type == "Bank Account Opening Application":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["cnic"] = st.text_input("CNIC Number")
    user_inputs["account_type"] = st.text_input("Account Type (e.g., Savings)")
    user_inputs["bank_name"] = st.text_input("Bank Name")
    user_inputs["address"] = st.text_area("Your Address")

elif doc_type == "Fee Concession Application":
    user_inputs["name"] = st.text_input("Student Name")
    user_inputs["class"] = st.text_input("Class or Department")
    user_inputs["institution"] = st.text_input("Institution Name")
    user_inputs["reason"] = st.text_area("Reason for Fee Concession")

elif doc_type == "Examination Center Change Application":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["roll_no"] = st.text_input("Roll Number")
    user_inputs["current_center"] = st.text_input("Current Exam Center")
    user_inputs["desired_center"] = st.text_input("Desired Exam Center")
    user_inputs["reason"] = st.text_area("Reason for Change")

elif doc_type == "Experience Certificate":
    user_inputs["employee_name"] = st.text_input("Employee Name")
    user_inputs["position"] = st.text_input("Position Held")
    user_inputs["company_name"] = st.text_input("Company Name")
    user_inputs["duration"] = st.text_input("Duration (e.g., Jan 2020 - Dec 2023)")
    user_inputs["performance"] = st.text_area("Performance Summary")

elif doc_type == "Freelance Contract":
    user_inputs["freelancer_name"] = st.text_input("Freelancer Name")
    user_inputs["client_name"] = st.text_input("Client Name")
    user_inputs["service_description"] = st.text_area("Services Description")
    user_inputs["rate"] = st.text_input("Agreed Rate")
    user_inputs["duration"] = st.text_input("Duration of Contract")
    user_inputs["payment_terms"] = st.text_area("Payment Terms")

elif doc_type == "Resignation Letter":
    user_inputs["name"] = st.text_input("Your Full Name")
    user_inputs["position"] = st.text_input("Your Position")
    user_inputs["company"] = st.text_input("Company Name")
    user_inputs["last_day"] = st.text_input("Last Working Day")
    user_inputs["reason"] = st.text_area("Reason for Resignation")

elif doc_type == "Rental Agreement":
    user_inputs["landlord_name"] = st.text_input("Landlord Name")
    user_inputs["tenant_name"] = st.text_input("Tenant Name")
    user_inputs["property_address"] = st.text_area("Property Address")
    user_inputs["rent_amount"] = st.text_input("Monthly Rent Amount")
    user_inputs["duration"] = st.text_input("Rental Duration")
    user_inputs["terms"] = st.text_area("Special Terms and Conditions")

if st.button("Generate Document"):
    content = doc_types[doc_type](user_inputs)
    st.subheader("📄 Generated Document")
    st.text_area("Document Preview", content, height=400)
    pdf_file = create_pdf(content)
    st.download_button("📥 Download PDF", data=pdf_file, file_name=f"{doc_type.replace(' ', '_')}.pdf", mime="application/pdf")
