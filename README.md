# simple_gui

This is a simple app with a Graphic User Interface using tkinter in Python3. This was just a small project to explore tkinter. May expand this to something larger at a later time.
This app allows you to set the text in the main text field to anything you want, allows you to change the color of the text, and reverse the text to display backwards as well.
The text does not dynamically change with the window size, and the window size is preset to be 400x400.

![simple_text_gui](https://user-images.githubusercontent.com/83800421/200504214-31a2d2e9-4210-4bc4-9820-34e4a056c62f.png)

Current Issues:

- Gray Background for the main Label "Hello There".
- Gray Background for the Set Text input field, Set Text button, Set Color dropdown menu, Set Color button, and Reverse Text button.
  - Note: The backgrounds defaulting to gray seems to be based on the current light or dark theme applied to macOS. Needs to be looked into via tkinter documentation. Size of the drop-down menus also slightly changes when the macOS them is changed from light mode to dark mode. When in dark mode, the box extends closer to the border of the window.
