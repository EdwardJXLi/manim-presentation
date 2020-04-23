from functools import wraps
import time
from manimlib.imports import *


'''
Monkey patch and inject presentaion control code into Scene Init
'''
#Code to be run before render
def slide_pre_scene(self):
    #Create Timecodes List
    self.timecodes = []
    
    print(f"\nPresentation Slides Ready")

#Code to be run after render
def slide_post_scene(self):
    #Create Timecode File Location
    timecode_file_extention = ".txt"
    module_directory = self.file_writer.output_directory or self.file_writer.get_default_module_directory()
    scene_name = self.file_writer.file_name or self.file_writer.get_default_scene_name()
    timecode_dir = os.path.join(
        consts.VIDEO_DIR,
        module_directory,
        self.file_writer.get_resolution_directory(),
        add_extension_if_not_present(
            scene_name+"Timecode", timecode_file_extention
        )
    )
    print(f"\nDone Render '{scene_name}'")
    #Save Data To File
    #print(self.timecodes)
    with open(timecode_dir, "w") as timecode_ile:
        timecode_ile.write("\n".join([str(x) for x in self.timecodes]))
    #Output File Location
    print(f"Movie Timecode Saved To {timecode_dir}")

#Save Original Scene Init
old_scene_init = Scene.__init__

#Create New Scene Init
def new_scene_init(self, *k, **kw):
    slide_pre_scene(self)
    old_scene_init(self, *k, **kw)
    slide_post_scene(self)

#Replace Original Init
Scene.__init__ = new_scene_init


'''
Add the create_slide method onto the Scene class
'''
#Helper to add method
def add_method(cls):
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(self, *args, **kwargs)
        setattr(cls, func.__name__, wrapper)
    return decorator

#Add the self.create_slide method
@add_method(Scene)
def create_slide(self):
    #Add Timecode To List
    self.timecodes.append(self.get_time())
    #Print Timecode
    print(f"Added New Slide At {self.get_time()}")
    


'''
Setup Complete
'''
print(f"Manim Presentation Loaded!")