import re

def validate_email(email):
    # Regular expression for validating an email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

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

if __name__ == "__main__":
    binary = doc_as_binary("faty.mp4")
    binary_as_doc(binary, "faty_copy.mp4")