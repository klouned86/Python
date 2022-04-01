def user_update(email, name, password, phone, user_emails, user_storage):

    user_storage[email] = {'name': name,
                           'password': password,
                           'phone': phone}

    return [user_emails, user_storage]





