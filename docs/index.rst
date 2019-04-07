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

Day 9: March 22, 2019
---------------------

**Today's Progress:**

1. Working with sockets. Creating Basic Client and Server

**Thoughts:** Basic Socket Connectivity and Fixing Linters and some bugs in the Linting Script. Learning about how to skip a specific pylint in a specific file.

**Link to work:**

1. See `Basic Socket Client and Server <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/socket_programming>`_

Day 10: March 23, 2019
---------------------

**Today's Progress:**

1. Working with sockets. Creating Advanced Client and Server

**Thoughts:** Need to study more about sockets and focus on how to apply on infra and network debugging tools

**Link to work:**

1. See `Advanced Socket Client and Server <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/socket_programming>`_

Day 11: March 24, 2019
---------------------

**Today's Progress:**

1. Playing with fbprophet, Forecast from Facebook

**Thoughts:** Nice one to understand how to play with dates and Pandas and doing some data forecasting with Python

**Link to work:**

1. See `Python Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/forecasting>`_
2. See `URL with some tips and data <https://mode.com/example-gallery/forecasting_prophet_python_cookbook/>`_

Day 12: March 25, 2019
---------------------

**Today's Progress:**

1. Docker Creation for Data Science
2. Matplotlib Tutorial

**Thoughts:** Good Docker to Play with DataScience and Jupyter without breaking my environment

**Link to work:**

1. See `Matplotlib Tutorial <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/plotting>`_
2. See `Docker DataScience <https://github.com/imjoseangel/docker-data-science>`_

Day 13: March 28, 2019
---------------------

**Today's Progress:**

1. Created Speech Recognition Script with Command Execution

**Thoughts:** Google Speech Recognition works fine. Probably quite slow if you are impatient ;)

**Link to work:**

1. See `Speech Recognition <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/speech>`_

Day 14: March 31, 2019
---------------------

**Today's Progress:**

1. Created Men Restroom Algorithm

**Thoughts:** Idea from `Reddit <https://www.reddit.com/r/learnpython/comments/b7kq94/men_restroom_algorithm/>`_

**Link to work:**

1. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_

Day 15: April 1, 2019
---------------------

**Today's Progress:**

1. Adding Threading and Average to Men Restroom Algorithm

**Thoughts:** Investigating Threading although not easy to stop process when list is full. Needs further investigation

**Link to work:**

1. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_

Day 16: April 2, 2019
---------------------

**Today's Progress:**

1. Fixing Wifi and Code for Python 3 for DisplayOtronHat from Pimoroni

**Thoughts:** Wifi Display didn't work in Python3 due to the map/list difference

**Link to work:**

1. See `Pull Request on Pimoroni <https://github.com/pimoroni/displayotron/pull/59/files>`_

Day 17: April 3, 2019
---------------------

**Today's Progress:**

1. Adding Some Wifi and Inky from Pimoroni examples and Thinking about some Men Restroom algorithm changes

**Thoughts:** Not easy to split men in stall. Need some thoughts to distribute them.

**Link to work:**

1. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_
2. See `InkyTest <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/pimoroni>`_
3. See `WifiTest <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/wifi>`_

Day 18: April 4, 2019
---------------------

**Today's Progress:**

1. Starting Machine Learning Project Walk-Through in Python

**Thoughts:** Nice one to settle ML knowledge.

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/machine-learning>`_
2. See `Original Project <https://morioh.com/p/b56ae6b04ffc/a-complete-machine-learning-project-walk-through-in-python>`_

Day 19: April 6, 2019
---------------------

**Today's Progress:**

1. Continuing with Machine Learning Project Walk-Through in Python

**Thoughts:** Need to focus in the two variables plot as from there the data is not properly working. I will investigate how to fix it.

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/machine-learning>`_
2. See `Original Project <https://morioh.com/p/b56ae6b04ffc/a-complete-machine-learning-project-walk-through-in-python>`_

Day 20: April 7, 2019
---------------------

**Today's Progress:**

1. Continuing with Machine Learning Project Walk-Through in Python
2. Finishing Men Restroom Algorithm. Now supporting taking alternate further stalls to the door

**Thoughts:** Fully Working Projects Now. Need to finish Voice Recognition with API, Swagger and SQLLite

.. note:: For the ML Project, only finished first part

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/machine-learning>`_
2. See `Original Project <https://morioh.com/p/b56ae6b04ffc/a-complete-machine-learning-project-walk-through-in-python>`_
3. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_
