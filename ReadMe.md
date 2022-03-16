# Selenium-twitter-automation

This is a [Selenium](https://github.com/SeleniumHQ/selenium) based python project that automates liking tweets via [Chrome Driver](https://chromedriver.chromium.org/downloads)

## Functions || What it does:

- `login()` : Log in into your account
- `like_homepage()` : Like tweets in hompage
- `like_by_hastag()` : Like tweets in hashtag
- `like_user_posts()` : Like tweets of a user
- `like_a_list()` : Like tweets from a twitter list
- `logout()` : Log out of your account

## Variables:

- `post_to_like` = no of posts to like in each iteration
- `wait_like` = seconds to wait before liking next post
- `user` = username of the twitter profile to like the posts of
- `wait_pageload` = seconds to wait for page to load
- `list_link` = link to any twitter list
- `chromedriver` = path to the chromedriver
- `hastag`='hastag to search for

## To Run project :

- Have `python` environment setup
- Clone the repo and go to the cloned directory
- Run `pip install selenium`
- Have chrome Driver installed [Link](https://chromedriver.chromium.org/downloads)
- Check the Variables, change values as required

## Log in Credentials:

- There are two ways to get the credentials via `Environment Variables` or `Hardcode` in [credentials](./credentials.py)
- For better security use Environment variables.
- For windows
  - Start>system>Advanced System Settings>Environment Variables>New
- For [Mac](https://phoenixnap.com/kb/set-environment-variable-mac) and [linux](https://www.geeksforgeeks.org/environment-variables-in-linux-unix/)
- And if you like living on the edge just paste your id and password in [credentials file](./credentials.py)

