# Password Strength Checker

This project is a password strength checker in Python. It evaluates the strength of a password based on several criteria and also checks if the password is in a list of common passwords.

## Features

- Checks if the password contains:
  - At least 6 characters
  - At least one lowercase letter
  - At least one uppercase letter
  - At least one digit
  - At least one special character
- Checks if the password is in a list of common passwords (`commons.txt`)
- Informs the user of the password's strength (weak, medium, strong)
- Allows the user to check multiple passwords in sequence
- Error handling for user input and file reading

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/password-strength-checker.git
    cd password-strength-checker
    ```

2. Ensure you have Python installed on your machine (version 3.12.0).

3. Create a file named `commons.txt` in the project's root directory containing a list of common passwords, one password per line.

4. Run the script:
    ```bash
    python3 password_checker.py
    ```

5. Follow the on-screen instructions to enter and check passwords.

## Project Structure

- `password_checker.py`: The main script file that contains the functions for checking password strength and the main program logic.
- `commons.txt`: A text file containing the list of common passwords (one password per line).
