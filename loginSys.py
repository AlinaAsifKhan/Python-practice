correct_username = "alinakhan"
correct_password = "lin123"
max_attempts = 3

print("----Basic Login System----")

for attempt in range(max_attempts):
  try:
      username = input("Enter username: ")
      password = input("Enter password: ")

      if username.strip() == "" or password.strip() == "":
          print("⚠ Fields cannot be empty. Please try again.\n")
          continue 

      if username == correct_username and password == correct_password:
          print("\n Login Successful! Welcome,", username)
          break
      else:
          if username != correct_username and password != correct_password:
              print(" Both username and password are incorrect.")
          elif username != correct_username:
              print(" Username is incorrect.")
          else:
              print(" Password is incorrect.")

          remaining = max_attempts - (attempt + 1)
          if remaining > 0:
              print(f"Attempts left: {remaining}\n")
          else:
              print("\n Login Failed! No attempts left.")
  except KeyboardInterrupt:
      print("\nLogin process interrupted. Exiting...")
      break