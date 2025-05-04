import re
from NumerologyLifePathDetails import NumerologyLifePathDetails

def valid_date(s: str) -> bool:
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

    num = NumerologyLifePathDetails(name, dob)

    print(f"Test Name: {num.Name}")
    print(f"Test DOB: {num.Birthdate}")
    print(f"Life Path Number: {num.LifePath}")
    print(f"Life Path Description: {num.LifePathDescription}")
    print(f"Birth Day Number: {num.BirthDay}")
    print(f"Attitude Day Number: {num.Attitude}")
    print(f"Soul Number: {num.Soul}")
    print(f"Personality Number: {num.Personality}")
    print(f"Power Name Number: {num.PowerName}")

if __name__ == "__main__":
    main()
