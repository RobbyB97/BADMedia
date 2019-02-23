# BADMedia
## Overview
 BADMedia is a project that can generate webpages customized specifically to a user's interests. Unlike social media, which relies on the cooperation of the producers of the media and confines the consumption of media to their application, BADMedia can aggregate media of any format to be consumed either directly through the webpage or downloaded to be consumed later.

 This is made possible through XML/RSS feeds (you know, those things typically used as nothing more than background noise on ad-invested news blogs?) Most prominent producers of media have these, and all a user need do is enter it into the BADMedia program to keep themselves updated on the producer through an encapsulated section of their webpage.

  This is by far the least constrained way to keep a user up-to-date on whatever interests them most and can supply media that interests them. If the user is ever going on a flight or knows they will not be able to access the internet for some time, they are no longer restricted to whatever entertainment they would otherwise be subjected to without the help of BADMedia. This is because every unit of media on a BADMedia page can be downloaded at the click of a button. (Except youtube videos)

___

<img src="./images/badmediaexample.png" alt="screenshot of prototype webpage" width="100%" height="auto">
Here is a sample of a BADMedia page, which shows real-time updates from NASA, StarTalk podcast and youtube channel 'Amazing Space' (This user clearly loves space, and is able to click on the images to learn more about them, listen to his favorite podcast through the site or download it, and watch the latest videos from a youtube channel he is subscribed to)

___
## How it works
  The main Python file takes input from the user to convert the relevant content of a given RSS feed into a JSON object, which is added to a list of all the user's media. Then, an HTML file is dynamically generated to convert the JSON objects into encapsulated sections of the BADMedia page.

  '''json
  {
    "indent_size": "4",
    "indent_char": " ",
    "max_preserve_newlines": "5",
    "preserve_newlines": true,
    "keep_array_indentation": false,
    "break_chained_methods": false,
    "indent_scripts": "normal",
    "brace_style": "collapse",
    "space_before_conditional": true,
    "unescape_strings": false,
    "jslint_happy": false,
    "end_with_newline": false,
    "wrap_line_length": "0",
    "indent_inner_html": false,
    "comma_first": false,
    "e4x": false,
    "medianame": "title given by user",
    "mediatype": "audio, video, text, image or youtube",
    "media": {
      "1": "url",
      "2": "url",
      "3": "url"
    }
  }
  '''
