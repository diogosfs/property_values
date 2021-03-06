# Author/source: Koosha Golmohammadi

# Convert a list of addresses from an input file to geocodes 

import sys

from geopy import GoogleV3

geolocator = GoogleV3()

input_file = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')

for line in input_file:
    print line
    address, (latitude, longitude) = geolocator.geocode(line, timeout=10)
    output_line = '%s,%s,%s\n' % (address, latitude, longitude)
    output_file.write(output_line)

input_file.close()
output_file.close()

#return 0
