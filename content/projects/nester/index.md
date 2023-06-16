---
title: "Nester"
date: 2023-06-15T22:43:55+02:00
draft: false
---

## Where are we?

[Nester](https://github.com/ByteOtter/nester) is my first serious open source project that is completely accessible to the public for general use.

At the same time it is the first project that I entirely built from scratch and is actively maintained by me.

Basically it is a command-line tool which can create a full project directory tree for a programming project when given a language and a project name.
Now, you may say *"but Chris, my IDE can do that just fine!"* then I will tell you *"but I like to work from the terminal!"*<br>
Let me tell you how we got here ...

## An idea born through pain

When I came up with the idea for Nester I had just rotated into a new team at my company, as all apprentices do every six months, and my task was to create a full Python application from scratch which would interlink with [Cobbler](https://github.com/cobbler/cobbler).<br>
Now so far so good. Problem was that it should follow all standards and regulations Python has and I was confronted with a lot of new concepts which I, who just came from his first team in which he did only concern himself with software QA, have not really had any experience with. Stuff like build systems, creating actual packages and dependency management.<br>
So as I am who I am I got obsessed with creating a perfect [`src`-Layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) for my project, creating all the configuration files and so on and so forth.<br>
I unironically beat myself over my head with the `pyproject.toml` syntax and fumbling that together with the legacy `setup.py` build system by using a `setup.cfg` and setting that up and *literally going back to the internet archive to find old(er) documentation of `setuptools`* (which no, they do not keep any documentation apart from their most recent one, which is fair enough for their workflow I guess...) so I can read how all of this works for Python 3.6 as I had to ensure compatibility because people apparently do not like to update...

It was a journey I tell ya...

However, the longer I screwed around with everything around the project the more I thought to myself *"ugh I wish there was a tool which would do all of that for me!"*.

Now, I know **now** that there are things like [Poetry](https://python-poetry.org/), which I think would not be applicable here for compatibility reasons, and that PyCharm can be configured to create new projects in a `src`-Layout, too; But I did not know that back then.

So, following the *"has not been implemented here"* mantra of FOSS, I thought to myself *"When I do it once, I do it twice and create a program to automate this."*

So, **Nester** was born!

And it was quite convenient, too. As I had to build a CLI application for work I could interchangeably use what I learned on either my project or Nester on the other project. I started researching CLI application frameworks and found the very nice and very intuitive [`Click`](https://click.palletsprojects.com/en/8.1.x/) framework and started building it.

And oh boi, did I run into a wall again trying to set everything up.

But eventually I managed to build the basics of the cli-"frontend", I will just call it that. A bit into implementing Nester's logic I got stuck, however. I simply realized I did not have the experience of what Python can do and how to approach the problem at hand. A skill that, thankfully, I was able to improve significantly over time. So I was able to convince one of my colleagues, another apprentice, to lend me a hand and go over with me on how to approach this and what to do.<br>
This agreement then informally transformed into him setting up the first three functionalities of Nester himself while I took care of the "bells and whistles" that Nester required.

As Nester, by the nature of its idea, is supposed to uphold the standards of various programming languages when it comes to the project's form, I knew I had to make Nester conform to this standards as well. This included the setup of the project structure as well as all linters, tests and properly setting up `setuptools` and documentation.

Now, before you say anything, yes; I know that Nester's size is quite small compared to all the stuff around it. You could argue that, when the first version of Nester released, linters, documentation setup, build configuration, etc. probably included twice or thrice the lines of code than the actual application logic itself. Quite ridiculous isn't it?<br>
I would say no. Yes, it was a pain to set up but the learning experience doing so, as well as the experience of managing and administering a project, meeting up with my colleague going over specific design choices is invaluable. And I would say it was well worth it.

## The way to the first release

### Building the core

Now that we set the scene, let's talk about how we got the first release of Nester out the door.

Nester's core functionality, at first, consisted of three functions:

- `create` - which takes `language` and `projectname` parameters and creates a new project.
- `validate` - which takes `language` and `projectname` parameters and validates the projects file structure against the language's JSON schema.
- `clean` - which (in its first form) deletes the contents of the current directory.

`nester create`, as the name implies, tells Nester to create a new project given the short form of a language (like `py` for Python, `cs` for C#, etc) and a project name. It does so by looking for a JSON schema with the name of the language and creating files and directories according to it.

The way `nester create` works is actually quite cool (props to my colleague for that): JSON data is represented by Dictionaries (A list of `key` and `value` pairs). The `keys`, a String, is seen as the directory- or filename. Then it will be checked if the key is a string. If yes, it is assumed as a file and a `touch` command is executed to create the file and write the content of the string to it if applicable. If it is a dictionary however, it is assumed that the name corresponds to a directory and a mkdir is executed, the directory changed to inside the new directory and the contents of this dictionary are checked.

Cool side notes aside, these three functions were the core of what Nester should be able to do.

### Testing, testing testing

It took a week or two to implement the core of Nester's functionality. On the side I concerned myself with `setuptools`. I wanted to get that up and running so I could publish Nester, ideally automatically.<br>
To be hones, a lot of the time it did not want the way I did. Mostly because I was thinking wrong:<br>
Coming from Uni and programming courses in school I thought *"ah everything needs a `main` function"* and in Python that means the typical `main.py` with that nice `if __name__ == "main"` bit inside. And as I tried to get my build system to work I stumbled over `setuptools entrypoints`. Essentially, you tell setuptools in your `pyproject.toml` where your code starts and it will do the rest for you. In my case it starts in my click frontend. So I pointed it to that module, rebuilt it and .... IT WORKED!

Granted, at this point Nester was still broken... BUT it built!

Now I could go to sleep (it was 4 AM on a workday), and, with an easy mind, build Nester's functionality. So we did.

Until a realization set in: A well written and organized project must have automated unit tests.

Oh boi another journey let me tell you...

I mentioned that in my previous team I was in software QA. And I learned some things about automated testing, testing web frontend stuff, etc, etc...<br>
But I have never touched unit tests that were not frontend tests. Why? Because these fell into a different team.

So I sat there, never touched testing in unit (because why should they teach us useful things lol) nor in my project before (everything just works) and have to grasp new concepts like `mocking` functions.

To sum it up it was quite a ride. But I managed to put out not only unit tests but also integration tests (admittedly by accident). And they worked!

Now just slap in a workflow to automatically run unit tests on PRs and commits and I can release my first project I just ... ooooooh Scheiße...

### Read the f*cking docs!

I mentioned documentation somewhere up there, didn't I?

Yeah. In my bright mind I wanted to do what I would do for my work project too: Use [`sphinx`](https://www.sphinx-doc.org/en/master/) to automatically create and build documentation from my code and publish it to [`Read the Docs`](https://readthedocs.org/).

*Sigh* Here we go again...

So, go over the entire code and add proper docstrings so sphinx can build correct documentation. Configure sphinx and its extensions so they actually run and don't crash for no reason. Steal a documentation publishing workflow from my colleague and see it fail as I did not change it correctly to fit my project. Change the horribly documented sphinx css sheet to at least have a little bit of theming going on. See the ReadtheDocs build fail because yes and then ... all green!

Nester now has documentation! This means I can finally...

### Releasing the first version

I anxiously committed the PyPi publishing workflow and watched that yellow circle to it's thing. Hoping, begging that `v0.1.0` of Nester would see the light of day.

Spoiler: It did not.

Turns out a workflow like this only works on `tags`. So, after a quick introduction into `git tags` by my mentor finally that thing turned green and on this day, the **11th of May 2023** Nester was finally free to spread its wings and help people create new projects with one simple command.

## First issues

After the first release I leaned back in my chair, the PyPi page open looking on what I had achieved with the help of my friends and colleagues.

*"No time to rest!"* I thought. Some more features wanted to be implemented. So I opened the source code and dabbled around with Nester on the side in the terminal until I realized that creating projects with any other language than Python did not work. I checked the JSON files and: turns out, they were all empty. Till today I do not know why.

It was an easy fix though. Add that stuff back in, commit, push, tag, build, release. Two versions at release date. Something only AAA game studios manage to achieve. Yes, I am proud.

## The time since

Ever since Nester released my development speed has slowed slightly with it as it is currently not my top priority anymore as I made progress with my work. However, I did built a new feature into it: Allowing Nester to keep a log of projects it creates and maintain and sanitize that log and keep track so the user does not create duplicate projects etc. Quite proud of that little feature to be honest.

I plan to steadily built on top of Nester and improve it, expand the supported languages, add an interactive mode. And see what ideas I get in the future. A bit more project management utility would be nice, wouldn't it?

All in all Nester, and my project at work, have both taught me a lot about creating projects from scratch as well as how to break up a problem into smaller tasks and tackle them one by one. They also taught me where and how to look for help, how to argue my case (e.g. where and why to use a certain dependency) physically in the office or publicly in a written discussion on GitHub or similar.

And though Nester is mainly a learning project, we are currently in the process on expanding on it and throw it in OBS to maybe one day package it for openSUSE. Who knows what the future holds? I am excited anyways...

## Thanks

Let me use a small part of this blog post to say thank you to my friends and colleagues who have helped me honing my skills and create my own little pet project.

You know who you are.

## You

You, yes you there. Thank you for reading this!

If you would like to check Nester out and maybe contribute I would greatly appreciate it! You can find it on [GitHub](https://github.com/ByteOtter/nester).

Otherwise I'll see you around! :otter:

---

**Fun Fact**: The name "Nester" came from my desire to have a dragon as my icon and what do dragons do? Build nests! And ... you can see your project directory as your nest I guess? Look, I promised you reasons... I never said *good* reasons.