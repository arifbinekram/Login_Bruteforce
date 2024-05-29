# Login Brute Force Project

This repository contains scripts and tools for performing brute force attacks on login forms for educational and testing purposes. The project demonstrates how to use Python to automate the brute force process against a web login form.

## Features

- **Brute Force Script**: The main script to perform brute force attacks on login forms.
- **Customizable**: Easily modify the script to target different login forms and adjust parameters such as the wordlist and request structure.
- **Logging**: Keeps track of attempts and successful logins.

## Prerequisites

- Python 3.x
- `requests` library

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine using:
```sh
git clone https://github.com/arifbinekram/Login_Bruteforce.git
```

Navigate to the project directory:
```sh
cd Login_Bruteforce
```

### 2. Install Required Libraries

Install the required Python libraries using pip:
```sh
pip install -r requirements.txt
```

### 3. Configure the Script

Open `bruteforce.py` and configure the following variables according to your target:

- `url`: The URL of the login form.
- `username_field` and `password_field`: The names of the form fields for the username and password.
- `wordlist`: The path to your wordlist file.

Example:
```python
url = "http://example.com/login"
username_field = "username"
password_field = "password"
wordlist = "wordlist.txt"
```

### 4. Run the Brute Force Script

Execute the brute force script:
```sh
python bruteforce.py
```

The script will start attempting to log in using the credentials provided in the wordlist. Successful login attempts will be logged.

## Usage

The brute force script is intended to test the security of web applications by identifying weak login credentials. Ensure you have explicit permission to test the target application.

## Repository Structure

- `bruteforce.py`: The Python script for performing brute force attacks on login forms.
- `wordlist.txt`: An example wordlist file containing potential passwords.
- `requirements.txt`: A list of required Python libraries.

## Disclaimer

This project is intended for educational and ethical testing purposes only. Unauthorized use of these scripts is illegal and unethical. Always ensure you have explicit permission before conducting any brute force attack.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

---

**Note**: Always use such tools responsibly and within legal boundaries. This repository is meant to provide educational insights into brute force attack methodologies for security professionals and researchers. Misuse of these scripts can lead to serious legal consequences.
