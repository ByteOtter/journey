---
title: "Linux 02 - Installing a Linux Distribution"
date: 2023-10-11T16:00:03+02:00
series: ["Introduction to Linux"]
series_order: 2
heroStyle: "background"
draft: true
---

# Creating a bootable device

To install any operating system on a computer you need to create a medium which you can boot from first.
Usually this is done with a regular USB-Stick.

## On Windows

When you have a Windows computer you can create a bootable USB stick using a tool like
[Balena Etcher](https://etcher.balena.io/url). Let's go over the process step by step. We are using the distribution
`openSUSE Tumbleweed`.

1. **Download the ISO-File**. To download the distribution's image visit [https://get.opensuse.org/](https://get.opensuse.org/tumbleweed/?type=desktop#download)<br>
   When you click the link you will be greeted by a selection of different images. Choose the one which fits your computer.<br>
   If you have a reasonably modern computer, you will most likely need the `Intel or AMD 64-bit desktops, laptops, and servers (x86_64)` image.<br>
   In this section you have the choice to either download the offline- or network-image. The first comes with all
   necessary software packages while the other, smaller, one will download what it needs from the internet during installation.<br>
   I personally recommend using the larger offline image though. Especially if you are installing in a Virtual Machine.
2. **Flash your USB-Stick**. (You can skip this step if you use a VM)