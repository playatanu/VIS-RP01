# sudo apt-get install flite

import os
import shlex


def speak(text, voice="slt"):

    escaped_text = shlex.quote(text)
    print(text)

    os.system(f"flite -voice {voice} -t {escaped_text}")
