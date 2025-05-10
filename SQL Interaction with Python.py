import sqlite3
import csv
import os

DB_FILE = "retirement.db"

def part1_create_and_import(cursor):

    # Drop & recreate tables
    cursor.execute("DROP TABLE IF EXISTS Employee")
    cursor.execute("DROP TABLE IF EXISTS Pay")
    cursor.execute("DROP TABLE IF EXISTS SocialSecurityMin")

    cursor.execute("""
        CREATE TABLE Employee (
            EmployeeID   INTEGER PRIMARY KEY,
            Name         TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE Pay (
            EmployeeID   INTEGER,
            Year         INTEGER,
            Earnings     REAL,
            FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
        )
    """)
    cursor.execute("""
        CREATE TABLE SocialSecurityMin (
            Year         INTEGER PRIMARY KEY,
            Minimum      REAL
        )
    """)
     #print("  • Tables Employee, Pay & SocialSecurityMin created.")

    #  Import each text file, skipping header
    def bulk_insert(txt_filename, insert_sql, converter):
        count = 0
        with open(txt_filename, newline="") as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                cursor.execute(insert_sql, converter(row))
                count += 1
        return count

    emp_count = bulk_insert(
        "Employee.txt",
        "INSERT INTO Employee(EmployeeID, Name) VALUES (?, ?)",
        lambda r: (int(r[0]), r[1].strip())
    )
    pay_count = bulk_insert(
        "Pay.txt",
        "INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES (?, ?, ?)",
        lambda r: (int(r[0]), int(r[1]), float(r[2]))
    )
    min_count = bulk_insert(
        "SocialSecurityMinimum.txt",
        "INSERT INTO SocialSecurityMin(Year, Minimum) VALUES (?, ?)",
        lambda r: (int(r[0]), float(r[1]))
    )


def part2_report(cursor):


    sql = """
    SELECT E.Name, P.Year, P.Earnings, S.Minimum
      FROM Employee E
      JOIN Pay P               ON E.EmployeeID = P.EmployeeID
      JOIN SocialSecurityMin S ON P.Year       = S.Year
     ORDER BY E.Name, P.Year
    """
    cursor.execute(sql)

    # print header
    print(f"{'Employee Name':<20} {'Year':<6} {'Earnings':>12} {'Minimum':>12} {'Include':>8}")
    # each row
    for name, year, earn, minimum in cursor.fetchall():
        include = "Yes" if earn >= minimum else "No"
        print(f"{name:<20} {year:<6} {earn:12,.2f} {minimum:12,.2f} {include:>8}")

def main():
    # remove old DB so Part1 always starts fresh
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Part 1
    part1_create_and_import(cur)
    conn.commit()

    # Part 2
    part2_report(cur)

    conn.close()

if __name__ == "__main__":
    main()
