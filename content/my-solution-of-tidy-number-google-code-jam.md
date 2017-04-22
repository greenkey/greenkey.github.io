---
title: my solution of Tidy Number (Google Code Jam)
published: true
date: 2017-04-11
description: My solution for the second problem
tags: programming, python, Google Code Jam
---

![Numbers](https://static.pexels.com/photos/278958/pexels-photo-278958.jpeg "Numbers")

## Google Code Jam

This year I'm sharing my solutions of the Google Code Jam, this is the second post, here are the previous:

* [Oversized Pancake Flipper](https://dev.to/greenkey/oversized-pancake-flipper---google-code-jam)


## The problem

[Here the complete problem text](https://code.google.com/codejam/contest/3264486/dashboard#s=p1).

Tatiana is a nice girl with a bit of [OCD](https://en.wikipedia.org/wiki/Obsessive%E2%80%93compulsive_disorder), she likes to find numbers with the digits in non-decreasing order, the so-called "*tidy numbers*".

Given a number, we have to find the biggest *tidy number* below it.


## The solution

[Here](https://gist.github.com/greenkey/9a81413351ee224a57434ab9a96723df) my complete code.

The first thing to do is to understand what a *tidy number* is: a number with non-decreasing digits.
In other words: each digit should be equal or greater than the preceding.

```python
>>> n = 1234
>>> def is_tidy(number):
...     prev = "0"
...     for digit in str(number):
...         if digit < prev:
...             return False
...         prev = digit
...     return True
...
>>> is_tidy(12345)
True
>>> is_tidy(4444)
True
>>> is_tidy(42)
False
>>> is_tidy(10)
False
```

Pretty straight forward, right?

But we're just at the beginning of our alorithm: how can we find the previous *tidy number*?

It seems simple, right? Just try all the preceding numbers until you find a *tidy* one:

```python
>>> def find_preceding_tidy(number):
...     while not is_tidy(number):
...         number -= 1
...     return number
...
>>> find_preceding_tidy(10)
9
>>> find_preceding_tidy(12345)
12345
>>> find_preceding_tidy(12350)
12349
>>> find_preceding_tidy(12000)
11999
```

It works!

But... what if the numbers are really big and strange?

```python
>>> find_preceding_tidy(3914589564)
3899999999
```

On my machine it takes about 12 seconds to find the number.
This is too much time for the large dataset, where we can have numbers with 18 digits.

It's time to take pencil and paper.

```
3914589564
3899999999

345918
345899

123000
122999

123200
122999
```

So the logic seems to be: when you find the decreasing digit, that's the point you have to decrease the left part and then put 9s for the right part:

```
39 14589564
38 99999999

3459 18
3458 99

123 000
122 999

123 200
122 999
```

And so this is what I do:
* `enumerate` the digits so I can see them one by one **and** have also the index
* when I find the decreasing digit, I use *slicing* to separate the two parts
* I convert the left part to integer and decrease by 1
* create the new right part, repeating 9 for the number of characters

```python
def find_preceding_tidy(number):
    line = str(number)
    prev = "0"
    for i, digit in enumerate(line):
        if digit < prev:
            left_part = str(int(line[:i])-1)
            right_part = "9" * (len(line) - i)
            return left_part + right_part
        prev = digit
```


## What I learnt

It's ok to make a *brute force* algorithm, but you know it will be just for the small data set.

The first solution, however, can be used as a "unit test" when you'll write the second, possibly more complex, algorithm.