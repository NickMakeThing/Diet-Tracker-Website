# Diet-Tracker-Website
Diet-Tracker consists of a basic website backend, website frontend, and Python code that runs on a Raspberry Pi. This repository holds code for the website's backend and frontend.
The purpose of the code on the Raspberry Pi was to receive/process weight information from a strain gauge, and take photos of nutritional labels on packaged foods.  
The photos would be sent to an AWS service called [Textract](https://aws.amazon.com/textract/), which would return machine-readable text that is extracted from the photo.

The website backend was written in python using the Django framework. The front end was written in plain Javascript, HTML, and CSS. The user is presented with a controllable graph, which provides options to show how much energy, fats, protein, and carbs were consumed on a regular basis. The user may select from a range of timeframes (daily, weekly, monthly).

The code/scripts that ran on the Raspberry Pi can be found [here](https://github.com/NickMakeThing/Diet-Tracker-Rpi)

~~The diet tracker system was built as part of a group project that was part of my bachelor degree.  
A demonstration can be viewed [here](https://streamable.com/syd3qt).~~ <sub>Video link died. Need to find video file and upload it to youtube.</sub>



