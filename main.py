# Asking User Name
user_name = input("Enter The User-Name : ")
print("\n")
gmail = input("Enter The E-Mail : ")
print("\n")
password = input("Enter The Password : ")
print("\n")

# Repeated Passwords Are Saved Here As Strings.
repeat_user_name = ("Your Name Is - ", user_name)
repeat_gmail = ("Your E-Mail Is - ", gmail)
repeat_password = ("Your Password Is - ", password)

# Consider the clipboard history:

forget_gmail = input("You Forget The E-Mail ? (Yes/No) : ")

if forget_gmail == "Yes":
    print(repeat_gmail)
elif forget_gmail == "No":
    print("Database Has Your E-Mail Saved", "End To End Encrypted")
else:
    print("The DataBase Is Working")

print("\n")

forget_password = input("You Forget The Password ? (Yes/No) : ")

if forget_password == "Yes":
    print(repeat_password)
elif forget_password == "No":
    print("Database Has Your Password Saved\n", "End To End Encrypted")
else:
    print("The DataBase Is Working")
