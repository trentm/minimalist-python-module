A stab at a minimalist repo supporting a single Python module.
Spurned by <http://twitter.com/jessenoller/status/19853449226> 
(who still owes me a beer, BTW).  

Q&A


# Why the "lib" subdir?

Allows nicer 3rd-party usage via 'svn:externals' -- historically when I was
using Subversion more. Allows one to put the "lib" dir on PYTHONPATH and not
have the "setup.py" and other supportive ".py" files unintentionally get on the
import path. Separates the important code from the chaf.

@voidspace: I still don't like the "lib" dir.


# I want to use "README.md" for Markdown rendering on github.com

Then you'll need to add a "MANIFEST.in" for "python setup.py sdist" to pick
up the README file. It only picks up either "README" or "README.txt" by
default.


# default MANIFEST considered harmful?

@voidspace notes that he typically includes a "setup.cfg" and "MANIFEST.in",
for example https://code.google.com/p/mock/source/browse/#svn/trunk

It looks like his main usage of "setup.cfg" is to turn off default MANIFEST processing.
I've not dug into that in distutils/setuptools to know if the presence of
"MANIFEST.in" alone would be sufficient.


# The "setup.py" is a little hefty

Fair enough, you could argue that. I'd welcome suggestions on paring that
down. I'm a fan of importing the main module (here `mpm`) to be able to get
the version from it. A static data file that supported specifying all this
same info would be cool. I'm not up on latest latest Python packaging stuff
to know if something like that has been proposed.


# What's left TODO?

- do I need to use `setuptools` in "setup.py" or will distutils do?
- discuss
- a good minimalist *python-land* module's README should probably use
  reStructuredText, but I'm a Markdown fanboy



