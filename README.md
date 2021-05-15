<a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/ketsbp2oe3jyotige4dk" alt="trackgit-views" />
</a>

# Cancel Instagram Follow Requests
A simple script that automatically gets all the people you have sent follow requests and cancels them all with ease.

If you have a long list of unresponded follow requests then you can cancel them. I don't know why but there isn't a simple way to do that. I wanted to do that for my business account so I created this on my own a few months ago. Here this tool works in two parts, in the first part, it logs in your IG account via username and password and gets all the handles whom you have sent a follow request. Next, then it gets all those names in a file and uses unofficial Intagram API to cancel those in bulk.

The endpoint to get current follow requests isn't availale in the official API or the graph API, so I had to go for the scraping. Here it runs on Python3 and uses Chrome driver to automate everything, you just have to specify the usernam and password and it will take care of the rest. I have tested it on Linux and Windows, should work on MAC too.

#### Steps to use it on Windows and Linux:

**Step 1**: Download Python 3.x from here: https://www.python.org/downloads/ and download Chrome driver from here: https://chromedriver.chromium.org/downloads<br>
**Step 2**: Put the `chromedriver.exe` file in the repository root and then double click on the `requirements.bat` file to install the dependencies. On Linux, you have to run the commands listed in the BAT file manually(may require `sudo`).<br>
**Step 3**: Edit the "loginInfo.py" file and specify your username and password inside doule quotes.<br>
**Step 4**: Finally start the script by openign command prompt in the root of the repo and type `python get_follow_req.py`. Next, sit back and relax and watch it in action.<br>

#### Known Issues:

---> Won't work on Instagram accounts having 2 Factor Authentication.<br>
---> May not work properly on slow internet connection.<br>

#### Screenshot(OpenSuse Linux):

<p align="center"> 
<img src="https://github.com/Suleman-Elahi/Cancel_InstagramFollowRequests/blob/master/cancel%20req%20in%20action.png">
</p>

~Ps I am not an expert in scraping and Python so the code here may be laughable but it works. Any suggestions are welcome tho.

