Title: eddie, build a bot in seconds!
Date: 2017-04-22
Tags: python, eddie, chatbot

I'm really into chatbots lately.

I was tired of creating the same chatbot on different platforms, so I created
**eddie**, a Python library that basically lets you doing the following:

* define your bot, using a set of simplified API
* define the endpoints (services to which you activate your bot)
* run the bot

Here an example

```python
>>> import eddie
>>> class MyGreatBot(eddie.bot.Bot):
...     def default_response(self, in_message):
...         return "You said: " + in_message
... 
>>> bot = MyGreatBot()
>>> bot.process("Hello!")
'You said: Hello!'
```

Let's say you want to deploy the bot on Telegram and Twitter (the only two
platforms supported now).

Get your tokens using the services' guides, and then use them to connect the
eddie's endpoints:

```python
>>> bot.add_endpoint(eddie.endpoints.TwitterEndpoint(
...     consumer_key='your consumer_key',
...     consumer_secret='your consumer_secret',
...     access_token='your access_token',
...     access_token_secret='your access_token_secret'
... ))
>>> bot.add_endpoint(TelegramEndpoint(
...     token='123:ABC'
... ))
>>> bot.run()
```

## Current status

Currently it is a very young library, it has just the following features:

* connect to Telegram, Twitter and HTTP (rest)
* define a default response
* define commands (i.e. `/start`, `/help`)

I don't have a roadmap yet, but surely I'm going to support:

* other endpoints like Facebook, Skype...
* specific NLP services like [api.ai](http://api.ai), [wit.ai](http://wit.ai),
  [conversate.eu](http://conversate.eu) ...
* context handling, user's details, conversation context...

There's a lot of work to do and I'm open to any collaboration. Eddie is
OpenSource!

## Why "eddie"

At first I staretd using `pychatbot` as the name of the library.

It was easy... too easy, indeed: when I decided to release the package on PyPI I found
that the name was already taken!

Then I llok for another name and I found a minor character of 
[The Hitchhiker's Guide to the Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy).

> [Eddie](https://en.wikipedia.org/wiki/List_of_minor_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Eddie)
> is the name of the shipboard computer on the starship Heart of Gold. [...]
> Eddie is over-excitable, quite talkative, [...] Shipboard networking
> interconnects Eddie with everything on the Heart of Gold [...]