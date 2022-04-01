def user_info(email, user_emails, user_storage):

    message = ''

    if email in user_emails:
        message = 'User_email =', email,'User_info:', user_storage[email]

        return message

    else:
        message = 'No user with email:', email
        return message

def all_users_info(users_storage):

    for k, v in users_storage.items():
        user_email = k
        user_info_1 = v

        print('User_email =', user_email,'User_info=', user_info_1)

