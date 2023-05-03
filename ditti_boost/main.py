# main.py
from authentication import Authenticator
from ditti_boost.reporting import configure_logging
from menu import display_menu, display_follow_scripts, display_unfollow_scripts
from scripts import FollowScript, UnfollowScript
from config import prompt_for_credentials

if __name__ == '__main__':
    configure_logging()
    access_token, mnemonic_phrase = prompt_for_credentials()
    authenticator = Authenticator(access_token, mnemonic_phrase)
    warpcast_client = authenticator.authenticate()

    choice = display_menu()

    if choice == '1':
        follow_criteria = display_follow_scripts()
        follow_script = FollowScript(follow_criteria, warpcast_client)
        result = follow_script.execute()
    elif choice == '2':
        unfollow_criteria = display_unfollow_scripts()
        unfollow_script = UnfollowScript(unfollow_criteria, warpcast_client)
        result = unfollow_script.execute()
