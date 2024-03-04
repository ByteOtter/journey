---
title: "So, I did a thing..."
date: 2024-03-04T20:00:03+02:00
draft: true
---

You may be wondering where I have been in the past 2 months ... or maybe not I have no idea if someone is even reading this.

Anyway, in the off-chance that you were and have been wondering where I went, I have been busy building a little something.

Let me tell you a little something about:

## [Nazara](https://github.com/The-Nazara-Project/)

### What?

Nazara is going to be a CLI application that will allow developers and system administrators to create or update
machines in [NetBox](https://netbox.dev) more efficiently.

Starting out as a Rust learning project in my spare time,
I am now at a point where I feel comfortable about talking about it openly.

In my last team at SUSE, I helped not only by writing software, but also had a hand in dealing with new machines sent to
us by our hardware partners.
Setting them up, putting them into a rack in our server room and configuring them, stuff like that.
I also got insight in how we keep track and manage these machines.

One of the tools we used was NetBox. A inventory and IPAM (IP address managemnet) tool, where we entered the machines IP addresses,
name, hardware components, etc largely manually.

That's where my teamlead and I came to an idea. I wanted to learn Rust and I am also a fan of automation.
So I started work on a CLI tool to automatically collect information about a machine and
throw it into a given NetBox instance. The name of the project then: `NetBox-Sync`.

Well, it was by far not as easy as I thought at first.

Turns out, learning a completely new and complex language like Rust as well as dealing with some new concepts
(in terms of applying them into software) such as Networking, Swagger and APIs,
all at once is kind of tough when doing so in one's spare time. (And yes. I did all this aside from work in my own time.)

But, I think I pushed through quite okay.

## What Nazara does.

Quite some time has passed since Nazara's, then NetBox-Sync's, design assumed that it would only require one or two API
endpoints and simply pass information to NetBox.

This was a mistake on my part. Turns out the issue is a little more complex. About 40,000 lines of code more complex.

But let's not get ahead of ourselves.

In short, Nazara is supposed to collect information about the machine its running on. Things like
the model of CPU, number of cores, amount of memory, its network interfaces, IP adresses, etc.

Then it should get either a list of devices or virtual machines from NetBox, look whether it is already registered, and
then either update or create a new machine or VM.

Collection is done by using `dmidecode`, a command to query a wide variety of system parameters built-in to a lot of
Linux distributions, and the `NetworkInterface`  crate.
A rust crate designed to collect all available network interfaces of a machine.

This data would then need to be translated into the format required by NetBox's API and sent.

Easy, right?

## NetBox doing NetBox things ...

While the process sounds easy there are some challenges regarding NetBox's API. Firstly, its [vastness](https://www.youtube.com/watch?v=arnWU1sWqKw&pp=ygURZGFtbiBib3kgaGUgdGhpY2M%3D).
When we take a look at the [swagger](https://demo.netbox.dev/api/schema/swagger-ui/) of the public NetBox test instance
(something that I am very very glad exists btw.), we can see that the number of possible endpoints is absolutely massive.

Scratch the idea of writing a small API client by hand.

Thankfully though, NetBox uses `openAPI` to specify create its API.
And they provide a generator for client code in a variety of languages given the API specification yaml. Hooray!

Problem, the generator for Rust creates a 120,000 lines of code blob of broken Rust code which not only brings VSCode
to its knees, but is also unmaintainable. Not that you **want** to maintain auto-generated code in the first place.

And that is besides the problem of the artificially implemented token limit for the free version of the generator,
which would regularly crash if the newest API schema version was passed to it.

Another problem: NetBox and its API are highly customizable. So the API spec for the public instance of NetBox can
deviate from the user's spec quite significantly.
Though we can ignore most of it, as long as the machine and VM endpoints stay the same, it is still something we need
to keep in mind.

## Creating Thanix

To circumvent the issues found with openAPI's generator, we (a colleague had joined me in the meantime) decided that we
needed our own client generator. One that actually works.

So my colleague got to work. In two days the first iteration of [`Thanix`](https://github.com/The-Nazara-Project/Thanix)
was ready. A true madlad this one.

And what can I tell you? Todd Howard said it best when he said:

> *"It just works." - Todd Howard*

And just like Fallout76, Thanix was a great piece of software without any bugs or exploits.

No, it didn't have a huge problem where the path functions would not be able to send data because they did not receive
a data struct argument, which was empty. Why you asking?

In all seriousness though, huge shout-out to my colleague whose help made all of this work.

So now here it is: Thanix.
A yaml-to-rust code generator which would take the API spec yaml and output an API client in a crate format.

While we were still ironing out some of the previously mentioned kinks with it, the plan was now as follows:

1. Use the publicly available API schema from NetBox's demo instance as a reference client and require it as a
   dependency for Nazara. (This would allow for a general implementation and easy testing).
2. Document on how to integrate a user's custom API client with a locally built crate.
   (This is the tricky part. We currently assume that the user's custom API at least resembles the one used by the demo
   instance. Custom API endpoints cannot be accounted for right now. Also the information we collect may deviate from
   the user's needs. But hey, it's open source. Help yourself.)

It has been a couple weeks since Thanix's first version and now we can finally say that it works to its fullest extend.

So I felt comfortable to release it into its first beta version. If you want to try it, you can find it
[in the repo](https://github.com/The-Nazara-Project/Thanix), on [crates.io](https://crates.io/crates/thanix) and as an
`.rpm` package for openSUSE Tumbleweed and Leap 15.6 on
[OBS](https://build.opensuse.org/package/show/home:ByteOtter:nazara-project/thanix).

It's still a good bit of work ahead of me, but the thing that's creating the most headaches for me is taken care of now.

To accommodate the new projects surrounding Nazara now, I decided to move everything into an organization, create a
temporary logo and am currently in the middle of creating a very basic website for it. All still in the works and very
much subject to change but I am very excited about all the positive feedback I got already.

I am fully committed to this project by now and already have some plans for Nazara which will extend its functionality
in the future.

I also have some other ideas for support projects already, that would make Nazara more useful.

Let's see how far we'll get.

## Closing

That's it. That's what I have been doing for the past couple of months.

If you feel like it, check out my projects and stay tuned for further updates.

Until then, have a great time!

- Chris
