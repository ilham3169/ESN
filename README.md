# ESN 
WhatsApp Message Automation Setup Guide
This guide explains how to set up and run the WhatsApp message automation script.

What You Need to Do

Ensure Chrome is Installed:

You must have Google Chrome installed on your PC. Download it from google.com/chrome if you don’t have it.


Run the Batch File:

Double-click RUN_THIS.bat to start the process.
If Windows warns that the file might be harmful, ignore it and run anyway. The script is safe, and the source code is available for review.


Follow the Terminal Instructions:

Read the colored text in the terminal for status updates.
The script will:
Check and install Python if it’s not on your PC.
Install required dependencies (e.g., Selenium).
Open WhatsApp Web in Chrome.


When WhatsApp Web loads, scan the QR code with your phone’s WhatsApp app.
Wait for the chats to load in the browser.
Return to the terminal (where you ran RUN_THIS.bat) and press any key (e.g., Enter).


Wait for Completion:

The script will send messages to all numbers listed in numbers.txt.
Wait until the process finishes. Press Enter to close the browser when prompted.




Editing Phone Numbers

Open numbers.txt to add or edit phone numbers.
Each number must:
Be on a separate line.
Include the country code (e.g., +994559667744).
Not use spaces or invalid formats (e.g., 055 555 55 55 is not acceptable).




Editing the Message

For now, contact the developer ( meeeee - ilham and **Fateh**inko dombilinko ) to change the message content.
In the next update, you’ll be able to edit the message via a .txt file, similar to numbers.txt.


Notes

Ensure you have an internet connection for Python and dependency installation.
The batch file is Windows-only. Contact the developer for macOS/Linux instructions.
If you encounter issues, verify Chrome is updated and numbers.txt contains valid numbers.

