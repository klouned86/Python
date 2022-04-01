from create_1 import create_user
from read import user_info, all_users_info
from update import  user_update
from delete import  user_delete
user_emails = []
user_storage = {}

while True:

    action = input('enter action  ')

    if action == 'cr':
        print('action =', action)

        email = input('Email: ')
        name = input('name: ')
        password = input('password: ')
        phone = input('phone: ')

        user_emails = create_user(email, name, password, phone, user_emails, user_storage)

        print('user_emails =', user_emails)
        print('user_storage = ', user_storage)


    elif action == 'r_all':
        print('action =', action)
        all_users_info(user_storage)
    elif action == 'r_user':
        user_e = input('Enter user email')
        message = user_info(user_e, user_emails, user_storage)
        print('action =', action)
        print('User :', message)



    elif action == 'up':
        print('action =', action)
        user_up = input('Enter update email ')
        name = input('name: ')
        password = input('password: ')
        phone = input('phone: ')

        user_update(user_up, name, password, phone, user_emails, user_storage)

        print(user_emails)
        print(user_storage)

    elif action == 'del':
        print('action =', action)
        del_user = input('Enter delete email ')
        user_delete(del_user, user_emails, user_storage)

        print(user_emails)
        print(user_storage)


    else:
        print('action = incorrect input')