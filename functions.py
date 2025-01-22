import re
import bcrypt
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def table_style():
    return """
        QTableWidget {
            background-color: #F9FBFD;
            border: 1px solid #D3D9DE;
            border-radius: 8px;
            font-size: 14px;
            gridline-color: #E0E0E0;
        }
        QHeaderView::section {
            background-color: #5DADE2;
            color: white;
            font-weight: bold;
            padding: 8px;
            border: none;
        }
        QTableWidget::item {
            padding: 5px;
        }
        QScrollBar:vertical {
            border: none;
            background: #ECF0F1;
            width: 10px;
        }
    """

def line_edit_style_rounded():
    return """
        QLineEdit {
            background-color: #FBFCFC;
            border: 2px solid #D5DBDB;
            border-radius: 10px;
            padding: 8px;
            font-size: 14px;
            color: #2C3E50;
        }
        QLineEdit:hover {
            border-color: #3498DB;
        }
        QLineEdit:focus {
            border-color: #2980B9;
            background-color: #F0F3F4;
        }
    """

def tab_style():
    return """
        QTabWidget::pane {
            border: 1px solid #D6DBDF;
            background: #F2F4F4;
            border-radius: 8px;
        }
        QTabBar::tab {
            background: #3498DB;
            color: white;
            font-size: 15px;
            padding: 8px 15px;
            border-radius: 5px;
            margin: 2px;
            width: 180px;
        }
        QTabBar::tab:hover {
            background: #2980B9;
        }
        QTabBar::tab:selected {
            background: #1A5276;
            font-weight: bold;
        }
        QPushButton {
            background-color: #27AE60;
            color: white;
            border-radius: 5px;
            padding: 8px 12px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #229954;
        }
    """

def spin_box_style():
    return """
        QSpinBox, QDoubleSpinBox {
            background-color: #FBFCFC;
            border: 2px solid #D5DBDB;
            border-radius: 10px;
            padding: 8px;
            font-size: 14px;
            color: #2C3E50;
        }

        QSpinBox::up-arrow, QDoubleSpinBox::up-arrow,
        QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {
            width: 8px;
            height: 8px;
        }
    """

def send_bill_email(to_email, pdf_path, bill_info):
    # Email credentials
    sender_email = "unifiedcityservicesplatform@gmail.com"
    sender_password = "bajogglnmhmxpljy"

    # Email subject and body
    subject = f"Utility Bill for {bill_info['bill_type']} - Due {bill_info['due_date']}"
    body = f"""
    Dear Customer,

    Please find attached your utility bill for {bill_info['bill_type']}.

    Bill Summary:
    - Amount Before Due: Rs {bill_info['amount_before_due']:.2f}
    - Tax: Rs {bill_info['tax_amount']:.2f}
    - Late Fee: Rs {bill_info['late_fee']:.2f}
    - Total Amount Due: Rs {bill_info['amount_after_due']:.2f}
    - Due Date: {bill_info['due_date']}

    Please make your payment before the due date to avoid additional charges.

    Thank you,
    Unified City Services Platform
    """

    # Creating the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_attachment = MIMEBase('application', 'octet-stream')
            pdf_attachment.set_payload(pdf_file.read())
            encoders.encode_base64(pdf_attachment)
            pdf_attachment.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(pdf_path)}'
            )
            msg.attach(pdf_attachment)
    except Exception as e:
        print(f"Error attaching PDF: {e}")
        return False

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Utility bill successfully sent to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def generate_otp(length=6):
    otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
    return otp

def send_email(to_email, otp):
    """
    Send the generated OTP via email.
    """
    import os

    sender_email = "unifiedcityservicesplatform@gmail.com"
    sender_password = "bajogglnmhmxpljy"

    subject = "Verification Code"
    html_content = f"""
            <!DOCTYPE html>
        <html>
        <head>
            <title>Verification Code</title>
        </head>
        <body style="font-family: Helvetica, Arial, sans-serif; margin: 0px; padding: 0px; background-color: #ffffff;">
            <table role="presentation" style="width: 100%; padding: 20px; background-color: #ffffff;">
                <tr>
                    <td align="center">
                        <table role="presentation" style="max-width: 600px; width: 100%; background-color: #d3d3d3; padding: 20px; border-radius: 10px;">
                            <tr>
                                <td style="text-align: left;">
                                    <h1 style="margin: 0; color: #333;">Verification Code</h1>
                                    <p style="padding-bottom: 16px; color: #555;">Use the following verification code to complete your login:</p>
                                    <h2 style="font-size: 130%; color: #333;"><strong>{otp}</strong></h2>
                                    <p style="color: #555;">If you did not request this, please ignore this email.</p>
                                    <p style="color: #555;">Thanks,<br>Unified City Services Platform, Team</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
    """

    # Creating the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"OTP successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$UpNSAeZLLDqh0CNTxSaRJe')
    return hashed

def pakistan_provinces():
    return ['Punjab', 'Sindh', 'Balochistan', 'Khyber Pakhtunkhwa', 'Gilgit-Baltistan', 'Azad Jammu and Kashmir']

def provinces_districts(province):
    province_to_districts = {
    "Punjab": [
        "Lahore", "Rawalpindi", "Faisalabad", "Multan", "Gujranwala", "Sialkot",
        "Sargodha", "Bahawalpur", "Sheikhupura", "Kasur", "Jhelum", "Mianwali"
    ],
    "Sindh": [
        "Karachi", "Hyderabad", "Sukkur", "Mirpurkhas", "Larkana", "Nawabshah",
        "Dadu", "Badin", "Thatta", "Shikarpur", "Jamshoro"
    ],
    "Khyber Pakhtunkhwa": [
        "Peshawar", "Mardan", "Abbottabad", "Swat", "Dera Ismail Khan", "Kohat",
        "Bannu", "Charsadda", "Nowshera", "Hangu"
    ],
    "Balochistan": [
        "Quetta", "Gwadar", "Sibi", "Kalat", "Mastung", "Khuzdar", "Chagai",
        "Pishin", "Zhob", "Loralai"
    ],
    "Azad Jammu and Kashmir": [
        "Muzaffarabad", "Mirpur", "Rawalakot", "Bhimber", "Kotli", "Poonch",
        "Neelum", "Bagh", "Sudhnoti"
    ],
    "Gilgit-Baltistan": [
        "Gilgit", "Skardu", "Hunza", "Diamer", "Ghizer", "Astore"
    ]
    }
    return province_to_districts.get(province, [])

def district_tehsils(district):
    district_to_tehsils = {
    "Lahore": ["Lahore City", "Raiwind", "Shalimar", "Balloki"],
    "Rawalpindi": ["Rawalpindi City", "Murree", "Taxila", "Kotli Sattian"],
    "Faisalabad": ["Faisalabad City", "Jaranwala", "Samundri", "Tandlianwala"],
    "Multan": ["Multan City", "Khanewal", "Shujabad", "Lodhran"],
    "Gujranwala": ["Gujranwala City", "Wazirabad", "Kamoke", "Gakkhar Mandi"],
    "Sialkot": ["Sialkot City", "Daska", "Sambrial", "Pasrur"],
    "Sargodha": ["Sargodha City", "Bhalwal", "Sahiwal", "Jhawarian"],
    "Bahawalpur": ["Bahawalpur City", "Hasilpur", "Ahmedpur East", "Yazman"],
    "Sheikhupura": ["Sheikhupura City", "Faisalabad", "Muridke", "Safdarabad"],
    "Kasur": ["Kasur City", "Pattoki", "Chunian", "Kot Radha Kishan"],
    "Jhelum": ["Jhelum City", "Pind Dadan Khan", "Chakwal", "Khewra"],
    "Karachi": ["Karachi Central", "Karachi East", "Karachi West", "Korangi", "Malir", "Southeast"],
    "Hyderabad": ["Hyderabad City", "Tando Allahyar", "Tando Muhammad Khan", "Badin"],
    "Sukkur": ["Sukkur City", "Rohri", "Pano Akil", "Ghotki"],
    "Mirpurkhas": ["Mirpurkhas City", "Digri", "Tando Jan Mohammad", "Sindhri"],
    "Larkana": ["Larkana City", "Shahdadkot", "Ratodero", "Baqarani"],
    "Nawabshah": ["Nawabshah City", "Sanghar", "Daur", "Shahpur"],
    "Dadu": ["Dadu City", "Khairpur Nathan Shah", "Johi", "Mehar"],
    "Badin": ["Badin City", "Matli", "Talhar", "Khoski"],
    "Thatta": ["Thatta City", "Sujawal", "Ghorabari", "Jati"],
    "Shikarpur": ["Shikarpur City", "Lakhi", "Garhi Yasin", "Kadhiro"],
    "Jamshoro": ["Jamshoro City", "Manjhand", "Kotri", "Indus"],
    "Quetta": ["Quetta City", "Pishin", "Kalat", "Zhob", "Chagai"],
    "Gwadar": ["Gwadar City", "Pasni", "Ormara", "Turbat"],
    "Sibi": ["Sibi City", "Kachhi", "Sibbi", "Dera Bugti"],
    "Kalat": ["Kalat City", "Khuzdar", "Mastung", "Awaran"],
    "Mastung": ["Mastung City", "Kalat", "Khuzdar", "Loralai"],
    "Khuzdar": ["Khuzdar City", "Mastung", "Awaran", "Loralai"],
    "Loralai": ["Loralai City", "Khuzdar", "Mastung", "Awaran"],
    "Chagai": ["Chagai City", "Nushki", "Kharan", "Panjgur"],
    "Peshawar": ["Peshawar City", "Charsadda", "Nowshera", "Mardan"],
    "Abbottabad": ["Abbottabad City", "Havelian", "Haripur", "Mansehra"],
    "Swat": ["Swat City", "Mingora", "Kalam", "Matta"],
    "Dera Ismail Khan": ["Dera Ismail Khan City", "Dera Khushab", "Tanki"],
    "Kohat": ["Kohat City", "Lachi", "Teri", "Hangu"],
    "Bannu": ["Bannu City", "Bannu Rural", "Lakki Marwat", "Dera Ismail Khan"],
    "Charsadda": ["Charsadda City", "Mardan", "Nowshera", "Peshawar"],
    "Nowshera": ["Nowshera City", "Charsadda", "Mardan", "Peshawar"],
    "Hangu": ["Hangu City", "Kohat", "Lachi", "Teri"],
    "FATA": ["Khyber Agency", "South Waziristan", "North Waziristan", "Kurram Agency"],
    "Muzaffarabad": ["Muzaffarabad City", "Rawalakot", "Bhimber", "Kotli"],
    "Mirpur": ["Mirpur City", "Dadyal", "Jhelum Valley", "Chakswari"],
    "Rawalakot": ["Rawalakot City", "Bagh", "Kotli", "Bhimber"],
    "Bhimber": ["Bhimber City", "Mirpur", "Jhelum Valley", "Chakswari"],
    "Kotli": ["Kotli City", "Mirpur", "Bhimber", "Rawalakot"],
    "Poonch": ["Poonch City", "Bagh", "Chakswari", "Sudhnoti"],
    "Neelum": ["Neelum Valley", "Muzaffarabad", "Rawalakot", "Bhimber"],
    "Bagh": ["Bagh City", "Poonch", "Sudhnoti", "Chakswari"],
    "Sudhnoti": ["Sudhnoti City", "Bagh", "Poonch", "Chakswari"],
    "Gilgit": ["Gilgit City", "Hunza", "Diamer", "Ghizer"],
    "Skardu": ["Skardu City", "Shigar", "Kharmang", "Rondu"],
    "Hunza": ["Hunza City", "Gilgit", "Diamer", "Ghizer"],
    "Diamer": ["Diamer City", "Hunza", "Ghizer", "Skardu"],
    "Ghizer": ["Ghizer City", "Diamer", "Hunza", "Skardu"],
    "Astore": ["Astore City", "Diamer", "Gilgit", "Skardu"]
    }
    return district_to_tehsils.get(district, [])

def majorProblem_to_subProblem(majorProblem):
    smart_city_issues = {
    "Electrical": [
        "Power Grid Management", 
        "Renewable Energy Integration", 
        "Electric Vehicle (EV) Charging Infrastructure", 
        "Energy Consumption Monitoring", 
        "Streetlight Automation", 
        "Energy Distribution Efficiency"
    ],
    "Plumbing": [
        "Water Leak Detection", 
        "Water Quality Monitoring", 
        "Sewer System Management", 
        "Water Conservation", 
        "Wastewater Treatment Optimization", 
        "Pressure Monitoring"
    ],
    "Potholes": [
        "Road Surface Monitoring", 
        "Automated Reporting Systems", 
        "Pothole Repair Scheduling", 
        "Material Quality Tracking", 
        "Public Notification Systems", 
        "Damage Severity Assessment"
    ],
    "Street Lighting": [
        "Smart Lighting Systems", 
        "Energy-Efficient Lighting", 
        "Lighting Maintenance", 
        "Traffic Adaptive Lighting", 
        "Public Safety Lighting", 
        "Integration with Smart City Infrastructure"
    ],
    "Garbage": [
        "Waste Collection Optimization", 
        "Recycling Systems", 
        "Waste-to-Energy Systems", 
        "Waste Monitoring", 
        "Public Awareness Programs", 
        "Landfill Management"
    ]
    }
    return smart_city_issues.get(majorProblem, [])  

def doc_as_binary(image_path):
    try:
        with open(image_path, 'rb') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def binary_as_doc(binary_data, output_path):
    try:
        with open(output_path, 'wb') as file:
            file.write(binary_data)
        print(f"File written successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def offices(type):
    offices = {
        "Passport Renewal": [
            "Garden Town",
            "Shalimar",
            "Raiwind",
            "Defence (DHA)",
            "Shahdrah"
        ],
        "CNIC Issuance": [
            "Allama Iqbal Town",    
            "DHA Phase 1",
            "Township",
            "DHA Phase 4",
            "Data Gunj Buksh",
            "Edgerton Road"
        ],
        "Driver's License": [
            "Farid Kot Road"
        ]
    }
    return offices[type]



if __name__ == "__main__":
    bill_info_example = {
        "bill_type": "Electricity",
        "amount_before_due": 5000.00,
        "tax_amount": 500.00,
        "late_fee": 550.00,
        "amount_after_due": 6050.00,
        "due_date": "2025-01-15"
    }

    pdf_path = "utility_bill_updated.pdf"
    recipient_email = "ahmadziachaudhary44@gmail.com"

    if send_bill_email(recipient_email, pdf_path, bill_info_example):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")


