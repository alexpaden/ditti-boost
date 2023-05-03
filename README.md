# Ditti Boost

Ditti Boost is a command-line tool that automates following and unfollowing users on Farcaster. It provides a simple way to grow your network, find new users, and manage your connections on the platform.

## Features

- Follow users based on different criteria:
  - Copy a user's following
  - Follow new users
  - Follow collection owners
- Unfollow users based on different criteria:
  - Unfollow all users
  - Unfollow non-follow back users
  - Unfollow collection owners

## Installation

_This project requires python3.10_

To install Ditti Boost, run the following command:

```
pip install ditti-boost

ditti-boost
```

## Usage

To use Ditti Boost, first navigate to the project directory and run the following command:

```
poetry env use 3.10
poetry install
poetry run python ditti_boost/cli.py
```

You will be prompted to enter either an access token or a mnemonic phrase. Then, you can choose from various follow and unfollow options.

## Contributing

Contributions are welcome! If you'd like to help improve Ditti Boost, please feel free to open an issue, submit a pull request, or suggest new features.

## License

Ditti Boost is licensed under the MIT License.
