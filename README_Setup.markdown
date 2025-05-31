# WhatsApp Message Automation Setup Guide

This guide walks you through setting up and running the WhatsApp message automation script with a polished, user-friendly process.

---

## Getting Started

**1. Verify Chrome Installation**  
Ensure Google Chrome is installed on your PC. If not, download it from google.com/chrome.

**2. Launch the Batch File**  
Double-click `RUN_THIS.bat` to begin.  
If Windows flags it as potentially harmful, proceed anyway—the script is safe, and the source code is open for review.

**3. Follow Terminal Instructions**  
Watch the colored text in the terminal for progress updates. The script will:  
- Check for Python 3.11+ and install it if missing.  
- Install necessary dependencies (e.g., Selenium).  
- Open WhatsApp Web in Chrome.  

When WhatsApp Web appears, scan the QR code using your phone’s WhatsApp app.  
Wait for the chats to load, then return to the terminal (where `RUN_THIS.bat` was run) and press any key, like Enter.

**4. Let It Run**  
The script will send messages to all numbers listed in `numbers.txt`.  
Wait for completion, then press Enter to close the browser when prompted.

---

## Editing Phone Numbers

To modify numbers:  
- Open `numbers.txt` in a text editor.  
- Ensure each number is:  
  - On a separate line.  
  - In international format with country code (e.g., +994559667744).  
  - Free of spaces or invalid formats (e.g., 055 555 55 55 is not allowed).

---

## Customizing the Message

For now, contact the developers (Ilham or Fateh) to update the message content.  
A future update will allow editing the message via a `.txt` file, similar to `numbers.txt`.

---

## Additional Notes

- An internet connection is required for Python and dependency installation.  
- The batch file is designed for Windows. For macOS/Linux, reach out to the developers for guidance.  
- If issues arise, confirm Chrome is up to date and `numbers.txt` contains valid numbers.