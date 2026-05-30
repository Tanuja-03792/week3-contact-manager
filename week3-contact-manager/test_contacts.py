from contacts_manager import validate_phone
from contacts_manager import validate_email

print(
validate_phone(
"9876543210"
))

print(
validate_phone(
"+91 9876543210"
))

print(
validate_email(
"abc@gmail.com"
))

print(
validate_email(
"wrongmail"
))