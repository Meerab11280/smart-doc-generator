def generate_cv(data):
    return f"""
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Address: {data['address']}

Objective:
A highly motivated and detail-oriented individual seeking a challenging role where I can apply my academic knowledge and skills to contribute effectively to the growth and success of the organization.

Education:
{data['education']}

Experience:
{data['experience']}

Skills:
{data['skills']}

References:
Available upon request.
"""

def generate_leave_application(data):
    return f"""
To,
The {data['authority']},
{data['institution']}.

Subject: Application for Leave

Respected Sir/Madam,

I am writing to formally request leave from {data['start_date']} to {data['end_date']} due to {data['reason']}. I assure you that I will complete all my pending tasks before going on leave or immediately upon my return.

Kindly grant me leave for the mentioned period. I shall be highly obliged.

Thank you for your consideration.

Yours sincerely,
{data['name']}
{data['class']}
"""

def generate_job_application(data):
    return f"""
To,
The Hiring Manager,
{data['company']}.

Subject: Application for the position of {data['position']}

Respected Sir/Madam,

I am writing to express my interest in the position of {data['position']} at {data['company']}. With my educational background in {data['qualification']} and my passion for contributing to a dynamic workplace, I believe I would be a valuable addition to your team.

I have attached my CV for your review. I look forward to the opportunity to further discuss how I can contribute to your organization.

Yours faithfully,
{data['name']}
Email: {data['email']}
Phone: {data['phone']}
"""

def generate_further_study_application(data):
    return f"""
To,
The Principal,
{data['institution']}.

Subject: Application for Permission to Pursue Further Studies

Respected Sir/Madam,

I am writing to seek your kind permission to pursue further studies in the field of {data['field']} at {data['university']}. I am highly enthusiastic about advancing my knowledge and career prospects and assure you that this will not affect my responsibilities or current obligations.

I hope for your favorable response and support.

Sincerely,
{data['name']}
{data['current_position']}
"""

def generate_character_certificate(data):
    return f"""
To whom it may concern,

This is to certify that Mr./Ms. {data['name']}, son/daughter of {data['father_name']}, has been a student of {data['institution']} from {data['start_year']} to {data['end_year']}. During this period, their conduct and character remained excellent.

We wish them success in all future endeavors.

Issued on: {data['issue_date']}
Principal,
{data['institution']}
"""

def generate_internship_application(data):
    return f"""
To,
The HR Department,
{data['company']}.

Subject: Application for Internship

Respected Sir/Madam,

I am currently pursuing my studies in {data['field']} at {data['university']} and am keen to gain practical experience through an internship at your esteemed organization. I am particularly interested in your company due to its reputation in the industry and the learning environment it offers.

I assure you of my dedication and eagerness to learn. Please consider my application for a suitable internship position.

Sincerely,
{data['name']}
Email: {data['email']}
Phone: {data['phone']}
"""

def generate_bank_account_opening_application(data):
    return f"""
To,
The Branch Manager,
{data['bank_name']}.

Subject: Application for Opening a New Bank Account

Respected Sir/Madam,

I am writing to request the opening of a new savings account in your branch. My details are as follows:

Name: {data['name']}
CNIC: {data['cnic']}
Contact: {data['phone']}
Address: {data['address']}

Kindly process my request at your earliest convenience. I am attaching the required documents with this application.

Sincerely,
{data['name']}
"""

def generate_fee_concession_application(data):
    return f"""
To,
The Principal,
{data['institution']}.

Subject: Application for Fee Concession

Respected Sir/Madam,

I am a student of class {data['class']} and would like to request a concession in my tuition fee due to {data['reason']}. I belong to a financially underprivileged background, and it has become difficult to afford the regular fees.

I am a hardworking and disciplined student and assure you that this concession will help me continue my studies without interruption.

Yours obediently,
{data['name']}
Roll Number: {data['roll_number']}
"""

def generate_exam_center_change_application(data):
    return f"""
To,
The Controller of Examinations,
{data['board_university']}.

Subject: Application for Change of Examination Center

Respected Sir/Madam,

I am writing to request a change in my examination center from {data['current_center']} to {data['requested_center']} due to {data['reason']}. I have attached the necessary supporting documents for your consideration.

I hope you will approve my request and make the necessary changes.

Thank you for your time.

Yours faithfully,
{data['name']}
Roll Number: {data['roll_number']}
"""

def generate_experience_certificate(data):
    return f"""
To whom it may concern,

This is to certify that Mr./Ms. {data['name']} was employed at {data['company']} as a {data['position']} from {data['start_date']} to {data['end_date']}. During this tenure, their performance was satisfactory and professional.

We found them to be punctual, hardworking, and cooperative. We wish them all the best in their future career.

HR Manager,
{data['company']}
"""

def generate_freelance_contract(data):
    return f"""
Freelance Contract Agreement

This agreement is made between {data['client_name']} (Client) and {data['freelancer_name']} (Freelancer) on {data['date']}.

Project Description:
{data['project_description']}

Payment Terms:
The client agrees to pay an amount of {data['amount']} upon successful completion of the project.

Timeline:
The project will be completed within {data['timeline']}.

Both parties agree to the terms outlined in this contract.

Client Signature: ____________
Freelancer Signature: ____________
"""

def generate_resignation_letter(data):
    return f"""
To,
The {data['authority']},
{data['company']}.

Subject: Resignation Letter

Respected Sir/Madam,

I am writing to formally resign from my position as {data['position']} at {data['company']}, effective from {data['last_working_day']}. I am grateful for the opportunities and experiences provided during my time here.

Please consider this letter as the start of my notice period. I will ensure a smooth handover of my responsibilities.

Sincerely,
{data['name']}
"""

def generate_rental_agreement(data):
    return f"""
Rental Agreement

This agreement is made on {data['date']} between the Landlord {data['landlord_name']} and the Tenant {data['tenant_name']}.

The property located at {data['property_address']} is rented for a monthly amount of {data['rent_amount']} for a period of {data['rental_period']}.

Both parties agree to abide by the terms and conditions stated in this agreement.

Landlord Signature: ____________
Tenant Signature: ____________
"""
