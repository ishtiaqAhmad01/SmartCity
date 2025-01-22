logined_cnic = None

def set_user_id(user):
    global logined_cnic
    logined_cnic = user

def get_user_id():
    return logined_cnic