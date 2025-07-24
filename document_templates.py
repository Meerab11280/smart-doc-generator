def generate_cv(data):
    return f"""Curriculum Vitae

Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Address: {data['address']}

Career Summary:
{data['summary']}

Education:
{data['education']}

Experience:
{data['experience']}

Skills:
{data['skills']}

Projects:
{data['projects']}

Certifications:
{data['certifications']}
"""

def generate_leave_application(data):
    return f"""To,
The {data['authority']},
{data['institution']}

Subject: Request for Leave

Respected Sir/Madam,

I am {data['name']} from {data['class']}. I request leave from {data['start_date']} to {data['end_date']} due to {data['reason']}.

Kindly approve my leave. I shall be grateful.

Sincerely,
{data['name']}
"""

def generate_job_application(data):
    return f"""To,
HR Manager,
{data['company']}

Subject: Application for {data['position']}

Respected Sir/Madam,

I am writing to apply for the position of {data['position']} at your esteemed company. With my experience in {data['experience']} and skills in {data['skills']}, I am confident I can contribute positively.

Looking forward to your response.

Sincerely,
{data['name']}
Email: {data['email']}
"""

def generate_study_application(data):
    return f"""To,
The Admission Office,
{data['desired_institution']}

Subject: Application for Further Study

Respected Sir/Madam,

I am {data['name']}, currently studying in {data['current_program']} at {data['institution']}. I am writing to express my interest in applying for {data['desired_program']} at your institution. 

Reason for applying:
{data['reason']}

Thank you for your time and consideration.

Sincerely,
{data['name']}
"""

def generate_character_certificate(data):
    return f"""To Whom It May Concern,

This is to certify that {data['name']}, son/daughter of {data['father_name']}, was a student at {data['institution']} from {data['duration']}. During this period, their conduct was {data['behavior']}.

Principal,
{data['institution']}
"""

def generate_internship_application(data):
    return f"""To,
HR Manager,
{data['company']}

Subject: Request for Internship

Respected Sir/Madam,

I am {data['name']}, currently enrolled in the {data['program']} program at {data['institution']}. I am interested in applying for an internship opportunity at your company.

Reason:
{data['reason']}

I would be grateful for the opportunity.

Sincerely,
{data['name']}
"""

def generate_bank_account_application(data):
    return f"""To,
Branch Manager,
{data['bank_name']}

Subject: Request to Open Bank Account

Respected Sir/Madam,

I am {data['name']} bearing CNIC {data['cnic']}. I wish to open a {data['account_type']} account in your bank.

My address is:
{data['address']}

Please guide me through the process.

Sincerely,
{data['name']}
"""

def generate_fee_concession_application(data):
    return f"""To,
The Principal,
{data['institution']}

Subject: Application for Fee Concession

Respected Sir/Madam,

I am {data['name']} of class {data['class']}. I request a fee concession due to {data['reason']}. Kindly consider my request.

Sincerely,
{data['name']}
"""

def generate_exam_center_change_application(data):
    return f"""To,
The Controller of Examinations,

Subject: Application for Change of Examination Center

Respected Sir/Madam,

I am {data['name']}, Roll No. {data['roll_no']}. I request to change my exam center from {data['current_center']} to {data['desired_center']} due to {data['reason']}.

I will appreciate your kind approval.

Sincerely,
{data['name']}
"""

def generate_experience_certificate(data):
    return f"""Experience Certificate

This is to certify that {data['employee_name']} worked as a {data['position']} at {data['company_name']} from {data['duration']}. Their performance was {data['performance']}.

We wish them success in future endeavors.

HR Department,
{data['company_name']}
"""

def generate_freelance_contract(data):
    return f"""Freelance Service Agreement

This agreement is made between {data['freelancer_name']} (Freelancer) and {data['client_name']} (Client).

Service: {data['service_description']}
Rate: {data['rate']}
Duration: {data['duration']}
Payment Terms: {data['payment_terms']}

Both parties agree to the terms above.

Signed,
{data['freelancer_name']} and {data['client_name']}
"""

def generate_resignation_letter(data):
    return f"""To,
{data['company']}

Subject: Resignation Letter

Respected Sir/Madam,

I, {data['name']}, hereby resign from my position of {data['position']}. My last working day will be {data['last_day']}. Reason: {data['reason']}

Thank you for the support and opportunity.

Sincerely,
{data['name']}
"""

def generate_rental_agreement(data):
    return f"""Rental Agreement

This agreement is made between {data['landlord_name']} (Landlord) and {data['tenant_name']} (Tenant).

Property: {data['property_address']}
Monthly Rent: {data['rent_amount']}
Duration: {data['duration']}
Terms and Conditions:
{data['terms']}

Both parties agree to the terms of this agreement.

Signed,
{data['landlord_name']} and {data['tenant_name']}
"""
