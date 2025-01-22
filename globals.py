logined_cnic = '3660245605291'

def set_user_id(user):
    global logined_cnic
    logined_cnic = user

def get_user_id():
    return logined_cnic