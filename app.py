import streamlit as st
from document_templates import *
from generate_pdf import generate_pdf

st.set_page_config(page_title="Smart Doc Generator", layout="centered")

st.title("📄 Smart Document Generator")

doc_type = st.selectbox("Select Document Type", [
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

# Dynamic Input Fields Based on Template
if doc_type == "CV":
    user_inputs['name'] = st.text_input("Full Name")
    user_inputs['email'] = st.text_input("Email")
    user_inputs['phone'] = st.text_input("Phone Number")
    user_inputs['address'] = st.text_input("Address")
    user_inputs['education'] = st.text_area("Education")
    user_inputs['experience'] = st.text_area("Experience")
    user_inputs['skills'] = st.text_area("Skills")
    user_inputs['references'] = st.text_area("References")

elif doc_type == "Leave Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['class'] = st.text_input("Your Class")
    user_inputs['institution'] = st.text_input("School/College Name")
    user_inputs['authority'] = st.text_input("Authority to Address (e.g., Principal)")
    user_inputs['reason'] = st.text_area("Reason for Leave")
    user_inputs['leave_dates'] = st.text_input("Leave Dates (e.g., 5th to 7th August)")

elif doc_type == "Job Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['position'] = st.text_input("Job Position")
    user_inputs['company'] = st.text_input("Company Name")
    user_inputs['skills'] = st.text_area("Relevant Skills")
    user_inputs['experience'] = st.text_area("Previous Experience")
    user_inputs['contact'] = st.text_input("Your Contact Info")

elif doc_type == "Further Study Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['current_institute'] = st.text_input("Current Institute")
    user_inputs['future_institute'] = st.text_input("Target Institute")
    user_inputs['reason'] = st.text_area("Reason for Further Study")

elif doc_type == "Character Certificate":
    user_inputs['student_name'] = st.text_input("Student Name")
    user_inputs['father_name'] = st.text_input("Father's Name")
    user_inputs['duration'] = st.text_input("Duration of Study")
    user_inputs['institute'] = st.text_input("Institute Name")

elif doc_type == "Internship Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['field'] = st.text_input("Field of Study")
    user_inputs['organization'] = st.text_input("Organization Name")
    user_inputs['duration'] = st.text_input("Internship Duration")

elif doc_type == "Bank Account Opening Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['account_type'] = st.text_input("Account Type (e.g., Savings)")
    user_inputs['bank_name'] = st.text_input("Bank Name")
    user_inputs['address'] = st.text_input("Your Address")

elif doc_type == "Fee Concession Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['father_name'] = st.text_input("Father's Name")
    user_inputs['reason'] = st.text_area("Reason for Concession")
    user_inputs['institution'] = st.text_input("Institute Name")

elif doc_type == "Examination Center Change Application":
    user_inputs['name'] = st.text_input("Your Name")
    user_inputs['roll_number'] = st.text_input("Roll Number")
    user_inputs['current_center'] = st.text_input("Current Center")
    user_inputs['desired_center'] = st.text_input("Desired Center")
    user_inputs['reason'] = st.text_area("Reason for Change")

elif doc_type == "Experience Certificate":
    user_inputs['employee_name'] = st.text_input("Employee Name")
    user_inputs['designation'] = st.text_input("Designation")
    user_inputs['duration'] = st.text_input("Employment Duration")
    user_inputs['organization'] = st.text_input("Organization Name")

elif doc_type == "Freelance Contract":
    user_inputs['freelancer_name'] = st.text_input("Freelancer Name")
    user_inputs['client_name'] = st.text_input("Client Name")
    user_inputs['project_description'] = st.text_area("Project Description")
    user_inputs['payment_terms'] = st.text_area("Payment Terms")
    user_inputs['duration'] = st.text_input("Contract Duration")

elif doc_type == "Resignation Letter":
    user_inputs['employee_name'] = st.text_input("Employee Name")
    user_inputs['designation'] = st.text_input("Designation")
    user_inputs['organization'] = st.text_input("Organization Name")
    user_inputs['reason'] = st.text_area("Reason for Resignation")
    user_inputs['notice_period'] = st.text_input("Notice Period")

elif doc_type == "Rental Agreement":
    user_inputs['landlord_name'] = st.text_input("Landlord Name")
    user_inputs['tenant_name'] = st.text_input("Tenant Name")
    user_inputs['property_address'] = st.text_area("Property Address")
    user_inputs['rental_amount'] = st.text_input("Monthly Rent")
    user_inputs['duration'] = st.text_input("Rental Duration")

# Generate Document
if st.button("Generate Document"):
    try:
        func_name = doc_type.lower().replace(" ", "_")
        generate_func = globals()[f"generate_{func_name}"]
        content = generate_func(user_inputs)

        st.subheader("📝 Generated Document")
        st.text_area("Preview", value=content, height=400)

        pdf_file = generate_pdf(content)
        if pdf_file:
            st.download_button(
                "📥 Download PDF",
                data=pdf_file,
                file_name=f"{doc_type.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        else:
            st.error("PDF generation failed. Please try again.")
    except KeyError as e:
        st.error(f"Missing input: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
