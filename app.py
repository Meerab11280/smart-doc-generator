import streamlit as st
from document_templates import *
from generate_pdf import generate_pdf

st.set_page_config(page_title="Smart Document Generator", layout="centered")

st.title("📄 Smart Document Generator")

doc_type = st.selectbox("Select Document Type", [
    "CV", "Leave Application", "Job Application", "Further Study Application",
    "Character Certificate", "Internship Application", "Bank Account Opening Application",
    "Fee Concession Application", "Examination Center Change Application",
    "Experience Certificate", "Freelance Contract", "Resignation Letter", "Rental Agreement"
])

data = {}

if doc_type == "CV":
    data['name'] = st.text_input("Name")
    data['email'] = st.text_input("Email")
    data['phone'] = st.text_input("Phone")
    data['address'] = st.text_input("Address")
    data['objective'] = st.text_area("Objective")
    data['education'] = st.text_area("Education")
    data['experience'] = st.text_area("Experience")
    data['skills'] = st.text_area("Skills")

elif doc_type == "Leave Application":
    data['authority'] = st.text_input("Authority (e.g., Principal)")
    data['institution'] = st.text_input("Institution Name")
    data['address'] = st.text_input("Institution Address")
    data['start_date'] = st.date_input("Leave Start Date")
    data['end_date'] = st.date_input("Leave End Date")
    data['reason'] = st.text_area("Reason for Leave")
    data['name'] = st.text_input("Your Name")
    data['roll_number'] = st.text_input("Roll Number")
    data['date'] = st.date_input("Date")

elif doc_type == "Job Application":
    data['company'] = st.text_input("Company Name")
    data['address'] = st.text_input("Company Address")
    data['position'] = st.text_input("Position Applied For")
    data['background'] = st.text_area("Your Background (degree/skills)")
    data['name'] = st.text_input("Your Name")
    data['email'] = st.text_input("Email")
    data['phone'] = st.text_input("Phone")
    data['date'] = st.date_input("Date")

elif doc_type == "Further Study Application":
    data['institution'] = st.text_input("Institution Name")
    data['address'] = st.text_input("Institution Address")
    data['field_of_study'] = st.text_input("Field of Study")
    data['name'] = st.text_input("Your Name")
    data['date'] = st.date_input("Date")

elif doc_type == "Character Certificate":
    data['name'] = st.text_input("Student Name")
    data['father_name'] = st.text_input("Father's Name")
    data['institution'] = st.text_input("Institution Name")
    data['start_year'] = st.text_input("Start Year")
    data['end_year'] = st.text_input("End Year")
    data['date'] = st.date_input("Date")

elif doc_type == "Internship Application":
    data['company'] = st.text_input("Company Name")
    data['address'] = st.text_input("Company Address")
    data['degree'] = st.text_input("Your Degree")
    data['institution'] = st.text_input("Your Institution")
    data['field'] = st.text_input("Field of Interest")
    data['name'] = st.text_input("Your Name")
    data['email'] = st.text_input("Email")
    data['phone'] = st.text_input("Phone")
    data['date'] = st.date_input("Date")

elif doc_type == "Bank Account Opening Application":
    data['bank_name'] = st.text_input("Bank Name")
    data['branch_address'] = st.text_input("Branch Address")
    data['name'] = st.text_input("Your Full Name")
    data['cnic'] = st.text_input("CNIC Number")
    data['contact'] = st.text_input("Contact Number")
    data['address'] = st.text_input("Your Address")
    data['date'] = st.date_input("Date")

elif doc_type == "Fee Concession Application":
    data['institution'] = st.text_input("Institution Name")
    data['address'] = st.text_input("Institution Address")
    data['name'] = st.text_input("Your Name")
    data['class'] = st.text_input("Your Class")
    data['roll_number'] = st.text_input("Roll Number")
    data['date'] = st.date_input("Date")

elif doc_type == "Examination Center Change Application":
    data['university'] = st.text_input("University Name")
    data['address'] = st.text_input("University Address")
    data['program'] = st.text_input("Program Name")
    data['roll_number'] = st.text_input("Roll Number")
    data['current_center'] = st.text_input("Current Examination Center")
    data['requested_center'] = st.text_input("Requested Center")
    data['reason'] = st.text_area("Reason for Change")
    data['name'] = st.text_input("Your Name")
    data['date'] = st.date_input("Date")

elif doc_type == "Experience Certificate":
    data['name'] = st.text_input("Employee Name")
    data['designation'] = st.text_input("Designation")
    data['company'] = st.text_input("Company Name")
    data['start_date'] = st.date_input("Start Date")
    data['end_date'] = st.date_input("End Date")
    data['date'] = st.date_input("Date")

elif doc_type == "Freelance Contract":
    data['client_name'] = st.text_input("Client Name")
    data['freelancer_name'] = st.text_input("Freelancer Name")
    data['project_title'] = st.text_input("Project Title")
    data['deadline'] = st.date_input("Deadline")
    data['payment'] = st.text_input("Payment Amount")
    data['date'] = st.date_input("Agreement Date")

elif doc_type == "Resignation Letter":
    data['company'] = st.text_input("Company Name")
    data['address'] = st.text_input("Company Address")
    data['position'] = st.text_input("Position")
    data['last_working_day'] = st.date_input("Last Working Day")
    data['name'] = st.text_input("Your Name")
    data['date'] = st.date_input("Date")

elif doc_type == "Rental Agreement":
    data['landlord_name'] = st.text_input("Landlord Name")
    data['tenant_name'] = st.text_input("Tenant Name")
    data['property_address'] = st.text_input("Property Address")
    data['monthly_rent'] = st.text_input("Monthly Rent")
    data['rental_duration'] = st.text_input("Rental Duration")
    data['start_date'] = st.date_input("Start Date")
    data['date'] = st.date_input("Agreement Date")

# Generate Document
if st.button("Generate Document"):
    generator_function = {
        "CV": generate_cv,
        "Leave Application": generate_leave_application,
        "Job Application": generate_job_application,
        "Further Study Application": generate_further_study_application,
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

    if doc_type in generator_function:
        document_text = generator_function[doc_type](data)
        st.subheader("📄 Generated Document:")
        st.text_area("Preview", document_text, height=400)

        pdf_file = generate_pdf(document_text)
        st.download_button("📥 Download PDF", data=pdf_file, file_name=f"{doc_type.replace(' ', '_')}.pdf", mime="application/pdf")
