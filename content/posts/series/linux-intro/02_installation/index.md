---
title: "Linux 02 - Installing a Linux Distribution"
date: 2023-10-11T16:00:03+02:00
series: ["Introduction to Linux"]
series_order: 2
heroStyle: "background"
draft: true
---

# Step 1: Creating a bootable device

> Hint: If you plan on installing Tumbleweed in a Virtual Machine, you can safely skip the rest of this step after
> downloading the OS's `.iso` image from [get.opensuse.org](https://get.opensuse.org/tumbleweed/?type=desktop#download).

To install any operating system on a computer you need to create a medium which you can boot from first.
Usually this is done with a regular USB-Stick.

First you will need to download the ISO. As we are using `openSUSE Tumbleweed` in this example, you can download the
operating system here: [get.opensuse.org](https://get.opensuse.org/tumbleweed/?type=desktop#download).<br>
When you follow this link you will be greeted by a large selection of download options. Worry not, as this overview
presents you with all the different computer architectures that Tumbleweed supports. Each with its own image.

If you have a reasonably modern computer that you want to install the OS on you can safely choose the upper left
box where it says `Intel or AMD 64-bit desktops`. This version of the OS is built for 64-bit CPUs. To the right of
this selection are the images for 32-bit PC processors. If you have a very old machine that you wish to revitalize
this will most likely be the option for you.

> Hint: If you are unsure which architecture your system has, stand by as I am working on an excursion on how to find out
> and why this matters. Until then Google is your friend, simply Google the PC or CPU you have and it will tell you.

I will not go over on how to create a bootable USB-Stick in this guide. There are many articles out there which explain
this process step by step with every tool under the sun. I have two good ones right here:

- On Windows the tool I recommend for creating bootable USB devices, or SD cards, is [`Balena Etcher`](https://etcher.balena.io/)
  it's quite literally a 3 click process. Just download the ISO, select the USB-device and off you go.
- In the off-chance you are using Linux, you probably already know how to do it using the `dd` command.
  In case you do not, however, here is an example:
  ```bash
  sudo dd if=openSUSE-Tumbleweed.iso of=/dev/sdb status=progress
  ```
  This can take a while to complete. **Do not forget** to replace `/dev/sdb` with the correct device name. You can check
  this by using `lsblk` followed by `sudo umount <DEVICE>`.
