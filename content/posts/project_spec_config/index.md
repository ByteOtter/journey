---
title: "Project specific LSP configs with LunarVim"
date: 2024-08-07T19:30:15+02:00
draft: false
heroStyle: background
tags: ['Programming', 'Tutorials & Guides']
---

When I start a new project, one of the first things I want to take care of is setting 
up my environment and tooling.

You know, stuff like my directory structure, readme, git repo, workflows and PR as well as 
issue templates. And also any configuration of my editor.
The latter I did not really need to get into very much - aside from the typical global stuff 
like installing language servers, etc - as I my projects up until now were 
fine with the defaults.
Stuff that I needed to change - like the configuration of linters, etc. - I did as these 
usually require configuration files in the project directory anyway.

Lately though, I had to experiment with project specific configurations, as some of the 
projects I worked on required special configuration of things like the language server 
or my editor's formatting. Things I did not want to change in a global config.

For my work on [menix](https://github.com/menix-os) we used the [`.editorconfig`](https://editorconfig.org) 
format to specify tings like character sets and the styles and sizes of tabs we use. 
This is actually really cool, as this allows you to set different formatting styles for differen 
kind of code files. For example you want to use tabs consisting of 4 spaces in `C` code files, while 
staying with a tab-character in your Makefile.

While this is really cool and helpful to assert your desired code style for outside contributors, as 
the `.editorconfig` file is respected by all major IDEs and texteditors I know of, it does not really 
allow you to configure things like your LSP for example.

This is usually done in the configuration of your editor or IDE.

And while this is usually easy enough to do, it can be a hassle to configue such things by project, 
instead of doing it globally for every project using this language.

Things like `rust-analyzer` for example, the language server which Rust uses, does not have a way to 
configure how it should check your project for each project individually. Instead you need to configure 
it globally.
It may be that VSCode, or the JetBrains tools have something like profiles you could configure and 
switch between, but I found using VSCode in larger Rust projects to be a graveyard for my memory 
and the JetBrains stuff is fucking expensive, so I don't really know if they do.
I have fully switched to [`LunarVim`](https://lunarvim.org), a `neovim` distribution, I will **definitely** 
have to make a guide for in the future, which - while very customizable and easy to modify - does not 
allow for project specific LSP configs.

Well, at least that's what the internet said.

## Why I Need this

Before I tell you, what I did to solve this issue, I should start with what my issue is in the first place.

Nowadays I mostly write Rust. I have a major project going on in my free time called [`Nazara`](https://github.com/The-Nazara-Project) 
and at work I am developing a library for [`openQA`](https://open.qa), called [`isotest-ng`](https://github.com/ByteOtter/isotest-ng),
which will one day modularize the backend of this project.
One of the three libraries in this project provides a logging functionality - as you should.
For this logging funcitonality I provide a `feature` the user of the library can activate, which will provide a default implementation 
of a logger using the `env_logger` crate. I did this to ship some form of a `Logger` instance with the library which will format the 
logs in a sensible way.
The interesting thing about logging in Rust is now that, the `macros` themselves which indicate the log level and conduct the actual 
logging of messages and events are ignored, as long as no Logger is created. Also, these `macros` are able to be evaluated by a variety 
of third party logging crates aside form `env_logger`. So, to provide the user the ability to choose their own favourite crate responsible 
for logging, or to omit logging completely, I turned this into an optional feature.
This would also mean, that they would not have to download or compile an additional `env_logger` dependency if they do not wish to use 
the default Logger configuration.

The code which provied this `default-logging` feature however, is ignored by `rust-analyzer` checks by default. 
You have to manually tell it to build your project with all features enabled in order to get code annotations.

This is easy enough, however I may not want to do this for all my projects.

So this is where `.lvim-config.lua` comes in.

## Drop-In Configs with Lua

As I said before, `LunarVim` and `rust-analyzer` only provide a native way to set LSP config options globally.

For `LunarVim` the configuration would be pretty simple:

```lua
-- ~/.config/lvim/config.lua
local lspconfig = require('lspconfig')

lspconfig.rust_analyzer.setup {
    settings = {
        ["rust-analyzer"] = {
            cargo = {
                allFeatures = true,
            },
        },
    },
}
```

This would be all I need to put in my `LunarVim` config file, and it would configure `rust-analyzer` at startup to build 
the project with all features enabled.

As I wanted to do this per project, however, I would have to put this snippet into a config file located in my project root and tell 
`LunarVim` to look for it and execute the code inside.

So I added code to my `config.lua` file to check if the current working directory contains a file named `.lvim-config.lua` and execute 
the code inside, if it is present.

```lua
-- search for .lvim-config.lua file in the current directory.
local project_config = vim.fn.getcwd() .. "/.lvim-config.lua"
if vim.fn.filereadable(project_config) == 1 then
    dofile(project_config)
end
```

In practice, this would then expand into the above snippet to configure `rust-analyzer` on startup to use the optional features of my 
project.
But I could essentially put any kind of config for `LunarVim` in there. If I wanted to I could have it use a different colorscheme for 
every project, or have certain plugins installed or activated.

I admit, it's not a perfect solution. For example, if I were to open `LunaVim` in a subdirectory of this project I'd be out of luck. 
And also, it only applies to LunarVim - which is not really the most common `NeoVim` flavour.

But it works for me and that's what counts, right?

Anyway, if you want you can find [my full LunarVim config](https://gist.github.com/ByteOtter/1465245bb65d9802e8c0bdd4d3d337b6) 
and the [`.lvim-config.lua`](https://gist.github.com/ByteOtter/e58999eb079e843fdac15a94d6d6463b) I used as Gist on GitHub.

I hope you enjoyed this little update. See you next time. :otter:
