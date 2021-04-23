user = "Ferdi"
password = "W_c1E@2a"
attempt = input("write your first name to get password : ").lower().title()

if attempt == user :
  print("Hello {}! Your password is : {}".format(attempt, password))
else :
  print("Hello {}! See you later.".format(attempt))
