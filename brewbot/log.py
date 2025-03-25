from enum import Enum
from sys import exit

import math
import time

class Level(Enum):
    Info = 0
    Success = 1
    _Warning = 2
    Error = 3
    Panic = 4

class Log:
    def __init__(self, verbosity, log_descriptor):
        self.verbosity = verbosity
        self.log_descriptor = log_descriptor
        self.hard_log_descriptor_override = False 
        self.writing_format = "[*k % *t]:: "
        self.old_format = ""
        self.recognized_formats = ["[*k % *t]:: ", "*k *t: ", "[*k ^^ *t]:: "]
        self.message_index = 0
    
    def change_verbosity(self, n: int):
        if n > 3:
            raise ValueError("Cannot be more verbose than 3!")
            
        self.verbosity = n
        
    def change_log_descriptor(self, descriptor_location: str):
        self.log_descriptor = descriptor_location
        self.hard_log_descriptor_override = True
    
    @staticmethod
    def puts(msg: str, location="/dev/stdout"):
        with open(location, "w") as descriptor:
            descriptor.write(f"{msg}\n")
     
    def get_fmt_on_ctx(self, ctx: Level):
        # store old format to variable
        self.old_format = self.writing_format

        match ctx:
            case Level.Info:
                self.writing_format = self.writing_format.replace("*k", "INFO")
            case Level.Success:
                self.writing_format = self.writing_format.replace("*k", " OK ")
            case Level._Warning:
                self.writing_format = self.writing_format.replace("*k", "WARN")
            case Level.Error:
                self.writing_format = self.writing_format.replace("*k", "FAIL")
            case Level.Panic:
                self.writing_format = self.writing_format.replace("*k", "EXIT")
            case _:
                raise ValueError("Ctx level is invalid!")
        
        self.writing_format = self.writing_format.replace("*t", str(self.message_index))
    
    def restore_old_format(self):
        self.writing_format = self.old_format

        # fallback to default if old format is not in one of 
        # few recognized formats, indicating restoration wasn't 
        # successful

        if self.writing_format not in self.recognized_formats:
            print("-- BrewBot-Logger: Cannot restore old format! Falling back to default")
            self.writing_format = self.recognized_formats[0]

    def log_write(self, level: Level, msg: str):
        original_format = self.writing_format  # Save the original format
        self.log_descriptor = "/dev/stdout"
        self.get_fmt_on_ctx(level)
        
        match self.verbosity:
            case 0:
                self.log_descriptor = "/dev/null"
                
            case 1:
                print("-- BrewBot-Logger: Verbose level 1 overrides self.log_descriptor to `/dev/stdout`!")
                self.log_descriptor = "/dev/stdout"
                self.writing_format = "*k *t: "
                
            case 2:
                pass
                
            case 3:
                print("-- BrewBot-Logger: Verbose level 3 overrides self.log_descriptor to `/dev/stdout`!")
                self.log_descriptor = "/dev/stdout"
                self.writing_format = "[*k ^^ *t]:: "
                
            case _:
                print("-- BrewBot Logger: Unknown Verbose level. Defaulting to level 1")
                self.verbosity = 1
                
        if level == Level.Panic:
            Log.puts(f"{self.writing_format} {msg}", self.log_descriptor)
            exit(1)
        else:
            Log.puts(f"{self.writing_format} {msg}", self.log_descriptor)
        
        self.message_index += 1

        self.writing_format = original_format  # Restore the original format

