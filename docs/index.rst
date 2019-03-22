Log: 100 Days Of Code
=====================

Day 0: March 10, 2019 (Preparation)
-----------------------------------

**Today's Progress:** Prepare GitHub Repo and Twitter, read documentation.

**Thoughts:** I will start with Python doing Master Python through building real-world applications but I would like to work on a PowerShell Module for Ansible.

**Link to work:**

1. See `imjoseangel GitHub #100HoursOfCode <https://imjoseangel.github.io/100-hours-of-code>`_

Day 1: March 11, 2019
---------------------

**Today's Progress:** Prepare Python Script for Travis and Checking PyLint in all Python Files.

**Thoughts:** Unexpected script for Travis CI to check Lint in all Python Files in the Repo.

**Link to work:**

1. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/scripts/pylint_check.py>`_
2. See `wargames Krypton Level0 -> Level1 <http://overthewire.org/wargames/krypton/krypton0.html>`_

Day 2: March 13, 2019
---------------------

**Today's Progress:** Building an Interactive Dictionary.

**Thoughts:** I have learn that instead of type, isinstance can be used in a conditional, also learning about the `difflib` library to manage words similarities.

**Link to work:**

1. See `dictionary.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/interactive-dictionary/dictionary.py>`_

Day 3: March 14, 2019
---------------------

**Today's Progress:**

1. Create Volcanos in the US Script and play with folium module
2. Improve pylint_check.py script
3. Improve PyLint to have better code
4. Improve Data Read in File Path

**Thoughts:** Good Module to create maps (folium)

**Link to work:**

1. See `map.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/volcanoes-in-the-United-States/map.py>`_
2. See `choropleth.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/volcanoes-in-the-United-States/choropleth.py>`_

Day 4: March 15, 2019
---------------------

**Today's Progress:**

1. Create documentation with Sphinx and readthedocs.io

**Thoughts:** Important for Company Projects and Documentation as Code

**Link to work:**

1. See `100 Days of Code Documentation - Imjoseangel <https://100-days-of-code-imjoseangel.readthedocs.io>`_
2. See `GitHub Documentation <https://github.com/imjoseangel/100-days-of-code/blob/devel/docs/>`_

Day 5: March 16, 2019
---------------------

**Today's Progress:**

1. Adding Pre-Commit to Project and Changing PyLint for Rating
2. Creating Site Blocker for Working Hours

.. note:: Need to create more stable pre-commit based in score and not rc as in CI.

**Thoughts:** Good way of doing CI with python by score.

Check the following code to find matches in lines iterating a list:

    >>> for line in CONTENT:
    ...     if not any(website in line for website in WEBSITE_LIST):

**Link to work:**

1. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/scripts/pylint_check.py>`_
2. See `pre-commit-config <https://github.com/imjoseangel/100-days-of-code/blob/devel/.pre-commit-config.yaml>`_
3. See `webblocker.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/website-blocker/webblocker.py>`_

Day 6: March 17, 2019
---------------------

**Today's Progress:**

1. Studying about `decorators <http://book.pythontips.com/en/latest/decorators.html>`_
2. Continuing Improving pylint_check.py utility

**Thoughts:** Now clearer how using them, but still need to use them more frequently (Logging and Flask)

**Link to work:**

1. See `decorators <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/decorators>`_
2. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/scripts/pylint_check.py>`_

Day 7: March 20, 2019
---------------------

**Today's Progress:**

1. Using Flake8 also for Pre-Commit and Fixing Other Lint Issues
2. Adding Code Complexity to Travis (Just Reporting)

**Thoughts:** Still need to work with py.test and unittest to understand better different scenarios. Adding radon for Code Complexity

**Link to work:**

1. See `radon_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/scripts/radon_check.py>`_

Day 8: March 21, 2019
---------------------

**Today's Progress:**

1. Flask Tutorial Completed

**Thoughts:** Need to work more with Flask to understand better its complexity

**Link to work:**

1. See `Flask Tutorial <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/flask-tutorial>`_
