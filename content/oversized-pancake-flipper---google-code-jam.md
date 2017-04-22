---
title: Oversized Pancake Flipper - Google Code Jam
date: 2017-04-10
description: My solution for the Problem A of the 2017's edition
tags: programming, python, Google Code Jam
---

![Pancakes](https://images.pexels.com/photos/4626/food-plate-morning-breakfast.jpg?w=940&h=650&auto=compress&cs=tinysrgb "Pancakes")

## Google Code Jam

If you're a programmer and you don't know [Google Code Jam](https://code.google.com), you should definitely go and check that. It's basically a coding competition, I like to call it "the programming olympics".

It's about 4 or 5 years I'm participating, I love it because it challenges my coding skills, and I'm not talking about "making a for loop".

This year I want to share my solutions of the problems, let's start with the first and the easiest one.


## The problem

[Here the complete problem text](https://code.google.com/codejam/contest/3264486/dashboard#s=p0).

You have a row of pancakes and a strange flipper, you have to find the right combination to make them show their *happy side*.

At first I thought it could be easy: just flip the *unhappy* pancakes and see what happens.

*"This is a competition, the solution can't be so simple!"* - my inner voice said. So I proceeded to the other problem to see if they were simpler, after those I came back.


## The solution

Facing the problem again, I had no other ideas but the first one. I decided to give it a try.

You can find the code [here](https://gist.github.com/greenkey/1fd7a44c0b110ec9cd6f69b99b000adf), but let me explain some part of it.

To ease the following steps, I get the first part of the input `line.split()[0]` and I convert the pancake row in a list of binary items.

```python
# ...
pancake_row = [p == '+' for p in line.split()[0]]
# ...
```

The list comprehension says something like *"for every character in the string, create an item with `True` value if the character equals `+`, False otherwise"*
List comprehension are very powerful, here is the code without it:

```python
pancake_row = list()
for p in line.split()[0]:
    pancake_row.append(p == '+')
```

Then i go through the list looking for a pancake to flip, now that every item is a boolean, I can check them with a simple `if`:

```python
# ...
pan_size = int(line.split()[1])
# ...
while i < (len(pancake_row) - pan_size + 1):
    if not pancake_row[i]:
# ...
```

Now I put the flipper starting from the first *unhappy pancake* and then flip.

```
pancakes: ---+-++-
flipper:  ***
flipped:  ++++-++-
```

To make it in the code, I just have to `not` the items: `not False == True`:

```python
# ...
while i < (len(pancake_row) - pan_size + 1):
    if not pancake_row[i]:
        for j in range(i, i + pan_size):
            pancake_row[j] = not pancake_row[j]
# ...
```

I think I could have done it using *slicing*:

```python
# ...
while i < (len(pancake_row) - pan_size + 1):
    if not pancake_row[i]:
        j = i + pan_size
        pancake_row[i:j] = [not p for p in pancake_row[i:j]]
# ...
```

Going on with the example, the pancake row evolution should be the following:

```
---+-++-
***
++++-++-
    ***
+++++---
     ***
++++++++
```

With this example we're lucky, because at the end all the pancakes are *happy*. We can check it using a special Python function (you don't have to reinvent the wheel):

```python
# ...
all(pancake_row)
# ...
```

[`all()`](https://docs.python.org/2/library/functions.html#all)
> Return `True` if all elements of the iterable are true

If the pancakes are not all on the happy side, we can argue that it's impossible: the *unhappy* pancake should be at the end of the row, there's no way flip them without flipping the previous pancakes.


## What I learnt

My intuition was right... *I* was right! (not my inner voice).

So next time I could give it a try sooner.