# document_templates.py

def generate_cv(data):
    return f"""CV
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Address: {data['address']}
Education: {data['education']}
Skills: {data['skills']}
Experience: {data['experience']}
Hobbies: {data['hobbies']}
"""

def generate_leave_application(data):
    return f"""Leave Application
To,
The Principal,
{data['institution']}

Subject: Application for Leave

Respected Sir/Madam,

I am {data['name']}, a student of class {data['class']}. I request you to kindly grant me leave from {data['from_date']} to {data['to_date']} due to {data['reason']}.

Thank you.

Yours obediently,
{data['name']}
"""

def generate_job_application(data):
    return f"""Job Application
To,
The HR Manager,
{data['company']}

Subject: Application for the post of {data['position']}

Dear Sir/Madam,

I am writing to express my interest in the {data['position']} position at your company. I have completed {data['education']} and have experience in {data['experience']}. I believe I can contribute effectively to your team.

Sincerely,
{data['name']}
"""

def generate_further_study_application(data):
    return f"""Further Study Application
To,
The Head of Department,
{data['institution']}

Subject: Request for Permission for Further Studies

Respected Sir/Madam,

I am {data['name']}, currently working as a {data['designation']}. I request permission to pursue further studies in {data['field']} to enhance my skills and knowledge.

Regards,
{data['name']}
"""

def generate_character_certificate(data):
    return f"""Character Certificate
To Whom It May Concern,

This is to certify that Mr./Ms. {data['name']} S/O or D/O {data['parent_name']} was a student of {data['institution']} from {data['from_year']} to {data['to_year']}. During this period, their conduct and character remained satisfactory.

Principal,
{data['institution']}
"""

def generate_internship_application(data):
    return f"""Internship Application
To,
The Manager,
{data['organization']}

Subject: Application for Internship

Dear Sir/Madam,

I am {data['name']}, currently studying in {data['program']} at {data['university']}. I am interested in doing an internship at your organization to gain practical experience in the field of {data['field']}.

Sincerely,
{data['name']}
"""

def generate_bank_account_application(data):
    return f"""Bank Account Opening Application
To,
The Branch Manager,
{data['bank_name']}

Subject: Application to Open a Bank Account

Respected Sir/Madam,

I am {data['name']}, residing at {data['address']}. I request you to kindly open a savings account in my name. I have attached all required documents.

Thank you.

Sincerely,
{data['name']}
"""

def generate_fee_concession_application(data):
    return f"""Fee Concession Application
To,
The Principal,
{data['institution']}

Subject: Application for Fee Concession

Respected Sir/Madam,

I am {data['name']} of class {data['class']}. I belong to a financially weak background and request you to kindly grant me a fee concession.

Thank you.

Yours obediently,
{data['name']}
"""

def generate_exam_center_change_application(data):
    return f"""Examination Center Change Application
To,
The Controller of Examinations,
{data['university']}

Subject: Request for Change of Examination Center

Respected Sir/Madam,

I am {data['name']}, a student of {data['program']}. Due to {data['reason']}, I request a change in my examination center from {data['current_center']} to {data['preferred_center']}.

Regards,
{data['name']}
"""

def generate_experience_certificate(data):
    return f"""Experience Certificate
To Whom It May Concern,

This is to certify that Mr./Ms. {data['name']} has worked as a {data['designation']} at {data['company']} from {data['start_date']} to {data['end_date']}. Their performance during the period was satisfactory.

Authorized Signatory,
{data['company']}
"""

def generate_freelance_contract(data):
    return f"""Freelance Contract
This agreement is made between {data['freelancer_name']} and {data['client_name']} on {data['date']}. The freelancer agrees to deliver the following services: {data['services']}.

Payment will be made as per the discussed terms. Both parties agree to the terms and conditions of this contract.

Freelancer: {data['freelancer_name']}
Client: {data['client_name']}
"""

def generate_resignation_letter(data):
    return f"""Resignation Letter
To,
The Manager,
{data['company']}

Subject: Resignation Letter

Dear Sir/Madam,

I am writing to formally resign from my position as {data['designation']} at {data['company']} effective from {data['resignation_date']}.

Thank you for the opportunities I have received during my time at the company.

Sincerely,
{data['name']}
"""

def generate_rental_agreement(data):
    return f"""Rental Agreement
This agreement is made on {data['date']} between the landlord {data['landlord_name']} and the tenant {data['tenant_name']}.

The property located at {data['property_address']} will be rented for {data['rent_amount']} per month for a period of {data['rental_period']}.

Both parties agree to the terms and conditions stated in this agreement.

Landlord: {data['landlord_name']}
Tenant: {data['tenant_name']}
"""
