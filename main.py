from pydub import AudioSegment
import os
import sys
import math

directory_path = sys.argv[1]
print("Searching: " + directory_path)

for filename in os.listdir(directory_path):
    fqdn = os.path.join(directory_path, filename)
    if os.path.isfile(fqdn) and filename.endswith('.wav'):
        print ("Checking file: " + filename)
        sound = AudioSegment.from_file(fqdn)
        loudness = sound.dBFS
        print (loudness)
        if math.isinf(loudness) and loudness < 0:
            print ("DELETING FILE NO SOUND")
            os.remove(fqdn)