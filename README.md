# ISP Tester and Twitter Bot

This program runs an internet speed test, compares the result to the speed promised
by an internet service provider and then optionally tweets the service provider if the 
internet is slower than promised.

## How the Application Works
1. Initialises a Selenium webdriver and automatically runs an internet speed test using 
https://www.speedtest.net/
1. Scrapes the speed result from the website and compares to the value promised by 
the ISP.
1. If the speed is too slow and login details have been provided for a twitter account,
then the webdriver navigates to the twitter website, logs in and sends a complaint tweet to the 
ISP.
<br>

|             Automated Internet Speed Testing:           |                  Twitter Bot:                    |
| ------------------------------------------------------- | ------------------------------------------------ |
| <img src="/images/automated-speed-test.png">            |<img src="/images/twitter-complaint.png">         |

## Using the Application
* Download main.py or clone this repository.
* Install Selenium using pip.
* Download the correct Selenium binary for the operating system and browser you wish to use:
 <https://www.selenium.dev/documentation/en/webdriver/driver_requirements/>
* Enter your minimum expected download speed as the PROMISED_DOWN variable in main.py.
* If you wish to tweet your ISP when the internet is slower than expected, then also provide
 your twitter authentication details and ISP twitter handle (TWITTER_EMAIL, TWITTER_PASSWORD 
 and ISP_TWITTER_HANDLE variables)
* Run main.py to commence the speed test. 


## Supporting Libraries and APIs
* Selenium (for browser automation and webscraping): https://www.selenium.dev/documentation/en/webdriver/  

## Future Development
* This program still makes use of time.sleep() while waiting for some webpages to load - I intend to swap in explicit waits shortly. 
