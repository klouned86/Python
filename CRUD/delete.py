def user_delete(email, user_emails, user_storage):

   del user_storage[email]
   user_emails.remove(email)

   return[user_emails, user_storage]