#Holly Buffam

from Numerology import Numerology
import re

def valid_date(s: str) -> bool:
    """
    Validate mm-dd-yyyy or mm/dd/yyyy where:
      - month 01–12
      - day   01–31
      - year  any four digits
    """
    pattern = r'^(0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])[-/]\d{4}$'
    return bool(re.match(pattern, s))

def main():
    while True:
        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue

        dob = input("Enter birthday (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        if not valid_date(dob):
            print("Invalid date format. Please use mm-dd-yyyy or mm/dd/yyyy.")
            continue
        break

    num = Numerology(name, dob)

    print(f"Test Name: {num.getName()}")
    print(f"Test DOB: {num.getBirthdate()}")
    print(f"Life Path Number: {num.getLifePath()}")
    print(f"Birth Day Number: {num.getBirthDay()}")
    print(f"Attitude Day Number: {num.getAttitude()}")
    print(f"Soul Number: {num.getSoul()}")
    print(f"Personality Number: {num.getPersonality()}")
    print(f"Power Name Number: {num.getPowerName()}")

if __name__ == "__main__":
    main()
