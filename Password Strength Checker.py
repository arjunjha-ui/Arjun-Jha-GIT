#!/usr/bin/env python
# coding: utf-8

# In[23]:


import re

def check_password_strength(password):
    feedback = []

    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    has_length = len(password) >= 8
    has_space = " " in password

    # Feedback only for failed checks
    if not has_length:
        feedback.append("Password should be at least 8 characters long.")
    if not has_upper:
        feedback.append("Add at least one uppercase letter.")
    if not has_lower:
        feedback.append("Add at least one lowercase letter.")
    if not has_digit:
        feedback.append("Add at least one digit.")
    if not has_special:
        feedback.append("Add at least one special character.")
    if has_space:
        feedback.append("Password should not contain spaces.")

    # Strength calculation
    score = sum([has_length, has_upper, has_lower, has_digit, has_special]) 

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


# In[25]:


password = input("Enter your password:")
strength , suggestions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if suggestions:
    print("Suggestions:")
    for s in suggestions :
        print("-", s)


# In[ ]:




