# Holly Buffam
# Password Validator
# February 2025

# Prompt user for their first and last name. Store name and initials.

def main():
    sName = input("Enter a full name such as John Smith: ")

    sInitials = ""
    sInitials += sName[0] + sName[sName.find(" ") + 1]

# Prompt for new password, run checks for requirements until ALL are met

    sPassword = ""
    bIsValid = False
    while not bIsValid:
        bLength = bPass = bInitials = bUpper = bLower = bDigit = bSpecial = bCount = False
        dictCharacters = {}
        sPassword = input("Enter new password: ")

        bLength = True if len(sPassword) in range(8, 13) else print("Password must be between 8 and 12 characters")

        bPass = True if not sPassword.lower().startswith("pass") else print("Password can’t start with Pass.")

        for char in sPassword:
            if char.isupper():
                bUpper = True
            elif char.islower():
                bLower = True
            elif char.isdigit():
                bDigit = True
            elif char in "!@#$%^":
                bSpecial = True

            if char in dictCharacters: continue

            iCount = sPassword.lower().count(char.lower())

            if iCount > 1: dictCharacters[char.lower()] = iCount

        if not bUpper: print("Password must contain at least 1 uppercase letter")
        if not bLower: print("Password must contain at least 1 lowercase letter")
        if not bDigit: print("Password must contain at least 1 number.")
        if not bSpecial: print("Password must contain at least 1 of these special characters: ! @ # $ % ^ ")

        bInitials = True if not sInitials.lower() in sPassword.lower() else print(
            "Password must not contain user initials. \n")

        if not dictCharacters:
            bCount = True

        else:
            dictCharacters = dict(sorted(dictCharacters.items()))
            print(f"These characters occur more than once:")
            for key, value in dictCharacters.items(): print(f"{key}: {value} times \n")

# After validating requirements and they all pass send message to user telling them password accepted

        if bLength and bPass and bInitials and bUpper and bLower and bDigit and bSpecial and bCount: bIsValid = True
    print("\nPassword is valid and OK to use.")

main()