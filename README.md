# Email Sender

## Description:
This Python script enables the sending of personalized HTML emails to recipients specified via command line arguments.

## Setup

1. Clone this repository.
2. Ensure you have Python installed on your system.
3. Set up a virtual environment (optional but recommended).
4. Install necessary dependencies using:
    pip install -r requirements.txt
5. Create an `index.html` file in the project root with the HTML content for the email body. Use `${name}` as a placeholder for the recipient's name.

## Usage

Run the script using the command line. Provide recipient data in the format `name:email`. For example:
python email_sender.py John:john@example.com Alice:alice@example.com Bob:bob@example.com

Replace `email_sender.py` with the actual name of your Python script.

Ensure you replace `enter-your-email` and `enter-your-password` with your actual sender email and password in the script to enable successful email delivery.

## Notes

- Ensure that the HTML file (`index.html`) contains the `${name}` placeholder to personalize the email content.
- This script uses Gmail's SMTP server. Make sure to enable "less secure app access" or use an app password for Gmail.
- Please replace enter-your-email and enter-your-password with your actual email credentials for sending emails successfully. Also, ensure the index.html file contains ${name} as a placeholder for personalized content.

## Author:
- [Raghav Minhas]

## Date:
- [17-11-2023]