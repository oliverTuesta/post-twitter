# post-twitter

## Table of contents

-   [General info](#general-info)
-   [Technologies](#technologies)
-   [Setup](#setup)

## General info

This a simple program made with python to post in Twitter using the Twitter API

## Technologies

Project is created with:

-   Python 3

## Setup

<ol>
    <li><p>Get acces to the <a href="https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api">Twitter API</a></p></li>
    <li><p>Apply for <a href="https://developer.twitter.com/en/portal/products/elevated">elevated acces </a></p></li>
    <li><p>Clone this repository</p></li>
    
```
$ git clone https://github.com/oliverTuesta/post-twitter.git
$ cd post-twitter
```
<li><p>Install dependencies using <a href="https://pypi.org/project/pip/">pip</a></p></li>

```
$ pip install tweepy
$ pip install pandas
```

<li><p>Create the file <b>config.ini</b> with your API credentials</p></li>

```
[twitter]
api_key = <your API key>
api_secret = <your API key secrete>

access_token = <your access token>
access_token_secret =  <your access token secret>
```

<blockquote>
    <p>Make sure to keep secret all your credentials</p>
</blockquote>
</ol>
