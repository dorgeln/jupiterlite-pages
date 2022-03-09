import shutil
import os

def task_build():
    """build"""
    def copyfiles (output,copyfiles):
        if not os.path.exists(output):
            os.mkdir(output)

        for f in copyfiles: 
            if os.path.exists(f):
                shutil.copyfile(f, os.path.join("_output",f))
 
    return {
        'actions': ['jupyter lite build',(copyfiles)],
        'params':[
                {
                    'name':'output',
                    'short':'o',
                    'default':'_output'
                },
                {
                    'name':'copyfiles',
                    'short':'v',
                    'default':["CNAME",".nojekyll"]
                }
            ],
        }