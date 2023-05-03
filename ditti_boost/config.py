# config.py
import os
from dotenv import load_dotenv

env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
MNEMONIC_PHRASE = os.getenv('MNEMONIC_PHRASE')

def save_credentials_to_env(access_token, mnemonic_phrase):
    with open(env_path, 'a') as env_file:
        if access_token:
            env_file.write(f"ACCESS_TOKEN={access_token}\n")
        if mnemonic_phrase:
            env_file.write(f"MNEMONIC_PHRASE={mnemonic_phrase}\n")

def prompt_for_credentials():
    if ACCESS_TOKEN is None and MNEMONIC_PHRASE is None:
        print("Please enter either an access token or a mnemonic phrase.")
        access_token_input = input("Access token: ")
        mnemonic_phrase_input = input("Mnemonic phrase: ")

        if not access_token_input.strip() and not mnemonic_phrase_input.strip():
            print("Error: Both access token and mnemonic phrase are empty.")
            exit(1)

        access_token = access_token_input.strip() or None
        mnemonic_phrase = mnemonic_phrase_input.strip() or None
        save_credentials_to_env(access_token, mnemonic_phrase)

        return access_token, mnemonic_phrase
    else:
        return ACCESS_TOKEN, MNEMONIC_PHRASE
