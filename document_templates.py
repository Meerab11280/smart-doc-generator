# document_templates.py

def generate_cv(data):
    return f"""
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Address: {data['address']}

Objective:
{data['objective']}

Education:
{data['education']}

Experience:
{data['experience']}

Skills:
{data['skills']}

Projects:
{data['projects']}
"""

def generate_leave_application(data):
    return f"""
To,
The Principal,
{data['institution']}

Subject: Application for Leave

Respected Sir/Madam,

I am writing to formally request leave from {data['leave_start']} to {data['leave_end']} due to {data['reason']}. I am a student of class {data['class']} and will ensure all pending work is completed upon my return.

I would be grateful if you could grant me the requested leave.

Thank you for your kind consideration.

Yours sincerely,  
{data['name']}  
Roll No: {data['roll_number']}
"""

def generate_job_application(data):
    return f"""
To,  
The HR Manager,  
{data['company_name']}

Subject: Application for the Position of {data['job_title']}

Dear Sir/Madam,

I am writing to express my interest in the position of {data['job_title']} at your esteemed company. With my qualifications and experience, I am confident that I can contribute effectively to your organization.

I have attached my CV for your review. I would be honored to have the opportunity to discuss how my background aligns with your needs.

Thank you for considering my application.

Sincerely,  
{data['name']}  
Email: {data['email']}  
Phone: {data['phone']}
"""

def generate_study_application(data):
    return f"""
To,  
The Head of Department,  
{data['institution']}

Subject: Application for Further Study Permission

Respected Sir/Madam,

I am writing to seek your kind permission to pursue further studies in the field of {data['program']}. I believe this will enhance my academic and professional growth.

I assure you that my current responsibilities will not be neglected during this period.

Thank you for your support.

Sincerely,  
{data['name']}  
Roll No: {data['roll_number']}
"""

def generate_character_certificate(data):
    return f"""
To Whom It May Concern,

This is to certify that Mr./Ms. {data['name']} S/O, D/O {data['father_name']} has been a student of {data['institution']} in class {data['class']} from {data['from_year']} to {data['to_year']}. During this period, their conduct and character remained satisfactory.

We wish them success in their future endeavors.

Principal  
{data['institution']}
"""

def generate_internship_application(data):
    return f"""
To,  
The Internship Coordinator,  
{data['company_name']}

Subject: Application for Internship

Respected Sir/Madam,

I am a student of {data['degree']} at {data['university']}, and I am seeking an internship opportunity in your organization. I am highly motivated and eager to gain practical experience in {data['field']}.

I hope for a positive response from your side.

Sincerely,  
{data['name']}  
Email: {data['email']}  
Phone: {data['phone']}
"""

def generate_bank_account_application(data):
    return f"""
To,  
The Branch Manager,  
{data['bank_name']}

Subject: Application for Opening a Bank Account

Respected Sir/Madam,

I would like to open a new savings account at your branch. My details are as follows:

Name: {data['name']}  
Father's Name: {data['father_name']}  
CNIC: {data['cnic']}  
Address: {data['address']}  
Contact: {data['phone']}

Kindly let me know the further process and required documentation.

Thanking you in anticipation.

Yours sincerely,  
{data['name']}
"""

def generate_fee_concession_application(data):
    return f"""
To,  
The Principal,  
{data['institution']}

Subject: Application for Fee Concession

Respected Sir/Madam,

I am writing to request a fee concession due to financial difficulties faced by my family. I am a student of class {data['class']} and have always maintained good academic performance.

I would be grateful if you could consider my request and allow me the opportunity to continue my education.

Sincerely,  
{data['name']}  
Roll No: {data['roll_number']}
"""

def generate_exam_center_change(data):
    return f"""
To,  
The Controller of Examinations,  
{data['university']}

Subject: Request for Change of Examination Center

Respected Sir/Madam,

I am a student of {data['program']} and I request a change of my examination center from {data['current_center']} to {data['requested_center']} due to {data['reason']}.

Kindly consider my request and provide confirmation.

Sincerely,  
{data['name']}  
Roll No: {data['roll_number']}
"""

def generate_experience_certificate(data):
    return f"""
To Whom It May Concern,

This is to certify that Mr./Ms. {data['name']} has worked with us at {data['company']} as a {data['designation']} from {data['start_date']} to {data['end_date']}. During this tenure, their performance and conduct were satisfactory.

We wish them success in all future endeavors.

Authorized Signatory  
{data['company']}
"""

def generate_freelance_contract(data):
    return f"""
Freelance Agreement

This agreement is made between {data['client_name']} (Client) and {data['freelancer_name']} (Freelancer) on {data['date']}.

Project: {data['project_description']}  
Payment: {data['payment_terms']}  
Deadline: {data['deadline']}  

Both parties agree to the above terms.

Signed,  
Client: {data['client_name']}  
Freelancer: {data['freelancer_name']}
"""

def generate_resignation_letter(data):
    return f"""
To,  
The Manager,  
{data['company_name']}

Subject: Resignation Letter

Dear Sir/Madam,

I am writing to formally resign from my position as {data['position']} at {data['company_name']}, effective from {data['resignation_date']}.

Thank you for the opportunities and experiences I have gained during my time with the organization.

Sincerely,  
{data['name']}
"""

def generate_rental_agreement(data):
    return f"""
Rental Agreement

This agreement is made between the Landlord {data['landlord_name']} and the Tenant {data['tenant_name']} for the property located at {data['property_address']}.

Rent Amount: {data['rent_amount']}  
Duration: {data['rental_duration']}  
Start Date: {data['start_date']}

Both parties agree to the terms and conditions outlined above.

Landlord Signature: __________  
Tenant Signature: __________
"""
---


