Web Application Firewall
########################

:date: 2014-10-24 16:41
:tags: nginx, lua, mozilla
:category: lua
:author: Tarek Ziade


Web Application Firewall (WAF) applied to HTTP web services is an interesting
concept.

It basically consists of extracting from a web app a set of rules that describes
how the endpoints should be used. Then a Firewall proxy can enforce those
rules on incoming requests.

Le't say you have a search api where you want to validate that:

- there's a optional *before* field that has to be a datetime
- you want to limit the number of calls per user per minute to 10
- you want to reject with a 405 any call that uses another HTTP method than GET


Such a rule could look like this::

    "/search": {
        "GET": {
            "parameters": {
                "before": {
                    "validation":"datetime",
                    "required": false
                }
            },
            "limits": {
                "rates": [
                    {
                        "seconds": 60,
                        "hits": 10,
                        "match": "header:Authorization AND header:User-Agent or remote_addr"
                    }
                ]
            }
        }
    }


Where the rate limiter will use the Authorization and the User-Agent header to uniquely
identify a user, or the remote IP address if those fields are not present.

.. note::
   We've played a little bit around request validation with
   `Cornice <http://cornice.readthedocs.org/en/latest/>`_, where you can programmatically
   describe schemas to validate incoming requests, and the ultimate
   goal is to make Cornice generate those rules in a spec file independantly from the code.


I've started a new project around this with two colleagues at Mozilla (Julien & Benson), called
**Videur**. We're defining a very basic JSON spec to describe rules on incoming requests:

https://github.com/mozilla/videur/blob/master/spec/VAS.rst

What makes it a very exciting project is that our reference implementation for the proxy is
based on NGinx and Lua.

I've written a couple of Lua scripts that get loaded in Nginx, and our Nginx configuration
roughly looks like this for any project that has this API spec file::

    http {
        server {
            listen 80;
            set $spec_url "http://127.0.0.1:8282/api-specs";
            access_by_lua_file "videur.lua";
        }
    }


Instead of manually defining all the proxy rules to point to our app, we're simply
pointing the spec file that contains the description of the endpoints and use the
lua script to dynamically build all the proxying.

Videur will then make sure incoming requests comply with the rules before passing
them to the backend server.

One extra benefit is that Videur will reject any request that's not described
in the spec file. This implicit white listing is in itself a good way to avoid
improper calls on our stacks.

Last but not least, Lua in Nginx is freaking robust and fast. I am still amazed
by the power of this combo. Kudos to `Yichun Zhang <https://github.com/agentzh>`_
for the amazing work he's done there.

**Videur** is being deployed on one project at Mozilla to see how it goes,
and if that works well, we'll move forward to more projects and add more features.

And thanks to `NginxTest <http://blog.ziade.org/2014/06/29/nginxtest/>`_ our Lua
script are fully tested.

