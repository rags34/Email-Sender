import smtplib
import sys 
from email.message import EmailMessage
from string import Template
from pathlib import Path  
import re 

# Function to check whether the email format is correct using regex
def is_valid_email(email):
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(email_pattern.match(email))

# Read the text from the HTML file using string.Template() and pathlib.Path()
html = Template(Path('index.html').read_text())

# Save the command line arguments in a list, excluding the name of the file
args = sys.argv[1:]

# Check if any command line arguments are provided
if len(args) == 0:
    print("No command line arguments provided. Please provide the necessary arguments.")
    sys.exit(1)

# Create a dict to store the data in name:email form
recipient_data = {}

# Saving the valid key,value pairs in the dict
for arg in args:
    if ':' in arg:
        name, email = arg.split(':', 1)
        if is_valid_email(email):
            recipient_data[name] = email
        else:
            print(f"Invalid email format for '{arg}'. Skipping.")
    else:
        email = arg
        if is_valid_email(email):
            recipient_data[email] = email
        else:
            print(f"Invalid email format for '{arg}'. Skipping.")

# If no valid recipient data is provided, exit the program
if not recipient_data:
    print("No valid recipient data provided.")
    sys.exit()

# Your login credentials
#You can use this code too if you want to send bulk email just change the values of sender_email and password variables which I have omitted for obvious reasons
sender_email = "enter-your-email"
password = "enter-your-password"

# Loop through each recipient's data and send individual emails
for name, email in recipient_data.items():
    # Create the EmailMessage object for each recipient
    message = EmailMessage()
    message["Subject"] = f"A Personalized HTML Email for You {name}"
    message["From"] = sender_email 
    message["To"] = f"{name} <{email}>"

    # Replace placeholders in the HTML template with the recipient's name
    personalized_content = html.substitute(name=name)
    message.add_alternative(personalized_content, subtype='html')

    # Use SMTP to send the email
    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
        smtp.starttls()
        smtp.login(sender_email, password)
        smtp.send_message(message)


#print when the program is sucessfully completed
print("Email sent successfully!")
