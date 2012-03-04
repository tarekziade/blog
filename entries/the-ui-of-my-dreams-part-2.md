Title: The UI of my dreams, part 2
Date: 2011-01-23 13:58
Category: mozilla, ux

I had a lot of feedback on [my previous blog post about the UI of my
dreams][].   
  
Some people said that a tiling windows manager, like [xmonad][] would
solve this problem if every application like Firefox, Thunderbird, or
the Terminal was managed like a regular window.   
  
So I gave xmonad a shot during a week.   
  
I really liked it ! It basically does with all windows what I am
already doing within VIM in split mode: when a new window is open, it's
added vertically or horizontally besides an existing window. It's easy
to move the focus from one window to the other, and adapt the size of
each window. The whole screen is effective and you don't waste time
anymore by rearranging your windows with the mouse. And you can have up
to nine desktops (==workspaces). Granted, you cannot save their states,
but it seems that this will be the case in the future.   
  
So the question is: can xmonad across 9 desktops replace Panorama ?   
  
Greg commented by blog post:   
> To me, Panorama groups are equivalent to other workspaces; and tabs in
> other groups are equivalent to windows/documents on other workspaces.
>   
>    
>  Gnome are working on making the contents of workspaces persist, which
> matches your use of tab groups as persistent identifiers.   
>    
>  Scale (and presumably Exposé) can be used to show just “this”
> workspace, and it would be this mode you’d normally use to see just
> the tabs/documents you’re interested in right now.

  
But my own usage of tabs goes beyond this. For one workspace --
understand one working context --, I can have more tabs opened than the
screen can fit. I don't want to have them all open in my screen. Tabs
are more like ***active bookmarks***.   
  
For example, when I am working I can have:   
-   one vim session that displays 2 windows: the code and its test
-   sometime a second vim session for another pending work
-   two terminals, one to run the tests and one to manage my mercurial
    queues
-   up to 10 opened tabs in Firefox. Bugzilla bugs, technical doc, etc.
-   some Thunderbird tabs

  
By using xmonad, I can organize the screen to have one vim session, and
one or two terminals to ***code***. But as soon as I need to **read**
documentation or bug descriptions, I need to display Firefox and browse
some tabs.   
  
And I don't want to use another Desktop for this. I have one for my
personal stuff like managing my servers, I have one for Python
development, one for organizing my trips, one for music etc. And they
all use Firefox, VIM sessions, Terminals etc.   
  
So switching from ***coding*** to ***reading*** when I work on
something, should be done within the same desktop. In other words, I
could use something like Panorama to display different organizations for
the same desktop. I could organize windows in Panorama categories like
"*coding"* and "*reading"* and define a desktop as **work** and another
one a **travels**.   
  
So the UI of my dream could be:   
-   xmonad or any tiling windows manager
-   One Panorama-like tool instance *per workspace*.
-   A global way to configure shortcuts. (VIM mode for me)

  [my previous blog post about the UI of my dreams]: http://tarekziade.wordpress.com/2011/01/14/the-ui-of-my-dreams-firefox-terminal-thunderbird-unified
    "Previous blog post"
  [xmonad]: http://xmonad.org/ "XMonad"
