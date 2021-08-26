import os

config = {
    "default" : {
        "save_type": "file",
        "file_directory": os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            'reusable_objects_tmp'
        )
    }
}