---
title: "The Nazara Project"
description: "The Nazara Project"
date: 2024-07-15T17:36:49+02:00
draft: false 
---

so, here it is. Long awaited, finally here, a proper explanation of what I have been doing off
work in the last year or so.

I have been busy building an open source project called *"[The Nazara Project](https://codeberg.org/nazara-project)"*.

The Nazara Project is a cluster of open source software projects which focus around an application called 
*"[Nazara](https://codeber.gorg/nazara-project/Nazara)"*.
Nazara is a CLI application through which users can register and update their machines in the inventory 
and IPAM tool *[NetBox](https://netbox.dev/)*.

But let's start at the beginning.

## How did we get here?

So it all started in when I transferred into my second team at the company I work for: Kernel Storage & Networking.

The focus of this team is maintaining the network and storage stack of the Linux kernel and enabling it on new 
hardware.
To do so, hardware manufacturers would send us machines with alpha hardware and we would test our distribution on it, 
see if it works and if not, implement support for this hardware.

This - understandably - leads to a high turnover of machines and their components relatively quickly. And keeping track
of it all manually became quite a hassle. Not to worry, as we are all software engineers so there were workarounds and 
scripts used to automate certain things around machine registration, update and deletion in NetBox.

However, none of these was a one-size-fits-all solution. A single thing to run and do it all.

So I, as the apprentice, asked myself if I could work on something like this and - with the blessing and support of 
my teamlead - started work on what was then called `Netbox-Sync`. And of course, I did it in Rust. Rust is cool after all 
and I did a bunch of Python before, so ... yeah, why not.

I quickly found out that learning Rust while working on a relatively complex project all by yourself is not the best idea, 
but this may be a topic for the future.

