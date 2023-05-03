# scripts.py
import logging
from farcaster import Warpcast

class FollowScript:
    def __init__(self, criteria, warpcast_client: Warpcast):
        self.criteria = criteria
        self.warpcast_client = warpcast_client

    def copy_following(self, username):
        fid = self.warpcast_client.get_user_by_username(username).fid
        users_to_follow = self.warpcast_client.get_all_following(fid).users
        for user in users_to_follow:
            try:
                self.warpcast_client.follow_user(user.fid)
            except Exception as e:
                logging.info("Failed to follow user: {}".format(user.username))
        logging.info("You've successfully copied the following of user: {}".format(username))

    def follow_new_users(self, count):
        recent_users = self.warpcast_client.get_recent_users(limit=count).users
        for user in recent_users:
            self.warpcast_client.follow_user(user.fid)
        logging.info("You've successfully followed {} new users".format(count))

    def follow_collection_owners(self, collection_id, limit=9999):
        collection_owners = self.warpcast_client.get_collection_owners(collection_id=collection_id, limit=limit).users
        for owner in collection_owners:
            self.warpcast_client.follow_user(owner.fid)
        logging.info("You've successfully followed the owners of collection: {}".format(collection_id))

    def execute(self):
        if self.criteria == '1':
            username = input("Enter the username to copy following from: ")
            self.copy_following(username)
        elif self.criteria == '2':
            count = int(input("Enter the number of new users to follow: "))
            self.follow_new_users(count)
        elif self.criteria == '3':
            collection_id = input("Enter the collection ID: ")
            self.follow_collection_owners(collection_id)

class UnfollowScript:
    def __init__(self, criteria):
        self.criteria = criteria

    def execute(self):
        # Implement unfollow logic here
        pass
