def generate_cv(data):
    return f"""
Curriculum Vitae

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

References:
Available upon request.
"""

def generate_leave_application(data):
    return f"""
To,
The {data['authority']},
{data['institution']},
{data['address']}

Subject: Application for Leave

Respected Sir/Madam,

I am writing to formally request leave from {data['start_date']} to {data['end_date']} due to {data['reason']}. I have ensured that my responsibilities will be managed during my absence.

I kindly request you to grant me leave for the mentioned period. I shall be thankful for your kind consideration.

Yours sincerely,
{data['name']}
{data['roll_number']}
Date: {data['date']}
"""

def generate_job_application(data):
    return f"""
To,
The Hiring Manager,
{data['company']},
{data['address']}

Subject: Job Application for the Position of {data['position']}

Respected Sir/Madam,

I am writing to express my interest in the {data['position']} position at your esteemed organization. With my background in {data['background']} and relevant experience, I am confident in my ability to contribute effectively.

I have attached my resume for your consideration. I look forward to the opportunity to discuss my application in more detail.

Sincerely,
{data['name']}
Email: {data['email']}
Phone: {data['phone']}
Date: {data['date']}
"""

def generate_further_study_application(data):
    return f"""
To,
The Head of Department,
{data['institution']},
{data['address']}

Subject: Request for Permission to Pursue Further Studies

Respected Sir/Madam,

I hope this message finds you well. I am writing to request your permission to pursue further studies in the field of {data['field_of_study']}. I believe that this academic endeavor will enhance my knowledge and skills, allowing me to contribute more effectively to my field.

I shall remain grateful for your kind approval.

Yours sincerely,
{data['name']}
Date: {data['date']}
"""

def generate_character_certificate(data):
    return f"""
Character Certificate

This is to certify that Mr./Ms. {data['name']}, son/daughter of {data['father_name']}, was a student of {data['institution']} from {data['start_year']} to {data['end_year']}. During their stay, their conduct and behavior remained satisfactory, and no disciplinary action was ever taken against them.

We wish them the best for future endeavors.

Principal
{data['institution']}
Date: {data['date']}
"""

def generate_internship_application(data):
    return f"""
To,
The HR Department,
{data['company']},
{data['address']}

Subject: Application for Internship

Respected Sir/Madam,

I am currently a student of {data['degree']} at {data['institution']}. I am writing to apply for an internship opportunity in your organization to gain practical experience in the field of {data['field']}. I am enthusiastic and eager to learn and grow under professional guidance.

Kindly consider my application. I shall be thankful.

Sincerely,
{data['name']}
Email: {data['email']}
Phone: {data['phone']}
Date: {data['date']}
"""

def generate_bank_account_application(data):
    return f"""
To,
The Branch Manager,
{data['bank_name']},
{data['branch_address']}

Subject: Request to Open Bank Account

Respected Sir/Madam,

I wish to open a savings/current account at your branch. My complete details are as follows:

Full Name: {data['name']}
CNIC: {data['cnic']}
Contact: {data['contact']}
Address: {data['address']}

I request you to kindly initiate the process and inform me about the required documentation.

Thanking you.

Sincerely,
{data['name']}
Date: {data['date']}
"""

def generate_fee_concession_application(data):
    return f"""
To,
The Principal,
{data['institution']},
{data['address']}

Subject: Application for Fee Concession

Respected Sir/Madam,

I am {data['name']}, currently enrolled in {data['class']}. Due to financial constraints at home, I am unable to pay the full tuition fee. I humbly request a fee concession so I can continue my studies without interruption.

I shall be highly obliged for your kind consideration.

Yours sincerely,
{data['name']}
Roll Number: {data['roll_number']}
Date: {data['date']}
"""

def generate_exam_center_change_application(data):
    return f"""
To,
The Controller of Examinations,
{data['university']},
{data['address']}

Subject: Request for Change of Examination Center

Respected Sir/Madam,

I am a registered student of {data['program']} under roll number {data['roll_number']}. I kindly request you to change my examination center from {data['current_center']} to {data['requested_center']} due to {data['reason']}.

Kindly consider my request at your earliest convenience.

Sincerely,
{data['name']}
Date: {data['date']}
"""

def generate_experience_certificate(data):
    return f"""
Experience Certificate

This is to certify that Mr./Ms. {data['name']} worked as a {data['designation']} at {data['company']} from {data['start_date']} to {data['end_date']}. During this period, they displayed professionalism, dedication, and efficiency in all assigned tasks.

We wish them success in future endeavors.

Authorized Signatory
{data['company']}
Date: {data['date']}
"""

def generate_freelance_contract(data):
    return f"""
Freelance Contract Agreement

This agreement is made on {data['date']} between {data['client_name']} and {data['freelancer_name']}.

The freelancer agrees to complete the project titled "{data['project_title']}" by {data['deadline']} for a total payment of {data['payment']}.

Both parties agree to the terms stated above.

Client: {data['client_name']}
Freelancer: {data['freelancer_name']}
"""

def generate_resignation_letter(data):
    return f"""
To,
The Manager,
{data['company']},
{data['address']}

Subject: Resignation from the Position of {data['position']}

Respected Sir/Madam,

Please accept this letter as formal notice of my resignation from the position of {data['position']} at {data['company']}, effective from {data['last_working_day']}. I have enjoyed working with the team and appreciate the opportunities provided.

Kindly initiate the clearance process. I am available to ensure a smooth transition.

Sincerely,
{data['name']}
Date: {data['date']}
"""

def generate_rental_agreement(data):
    return f"""
Rental Agreement

This agreement is made on {data['date']} between the landlord {data['landlord_name']} and the tenant {data['tenant_name']}.

The landlord agrees to rent the property located at {data['property_address']} for a monthly rent of {data['monthly_rent']} for a duration of {data['rental_duration']}, starting from {data['start_date']}.

Both parties agree to abide by the terms and conditions stated in this agreement.

Landlord: {data['landlord_name']}
Tenant: {data['tenant_name']}
"""
