---
title: "Linux 01 - A Overview"
date: 2023-10-01T18:00:03+02:00
series: ["Introduction to Linux"]
series_order: 1
tags: ['Linux', 'Tutorials & Guides', 'Series']
heroStyle: "background"
draft: false
---

Welcome to my series *"Introduction to Linux"* in which we will explore the world and possibilities of the Linux sphere.

I hope you enjoy this little trip whether you already have some experience with Linux or not.

## What is Linux?

Firstly, we should agree on a definition on what Linux is or rather, what we refer to when talking about `Linux`.

> `Linux` is an open-source operating system (OS). The duty of an operating system is to sit between a computer's hard-
> and software and manage the system's resources, like CPU, memory and storage.

This is probably one of the most common and controversial definitions of the term `Linux`. And I am not really fully
happy with it myself but for other reasons than the more experienced of you might suspect.

This is because the term `Linux` technically only refers to the operating system's `kernel`. A `kernel` is the heart, or
core, of an operating system. It manages all of the computer's resources and acts as a bridge between the hardware and
software, translating requests from software to CPU instructions for example.

However, a complete operating system is more than just its kernel. It typically includes a graphical interface, applications,
services and libraries that can be shared between software you install so it can function.

So what we think of when we hear the term `Linux` is called `GNU/Linux` by some people, as it includes the `GNU` operating system,
initiated by Richard Stallmann in 1983, aside from the `Linux kernel`, developed by Linus Torvalds in 1991. But when
we go down that rabit hole we have to call it `GNU/Linux/Wayland/Systemd/Plasma/WhatEver` as we would have to list
all the different components of a Linux operating system. So let's not do that.

In this guide though I will use the term `Linux` to refer to the **family of operating systems which use the linux kernel.**<br>
*Family* because there are many different flavours of Linux out there, called distributions, each with their own way
of doing things, their own graphical user interfaces, ways of storing files, etc.

So, summed up in the context of this guide:

- `Linux` means the **family of operating systems using some kind of Linux kernel**
- `Distribution` refers to a specific kind of a Linux OS (like Ubuntu, openSUSE, Debian, etc.)

## Why choose Linux?

The reasons why people decide to use a Linux system, or switch to it entirely, can be about as varied as the distributions
themselves.

Some prefer the control and privacy most Linux distributions offer, some want to breathe new life into an old machine
which has long since been left behind by hardware compatibility with Windows (tm) and others like to perfectly
tweak their setup fit their working environment to their needs.

There are many more reasons to list, like the superior reliability in the enterprise business but this list
would be getting out of hand and may be fit for a more in-depth look in the future.

In contrast there is not really a reason why you should not try Linux. Most distributions are free, small and can easily
be run in a Virtual Machine. So there is really no barrier to entry here.

## Choosing the right flavour

Before we begin we should try to get an overview on what kinds of distributions exist, what they are used for and
what you should choose depending on your use-case.

Let's start with general purpose distributions. For day-to-day operation on your private machine you will usually need:
A graphical user interface, some sort of office suite (or at least a text editor), a browser, an e-mail client, etc.<br>
So a full-fledged operating system, as you may be familiar with from the world of Windows (tm), would be preferred.

For this distributions like [`Ubuntu` by Canonical](https://ubuntu.com/download/desktop), [`Leap/Tumbleweed by openSUSE`](https://get.opensuse.org/desktop/),
or [`Fedora` by RedHat](https://fedoraproject.org/), and others, are excellent choices. All of these have significant
communities around them, come with graphical installers and offer documentation to help you navigate around. And if you
are afraid of the Terminal, worry not, as all of these come with `Desktop Environments` that have all necessary tools
included to avoid using the Terminal as much as possible. From settings menus to software "stores", from which you can
select the software you want to install via a graphical interface without the need to touch the terminal.

On the other hand if you are looking for something smaller, are not afraid of the Terminal or need to run a server with
it, you may want to leave the Desktop Environment behind and install one of the distributions mentioned above without
a graphical interface, or use a dedicated "server" distribution. Check out the distribution's website for more
information about that.

For home and personal use, the choice of which distribution you use is arguably less important nowadays than what
desktop environment you use.

The Desktop Environment (DE) as the name implies is the part of your distribution that handles everything desktop related.
It is the graphical user interface (GUI) similar to what you might have interacted with in the past using Windows.
Everything you see and interact with, your file explorer, settings application, browser, etc. all of this is handled
by your desktop environment.

There are several popular options to choose from with different pros and contras which I will not go into detail here.

All you need to know is that for this little series we are going to use the distribution `openSUSE Tumbleweed` with the
`KDE Plasma` desktop.

Thank you for reading this little overview. I hope you learned something. Join me next time when we finally start
installing your new system. See you next time.

---

## Glossary

This was a lot of information thrown at you all at once I know.

Here a quick overview of words used so far.

|Phrase|Description|
|-|-|
|`Linux`|Refers to the **family of operating systems using some form of the Linux kernel**.|
|`Distribution`|Refers to a specific kind of Linux OS (like Ubuntu, openSUSE, Debian, etc.).|
|`Graphical User Interface / GUI`|All visual elements you can interact with or that represent data.|
|`Desktop Environment (DE)`|The component of a Linux OS that handles the visual interpretation and representation of data and applications and allows for interaction using a GUI.|
