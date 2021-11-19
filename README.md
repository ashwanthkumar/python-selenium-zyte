# python-selenium-zyte

Python + Selenium + Zyte (Crawlera) integration example.

## Usage
Install all the required dependencies:
```
$ pip install -r requirements.txt
```

Download and keep the [chromedriver](https://chromedriver.chromium.org/downloads) in PATH. Choose the right version based on the version of chrome that's installed on your machine. You can check that at [chrome://version](chrome://version).

Run the selenium code (no proxy):
```
$ python try_crawlera.py
```

With proxy for HTTP requests:
```
$ HTTP_PROXY="http://<api-key>:@<zyte-host:port>" python try_crawlera.py
```

With proxy for HTTPS requests:
```
$ HTTPS_PROXY="http://<api-key>:@<zyte-host:port>" python try_crawlera.py
```

## Notes
- We use [selenium-wire](https://github.com/wkeeling/selenium-wire) to inject authenticated proxy settings for Chrome (or any other underlying browser)
- We need to pass the proxy configurations as an environment variable instead of hard-coding it.

