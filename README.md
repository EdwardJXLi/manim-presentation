# Manim Presentation
Hacky Project To Allow Presentation Of [3b1b/manim](https://github.com/3b1b/manim) Scenes.  
Allows users to stop and play to specific points (or aka "slides") using mouse or keyboard controls   
Hacked together within an hour as a prototype.

## Installation:
Grab and install any recent version of [Manim](https://github.com/3b1b/manim)  
Drag and drop `presentation.py` into the `manimlib` folder  
Done!

## Usage (Rendering):
Import the presentation library alongside the manimlib library  
```
from manimlib.imports import *
import manimlib.presentation
```
To create a slide, add `self.create_slide()`  
```
self.play(FadeIn(s1))
self.create_slide()
self.play(FadeOut(g2x))
self.create_slide()
```

## Usage (Webpage):
When rendering, Manim Presentation should create `<SceneName>Timecodes.txt` alongside the video file  
In the webpage, select the Video file and the Timecodes file  
Press Present  
Use arrow keys or click anywhere on the screen to change slides

## TODO / Future:
- Redesign Website
- Allow rendering directly on the web using [pyiodode](https://github.com/iodide-project/pyodide)  
    (Similar to [EulerTour](https://github.com/eulertour/eulerv2) or [ManimOnline](https://github.com/flwfdd/ManimOnline))
- Implement using [proposed API](https://github.com/3b1b/manim/pull/609)
- Allow more fine-grain control over videos
- Allow playing multiple scenes in sequence