A stab at a minimalist repo supporting a single Python module.
Spurned by <http://twitter.com/jessenoller/status/19853449226> 
(who still owes me a beer, BTW).  Q&A style:


# Why the "lib" subdir?

Allows nicer 3rd-party usage via 'svn:externals' -- historically when I was
using Subversion more. Allows one to put the "lib" dir on PYTHONPATH and not
have the "setup.py" and other supportive ".py" files unintentional get on the
import path. Separates the important code from the chaf.

# What's left TODO?

- do I need to use `setuptools` in "setup.py" or will distutils do?
- discuss
- a good minimalist *python-land* module's README should probably use
  reStructuredText, but I'm a Markdown fanboy



