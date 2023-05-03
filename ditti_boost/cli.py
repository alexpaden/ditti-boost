# cli.py
from ditti_boost.authentication import Authenticator
from ditti_boost.reporting import configure_logging
from ditti_boost.menu import display_menu, display_follow_scripts, display_unfollow_scripts
from ditti_boost.scripts import FollowScript, UnfollowScript
from ditti_boost.config import prompt_for_credentials

def main():
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

if __name__ == '__main__':
    main()
