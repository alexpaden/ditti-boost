# menu.py
def display_menu():
    print("1. Follow")
    print("2. Unfollow")
    choice = input("Enter your choice: ")
    return choice

def display_follow_scripts():
    print("1. Copy a user's following")
    print("2. Follow (x) new users")
    print("3. Follow collection owners")
    choice = input("Enter your choice: ")
    return choice

def display_unfollow_scripts():
    print("1. Unfollow all users")
    print("2. Unfollow non-follow back users")
    print("3. Unfollow collection owners")
    choice = input("Enter your choice: ")
    return choice
