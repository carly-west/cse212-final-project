accounts = {"user232@abc.com", "email1211@email.com", "user909@yahoo.com", "email@gmail.com", "email1231@yahoo.com", "user10101@outlook.com", "user123@yahoo.com"}

new_accounts = {"email@gmail.com", "user123@yahoo.com", "testing222@outlook.com", "tests1233@yahoo.com", "snailmail@gmail.com", "user10101@outlook.com"}

# Check for any repeat accounts
print(accounts & new_accounts)

# Create a new set with all of the unique emails
unique_accounts = accounts | new_accounts

count = 0

# Loop through old user list, and count the number of new accounts added
for user in accounts:
  if user in new_accounts:
    count += 1

print(count)
# Expected output: 3
