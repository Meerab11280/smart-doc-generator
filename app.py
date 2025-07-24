import streamlit as st
from generate_pdf import create_pdf
from document_templates import (
    generate_cv,
    generate_leave_application,
    generate_job_application,
    generate_study_application,
    generate_character_certificate,
    generate_internship_application,
    generate_bank_account_application,
    generate_fee_concession_application,
    generate_exam_center_change_application,
    generate_experience_certificate,
    generate_freelance_contract,
    generate_resignation_letter,
    generate_rental_agreement
)

TEMPLATES = {
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

st.set_page_config(page_title="Smart Doc Generator", layout="centered")

st.title("📄 Smart Document Generator")
doc_type = st.selectbox("Choose a document type:", list(TEMPLATES.keys()))

if doc_type:
    st.subheader(f"Fill the fields for: {doc_type}")
    fields = {}

    if doc_type == "CV":
        fields["name"] = st.text_input("Full Name")
        fields["email"] = st.text_input("Email")
        fields["phone"] = st.text_input("Phone")
        fields["address"] = st.text_input("Address")
        fields["summary"] = st.text_area("Career Summary")
        fields["education"] = st.text_area("Education")
        fields["experience"] = st.text_area("Experience")
        fields["skills"] = st.text_area("Skills")
        fields["projects"] = st.text_area("Projects")
        fields["certifications"] = st.text_area("Certifications")

    elif doc_type == "Leave Application":
        fields["authority"] = st.text_input("To (Authority)")
        fields["institution"] = st.text_input("School/College/Company Name")
        fields["name"] = st.text_input("Your Name")
        fields["class"] = st.text_input("Class/Designation")
        fields["start_date"] = st.date_input("Start Date")
        fields["end_date"] = st.date_input("End Date")
        fields["reason"] = st.text_area("Reason for Leave")

    elif doc_type == "Job Application":
        fields["company"] = st.text_input("Company Name")
        fields["position"] = st.text_input("Job Position")
        fields["experience"] = st.text_area("Your Experience")
        fields["skills"] = st.text_area("Your Skills")
        fields["name"] = st.text_input("Your Name")
        fields["email"] = st.text_input("Email")

    elif doc_type == "Further Study Application":
        fields["name"] = st.text_input("Your Name")
        fields["institution"] = st.text_input("Current Institution")
        fields["current_program"] = st.text_input("Current Program")
        fields["desired_program"] = st.text_input("Desired Program")
        fields["desired_institution"] = st.text_input("Desired Institution")
        fields["reason"] = st.text_area("Reason for Applying")

    elif doc_type == "Character Certificate":
        fields["name"] = st.text_input("Student Name")
        fields["father_name"] = st.text_input("Father's Name")
        fields["institution"] = st.text_input("Institution Name")
        fields["duration"] = st.text_input("Duration (e.g., 2021–2024)")
        fields["behavior"] = st.text_input("Conduct/Behavior")

    elif doc_type == "Internship Application":
        fields["company"] = st.text_input("Company Name")
        fields["name"] = st.text_input("Your Name")
        fields["program"] = st.text_input("Your Degree Program")
        fields["institution"] = st.text_input("Your Institution")
        fields["reason"] = st.text_area("Why do you want this internship?")

    elif doc_type == "Bank Account Opening Application":
        fields["bank_name"] = st.text_input("Bank Name")
        fields["name"] = st.text_input("Your Name")
        fields["cnic"] = st.text_input("CNIC Number")
        fields["account_type"] = st.selectbox("Account Type", ["Current", "Saving", "Student"])
        fields["address"] = st.text_area("Your Address")

    elif doc_type == "Fee Concession Application":
        fields["institution"] = st.text_input("Institution Name")
        fields["name"] = st.text_input("Student Name")
        fields["class"] = st.text_input("Class")
        fields["reason"] = st.text_area("Reason for Fee Concession")

    elif doc_type == "Examination Center Change Application":
        fields["name"] = st.text_input("Your Name")
        fields["roll_no"] = st.text_input("Roll Number")
        fields["current_center"] = st.text_input("Current Exam Center")
        fields["desired_center"] = st.text_input("Desired Exam Center")
        fields["reason"] = st.text_area("Reason for Changing Center")

    elif doc_type == "Experience Certificate":
        fields["employee_name"] = st.text_input("Employee Name")
        fields["position"] = st.text_input("Position")
        fields["company_name"] = st.text_input("Company Name")
        fields["duration"] = st.text_input("Work Duration")
        fields["performance"] = st.text_input("Performance/Conduct")

    elif doc_type == "Freelance Contract":
        fields["freelancer_name"] = st.text_input("Freelancer Name")
        fields["client_name"] = st.text_input("Client Name")
        fields["service_description"] = st.text_area("Service Description")
        fields["rate"] = st.text_input("Rate/Payment")
        fields["duration"] = st.text_input("Duration")
        fields["payment_terms"] = st.text_area("Payment Terms")

    elif doc_type == "Resignation Letter":
        fields["company"] = st.text_input("Company Name")
        fields["name"] = st.text_input("Your Name")
        fields["position"] = st.text_input("Your Position")
        fields["last_day"] = st.date_input("Last Working Day")
        fields["reason"] = st.text_area("Reason for Resignation")

    elif doc_type == "Rental Agreement":
        fields["landlord_name"] = st.text_input("Landlord Name")
        fields["tenant_name"] = st.text_input("Tenant Name")
        fields["property_address"] = st.text_area("Property Address")
        fields["rent_amount"] = st.text_input("Monthly Rent")
        fields["duration"] = st.text_input("Duration of Agreement")
        fields["terms"] = st.text_area("Terms and Conditions")

    if st.button("Generate Document"):
        try:
            doc_function = TEMPLATES[doc_type]
            result = doc_function(fields)
            st.success("✅ Document generated successfully!")
            st.text_area("📄 Preview", result, height=400)

            pdf_bytes = create_pdf(result)
            st.download_button("📥 Download PDF", pdf_bytes, file_name=f"{doc_type.replace(' ', '_')}.pdf")
        except Exception as e:
            st.error("❌ An error occurred while generating the document.")
