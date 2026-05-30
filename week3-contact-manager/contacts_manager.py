import json
import re
import csv
from datetime import datetime

CONTACT_FILE = "contacts_data.json"

contacts = {}


# ---------------- PHONE VALIDATION ----------------

def validate_phone(phone):

    digits = re.sub(r'\D', '', phone)

    if 10 <= len(digits) <= 15:
        return True, digits

    return False, None


# ---------------- EMAIL VALIDATION ----------------

def validate_email(email):

    if email == "":
        return True

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return re.match(pattern, email) is not None


# ---------------- ADD CONTACT ----------------

def add_contact():

    print("\nADD CONTACT")

    name = input("Enter Name: ").strip()

    if name == "":
        print("Name cannot be empty")
        return

    if name in contacts:

        print("Contact already exists")

        choice = input(
            "Update existing contact? (y/n): "
        ).lower()

        if choice == "y":
            update_contact(name)

        return

    while True:

        phone = input(
            "Enter Phone Number: "
        )

        valid, cleaned = validate_phone(phone)

        if valid:
            break

        print(
            "Invalid phone number"
        )

    while True:

        email = input(
            "Enter Email: "
        ).strip()

        if validate_email(email):
            break

        print(
            "Invalid email"
        )

    address = input(
        "Enter Address: "
    )

    group = input(
        "Enter Group: "
    )

    if group == "":
        group = "Other"

    contacts[name] = {

        "phone": cleaned,

        "email": email,

        "address": address,

        "group": group,

        "created_at":
        datetime.now().isoformat(),

        "updated_at":
        datetime.now().isoformat()

    }

    save_to_file()

    print("Contact Added")


# ---------------- SEARCH CONTACT ----------------

def search_contact():

    text = input(
        "Search Name: "
    ).lower()

    found = False

    for name, info in contacts.items():

        if text in name.lower():

            found = True

            print("\nName:", name)

            print(
                "Phone:",
                info["phone"]
            )

            print(
                "Email:",
                info["email"]
            )

            print(
                "Address:",
                info["address"]
            )

            print(
                "Group:",
                info["group"]
            )

    if not found:
        print("No Contact Found")


# ---------------- UPDATE CONTACT ----------------

def update_contact(existing_name=None):

    if existing_name:

        name = existing_name

    else:

        name = input(
            "Enter Contact Name: "
        )

    if name not in contacts:

        print("Contact not found")

        return

    phone = input(
        "New Phone: "
    )

    valid, cleaned = validate_phone(phone)

    if valid:

        contacts[name][
            "phone"
        ] = cleaned

    email = input(
        "New Email: "
    )

    if validate_email(email):

        contacts[name][
            "email"
        ] = email

    address = input(
        "New Address: "
    )

    contacts[name][
        "address"
    ] = address

    group = input(
        "New Group: "
    )

    contacts[name][
        "group"
    ] = group

    contacts[name][
        "updated_at"
    ] = datetime.now().isoformat()

    save_to_file()

    print("Updated Successfully")


# ---------------- DELETE ----------------

def delete_contact():

    name = input(
        "Delete Contact Name: "
    )

    if name not in contacts:

        print(
            "Contact not found"
        )

        return

    confirm = input(
        "Confirm delete (y/n): "
    )

    if confirm.lower() == "y":

        del contacts[name]

        save_to_file()

        print("Deleted")


# ---------------- DISPLAY ----------------

def display_all():

    if len(contacts) == 0:

        print(
            "No Contacts"
        )

        return

    print(
        "\nALL CONTACTS\n"
    )

    for name, info in contacts.items():

        print(
            "Name:",
            name
        )

        print(
            "Phone:",
            info["phone"]
        )

        print(
            "Email:",
            info["email"]
        )

        print(
            "Address:",
            info["address"]
        )

        print(
            "Group:",
            info["group"]
        )

        print(
            "-" * 30
        )


# ---------------- SAVE ----------------

def save_to_file():

    with open(
        CONTACT_FILE,
        "w"
    ) as file:

        json.dump(
            contacts,
            file,
            indent=4
        )


# ---------------- LOAD ----------------

def load_file():

    global contacts

    try:

        with open(
            CONTACT_FILE,
            "r"
        ) as file:

            contacts = json.load(
                file
            )

    except:

        contacts = {}


# ---------------- CSV EXPORT ----------------

def export_csv():

    with open(
        "contacts.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(
            file
        )

        writer.writerow([

            "Name",

            "Phone",

            "Email",

            "Address",

            "Group"

        ])

        for name, info in contacts.items():

            writer.writerow([

                name,

                info["phone"],

                info["email"],

                info["address"],

                info["group"]

            ])

    print(
        "CSV Exported"
    )


# ---------------- STATISTICS ----------------

def statistics():

    total = len(
        contacts
    )

    print(
        "\nTotal Contacts:",
        total
    )

    groups = {}

    for info in contacts.values():

        g = info[
            "group"
        ]

        groups[g] = groups.get(
            g,
            0
        ) + 1

    print(
        "\nGroup Statistics"
    )

    for k, v in groups.items():

        print(
            k,
            ":",
            v
        )


# ---------------- MENU ----------------

def menu():

    load_file()

    while True:

        print("""

CONTACT MANAGEMENT SYSTEM

1 Add Contact
2 Search Contact
3 Update Contact
4 Delete Contact
5 View Contacts
6 Export CSV
7 Statistics
8 Exit

""")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            add_contact()

        elif choice == "2":

            search_contact()

        elif choice == "3":

            update_contact()

        elif choice == "4":

            delete_contact()

        elif choice == "5":

            display_all()

        elif choice == "6":

            export_csv()

        elif choice == "7":

            statistics()

        elif choice == "8":

            save_to_file()

            print(
                "Thank You"
            )

            break

        else:

            print(
                "Invalid Choice"
            )


menu()