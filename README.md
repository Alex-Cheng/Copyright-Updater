==================
Copyright Updater
==================

Usage
======

Check copyright statements in .cs files of a specified changelist. Update them if outdated.


Install and Config
===================

1. Install Python. Version 2.7 to 3.x should all work, although I’ve only tested it with Python 3.3.
2. Install P4 API for python.
3. Put the two scripts in your folder. 
4. Create a custom tool in P4V:
    * Check "Add to applicable context menus"
    * Application set to ``Path\To\Collab.cmd``
    * Arguments set to ``$p $u $c %c``
    * Start in set to empty.
    * Check "Run in terminal window" and "Close window upon completion"
4. Rock and Roll!


Possible Issues
================

* python.exe may not be in system path so you may need to add it manually. 
* P4 connection fails – Usually happens when you have changed P4 server. Solution: Run ``p4 set P4PORT=yourserver:port``. Before this you can run ``p4 set`` to see if it’s configured correctly. This command changes windows registry so it is a one-time effort.
* ???
