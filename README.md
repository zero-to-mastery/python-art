# Python-Art 🎨🖌️

> ### **UPDATE:**  Project Archived!
> **This project has been archived to preserve its state at the end of Hacktoberfest 2019. Thank you to everyone that participated and made this project what it is tody and we look forward to seeing you all at Hacktoberfest 2020!
> Interested in more events? keep an eye on our Events page [HERE](https://zerotomastery.io/events?utm_source=github&utm_medium=python-art)**
____

#### [![](https://img.shields.io/badge/PYTHON%20PROJECT-ASCII%20Art%20-blue?style=for-the-badge&logo=Python)](./ASCII-Art/)
> Following the launch of the brand new [Complete Python Developer: Zero to Mastery](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/?couponCode=LEVELUPZTM) course, here is a perfect opportunity to put those new found skills to the test. Here we will be using Python to take an image input which it will then convert into ASCII Art.

# How to get Started:
In order to get started on this project, I recommend you watch the section on **Scripting** in the [Python course](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/?couponCode=LEVELUPZTM). We talk about ```sys.argv``` and ```Pillow``` library (Image processing) in that section which would help you!

1. Clone this repo
2. Make sure you have Python v3.6 (or greater) installed on your machine
3. Install the project dependencies `pip install -r requirements.txt`
4. run the command: `python3 make_art.py -i zeroToMasteryIcon.png -c 1` or `python3 make_art.py -i zeroToMasteryIcon.png -c 2` for a more clear output [zoomout a little bit]
5. Stare with amazement 😮


**All discussions around this event can now be had in our #hacktoberfest-2019 channel on Discord!**

# Running Tests

> Make sure you have all the dependencies installed, check step 3, **How to get Started** section

To add new test cases 
- Check *test_unit.py* module and start creating your test methods
- Or create a new test module, for naming conventions check pytest docs (link below)
- Run `pytest -v` command to run all the tests discovered by pytest

[Click](https://docs.pytest.org/en/latest/contents.html) for more imformation about **pytest**

# Need to convert an image into ASCII?

A webportal for converting images into ASCII! 
Link to portal :- [Click](http://13.127.254.208/cgi-bin/pythonascii/print)

# How to contribute?

Now that you see how this command line tool works, let's see how we can evolve it with our ZTM community help!! Maybe we want to display this on an HTML web page where users can submit images and we convert it to ASCII art? Maybe we want to improve how the Command Line Tool works/make it more customizeable? Or maybe modify the script to do many other types of art beyond ASCII. 

The options are endless and there is no wrong answer. This is all for fun, so try to customize the tool whichever way you think would be best and let's see what we get at the end of the month! Enjoy! 

### Bonus Task:
We have left the original code which was written in Python 2 under the `make_art_python2.py` file. See what happens when you run it with Python 3. See all of the errors? Can you fix it so it works with python 3? The answer is with the `make_art.py` file which is written in Python 3.

> If you have installed new project dependencies, before commiting and creating any PR make sure to run `pip freeze > requirements.txt`.


# But how do I make a pull request/participate?

> If you've never made a pull request before, or participated in an open source project, we recommend taking a look at our [Start Here Guidelines](https://github.com/zero-to-mastery/start-here-guidelines). This repo has everything you need to learn about open source, with a step-by-step guide to making your very first PR.
> Once you've got your feet wet, you're ready to come back and dive into Hacktoberfest fun!

**Remember, you only need to make 4 pull requests to one of these open source project in the month of October, and you get an awesome Hacktoberfest shirt! Let's see if we can beat the record from last year!!**
