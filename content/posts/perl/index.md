---
title: "A word about Perl..."
date: 2024-05-16T20:00:03+02:00
draft: false
---

So, Perl ... Perl, Perl, Perl.

Perl is weird, you know that? It is a very old language that seems
to be universally hated by those who use it, but - somehow - still found
a way to stick around long enough to be used in some major pieces of modern
software.

Which brings me to the fact that I now have to get somewhat familiar with it.

Why?

Well because [openQA](https://openqa.opensuse.org) is a thing and Perl scripts
are a core component of that.

## A peculiar error

All of the above brings us to a problem I noticed while developing new tests for both
the `rustup` and `cargo` packages for openSUSE.

While writing these tests, I took strong influence from existing testfiles, such as
the ones for the `python3` package. So far so well, my logic was sound:

1. Test if the packages can be installed
2. Check if they can do their main functionality (e.g `rustup` being able to install and switch toolchains)
3. Clean test environment
4. ...
5. Profit

However, I ran into a problem. A very peculiar one as well.
Part of submissions for the `os-autoinst-distri-opensuse` repo, where the test files for openSUSE are located,
is providing a verification run on that PRs code to show to maintainers that it works and does what it is intended to do.

When I triggered my verification run, however, it failed almost immediately with a compile error.

```
TODO: Compile error message here.
```

At first I thought - naive that I am - that it was about some naming convention. Changed that, tried again and it still failed.

By this time, my Mentor and I had been looking over my code for a while, but apart from some minor things we need to watch out for later,
it should at least compile.

The internet in the meantime has also been less than helpful - as it tends to be these days - so we were not really finding stuff out with that.

We read that darn error message so many times both in `openQA` but also when trying to compile the file manually when it dawned on us:

It sounds like it cannot find thi `subroutines`!

## F u Perl

At first I thought I was just too stupid to understand that Perl is forward declared. Meaning that you need to declare a function - 
or as it is called in Perl: `subroutine` - before you can use it.

Well, turns out, this is only sort of the case.

See, Perl allows you two main ways of calling a subroutine. One by calling its name and one by using parantheses.

The first one looks like this:

```perl
# Some code ...

some_func;

# ...
```

Nice and stright forward isn't it? Yes it is! And its mostly used for built-in subroutines but can be used for custom ones as well.

Though what I did *not* know is this:

**If you use it for custom subroutines, you must declare them before usage.**

Like this:

```perl
# Some code ...

sub some_func() {
    # ...
}

some_func;
```

If you do not, Perl will not be able to compile.

The reason this is - and this is **my speculation** please correct me if I am wrong - that when a symbol like this is used, it checks
somewhere if this is a known symbol. If it is, it is replaced by a subroutine call. If not -> you get the error that I was having.

There is another syntax however, which may look much more familiar to most of you.

```perl
# Some code...

some_func();

sub some_func() {
    # Some functionality...
}
# ...
```

In this case you **can** call the function before declaration as Perl handles this as a proper subroutine call - potentially with arguments - and
jumps to - or searches for - the declaration. I kid you not. *This was it.* I added the parantheses and it was *fine*.

This was a proper head-meets-desk moment.

Using the `some_func();` syntax, you can declare the function wherever you like in your file and Perl will find it. The only reason I found
why this exists is literally *"because other languages do it like this as well..."* - yeah and other languages don't have a defined behaviour tree. 
Or let you multiply a String with a Class. *You don't have to be like Lua or JavaScript now do you?*

In all seriousness though, it may not seem like a big deal - and really, it isn't - but it's somehwat inconsistent in my opinion.

## Why I didn't catch this sooner

You **could** ask now why I didn't catch this sooner as most languages use the second syntax unless they do weird stuff with macros - in which case
it is clear that they are macros - and that would be a valid point.

Though given the fact that I learn by doing and observing others and I took heavy inspiration from existing test files which use the first way of calling
subroutines, I never noticed anything odd. At least nothing that I couldn't put on Perl just doing things differently.

Thing with these tests I took inspiration from is, they use functionality that is not defined in that file. Not even in that repo.

You see, `os-autoinst-distri-opensuse` is not the only test component openQA uses. There is also `os-autoinst` which provides - amongst others - 
a lot of libraries and shared functions for openQA to work. Which would be fine if that was documented. Which it isn't.

Which brings us down a rabid hole about modularization and consolidation but that'd go to far for now.

I just wanted to make you all aware of some of the weird quirks you'll fine when doing Perl.

Thanks for reading, see you next time.
