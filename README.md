# Diet-Tracker-Website
Diet-Tracker-Website consists of a basic front end, back end, and python code that runs on a raspberry pi.
The code on the raspberry pi was to receive/process weight information from a strain gauge and take photos of the nutritional labels on packaged foods.  
The photos would be sent to an AWS service called [Textract](https://aws.amazon.com/textract/), which would return machine-readable text that is extracted from the photo.

The back end was written in python using the Django framework. The front end was written in plain javascript with HTML and CSS. The user is presented with a  controllable graph, which provides options to show how much energy, fats, protein and carbs were consumed on a daily, weekly or monthly basis.

The diet tracker system was built as part of a group project that was part of my bachelor degree.  
A demonstration can be viewed [here](https://streamable.com/syd3qt)
