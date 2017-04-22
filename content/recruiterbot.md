---
title: RecruiterBot - a collaborative presentation
date: 2017-04-17
description: I presented the idea to an audience
tags: chatbot
---

![Milano Chatbot](https://thepracticaldev.s3.amazonaws.com/i/khrpirmsy5otcmnaztqy.jpg "Milano Chatbot")

It's been a while I'm attending a meetup in Milan about chatbots.

The topic is very interesting and fast growing, furthermore, the meetup is always full of interesting people with very different skills.

For the April date, Paolo Montrasio (the meetup organiser) asked if someone had an idea to talk about.
I proposed to talk about a RecruiterBot and this post is the report of my presentation/brainstorm - if you understand Italian, you can see [the video of it](https://youtu.be/OqkqPmpyyBE).


## PersonalBot, CompanyBot, AgentBot?

The first idea came in my mind after the Nth head-hunter asking me the same questions: do you have experience in X? Do you prefer big or small companies? What is your salary expectation? Etc.

![Automate all the things](https://thepracticaldev.s3.amazonaws.com/i/cwco9itwgcud4tqnrh5l.jpg "Automate all the things")

I'm one of those freaks who wants to automate everything, so I thought that a bot answering the usual questions would be a fair time saver.

My first idea was a bot programmed by a person seeking for a job, used by companies and recruiters looking for a candidate. Let's call it a **Personal Bot**.

When I first talked other people about the idea, it was clear to me that it wasn't enough.
To someone, it would be even better to reverse the game: a bot programmed by someone offering a job, used by the people trying to apply for it. A **Company Bot**.
This is possibly a more interesting bot because companies are more likely to pay that a person.

Someone suggested me also a third type of bot, something that could stay in the middle, chatting both with seekers and offerers, an **Agent Bot**.



## The Presentation

<iframe src="//slides.com/greenkey_loman/recruiterbot/embed" width="576" height="420" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

My presentation to the audience was very short, it was just a presentation of myself (always put a *Who Am I* slide in your presentations!) and a brief introduction. The goal was to let the audience talk after all.

Right after the presentation I opened a [Trello board](https://trello.com/b/4xHTPOGv/chatbot-per-recruitment) set for the occasion, with the following columns:

* Out of scope - Ideas that are not interesting at the moment
* Strenghts - What differentiate this Bot from other solutions?
* For Companies - Ideas for the CompanyBot
* For Candidates - Ideas for the PersonalBot
* For Recruiter - Ideas for the AgentBot

Then I let the audience talk.



## Some general considerations

Before going in depth of each bot's ideas, I find something interesting during the brainstorming.

**A Bot should immediately state its nature.**
It's like the message on the voicemail, the first thing you always hear is "*Hi, we're not at home right now...*".
Once, I set this message on my answering machine: "*Hello? -pause- Oh, sorry, I'm not at home now, please leave a message.*"
It was fun until they started insulting me.

## Out Of Scope

#### It's not a crawler

[Someone already tried](https://www.fastcompany.com/3069166/i-built-a-bot-to-apply-to-thousands-of-jobs-at-once-heres-what-i-learned) to use a bot to automatically reply to job offers. That guy learnt a lot about recruiting but the bot didn't help him finding a job. 

## Strength

#### Straight to the point

We're tired to read tons of content to find the one that interests us (down with websites and CV).
With a bot in front of you you could ask questions in random order, without roundabout expressions, you can even be harsh (but not too much, someone could read the logs!).

#### Time saving

Imagine to make a 20 minutes call in which we talk about our experience, our skills, the team's activity, the role needed and then the question: "*Are you willing to relocate in Iceland?*".

## Ideas for Companies - CompanyBot

#### Skim

One of the greatest need for a company is to make a shortlist of all the candidates.
A bot could be programmed to ask some question in order to understand if the candidate has all the requirements.

#### Clustering

If the bot's decision tree is well made, the candidates can be grouped into clusters or categories, so that the company will be able to identify the right person, maybe for other positions.

#### Pre-evaluate

You can set the bot to make technical questions about the position.
You can exchange files too! So why not using it to ask examples of the candidate's works? 
For a programmer could be possible to propose a problem and then ask for the output file (I'm thinking about problems like the ones in [Google Code Jam](https://code.google.com/)).

#### A job post is too short

A job post cannot be too long and cannot contain all the of information.
A candidate could ask a bot all the data not present in the job post: "*You wrote Java but are you using some specific framework?*", "*What type of insurance is included in tha package?*"


## Ideas for Candidates - PersonalBot

#### A CV is too short

A Resumé cannot be too long and cannot contain all the information.
A company could ask a bot all the data not present in the resumé: "*You wrote Java but are you using some specific framework?*", "*Can you show me an example of your works?*"

#### Time matters

Sometimes you find the perfect CV for a position, but it's 2 years old. You could ask the bot information like the availability (maybe they're not interested in a new position now) or the latest version of the CV.


## Ideas for Recruiters - AgentBot

#### Interview simulator

This could be a service for a not-experienced candidate who wants to understand what type of question will face.
Also, the bot could record the answers and identify some interesting profiles.

#### Agent

This is a very broad concept, the idea is to have a personal assistant, always updated to the latest experience and always in contact with companies looking for candidates.
The agent could notify the person about a new job offer, but it could also notify the company about a new skill of a candidate.


## Conclusions

I'm letting all these information to the whole world, I'm not sure is the right thing to do, I don't know if I'm going to develop it.
Maybe these ideas will be massively used by more and more people, turning a purely human process in a completely automated one, making artificial intelligences drive our career and our life choiches, ending in a world in which we humans have nothing to do but follow what *they* say...

So now I can either write that bot or write a sci-fi novel.
