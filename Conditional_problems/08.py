#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).



char = "rt656434esxf"
char_length = len(char)

if len(char)<6:
    strength = "weak"
elif len(char)<=10:
    strength="medium"
else:
    strength="strong"

print("password strength is :", strength)