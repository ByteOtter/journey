---
title: "Crumb: (Un-)interesting Git - Changing the Author of a Git Commit"
date: 2025-03-03T17:00:03+02:00
draft: false
heroStyle: background
tags: ['Programming', 'Crumbs']
---

When setting up my new laptop for work I copied over my git config from my private machine, and while I changed 
my email to my work email I forgot to change my username.

Now for public upstream commits this is fine, but for internal ones ... People would look at me weird I am sure.

Now, for changing that, you basically have two options.

## Change Username of the last commit

Changing the username of the last commit is quite straight forward (but I still had to look it up).

```bash
git commit --amend --author="Your Name <your.email@example.com>"
```

## Change Username of a specific commit

Now changing the author of a historic commit is a bit more of a pain.

Supposedly it should work by looking up the commit ID by taking it from `git log` like this:

```bash
git rebase -i <commit-id>
# Change 'pick' to 'edit'
git commit --amend --author="Your Name <your.email@example.com>" --no-edit
git rebase --continue
```

For some reason though, this didn't work for me. It always picked the wrong commit.
Luckily, you can always count back from `HEAD` too:

```bash
git rebase -i HEAD~<Number of commits from head>
# Change 'pick' to 'edit'
git commit --amend --author="Your Name <your.email@example.com>" --no-edit
git rebase --continue
```

So yeah, that's how that works. Of course, you can also change your email address this way, though I guess when you
have commit signing set up it will most likely break, but I didn't try that.
