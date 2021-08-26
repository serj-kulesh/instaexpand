import sys
import os
import pickle
import zipfile
import time
import hashlib
import re
from . import reusable_object_processor_config


class ReusableObjectsProcessor:
    """ Module to save and load serialized objects """
    _instance: object
    _config: dict
    
    STATE_INITIAL = 0
    STATE_INSTANCE_RECIEVED = 1
    STATE_SAVED = 2
    STATE_LOADED = 3
    STATE_ERROR = 666
    
    def __init__(
        self, 
        instance: object = None, 
        *args, 
        config: dict = reusable_object_processor_config.config['default'], 
        filename: str = False,
        **kwargs
    ):
        """
            Instance creation usage
            
            Params:
            
            Position params:
            
            instance: object type
            
            -------------------------------------------------------
            
            Key - value params:
            
            config: dict type of config e.g. 
            config = {
                "save_type": "file",
                "file_directory": os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), 
                    'reusable_objects_tmp'
                )
            }
            
            filename: string type, must not contain special symbols
        """
        self._instance = instance
        self._config = config
        self._filename = filename
        if filename:
            if not re.search('^[\w\.\s-]+$', filename, flags=re.I|re.M|re.S):
                raise TypeError("""
                    Filename should contain only letters, numbers and ._- chars
                """)
        
        self._state = self.STATE_INSTANCE_RECIEVED
        
    def save(self):
        """
            Saves object instance to a file
            
            >>> o = SomeObject()
            # do something
            >>> processor = ReusableObjectsProcessor(o)
            >>> processor.save()
            
            return filename
        """
        
        filename = self._filename 
        if not self._filename:
            filename = self._generate_filename()
            
        try:
            with open(
                os.path.join(
                    self._config['file_directory'], 
                    filename
                ) + '.pickle', 'wb'
            ) as f:
                pickle.dump(self._instance, f)
        except:
            self._state = self.STATE_ERROR
            return False
        
        self._filename = filename + '.pickle'            
        self._state = self.STATE_SAVED
        
        return self._filename
        
    def load(self):
        """
            Loads object instance and returns it
            
            >>> processor = ReusableObjectsProcessor(filename = "filename.pickle")
            >>> my_object = processor.load()
            
            return object
        """
        if self._filename is None:
            self._state = self.STATE_ERROR
            raise AttributeError("No filename specified")
        
        try:
            with open(
                os.path.join(
                    self._config['file_directory'], 
                    self._filename
                ), 'rb'
            ) as f:
                self._instance = pickle.load(f)
                self._state = self.STATE_LOADED
                return self._instance
        except:
            self._state = self.STATE_ERROR
            return False
    
    def _generate_filename(self):
        """
            Generates filename using hashlib sha256
            and built-in id() of self._instance
            
            return filename
        """
        
        str_for_hash = str(time.time()) + str(id(self._instance))
        self.tmp_filename = hashlib.sha256(str_for_hash.encode()).hexdigest()
        
        return self.tmp_filename