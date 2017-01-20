#--------------------------------------------------------------------------------------------------
#   Auth : Dave Chalco 
#   Date : 01-19-2017
#   Desc : A script to play around with ALPR and RaspiCam integration - 0xDC
#   Notes: Skeleton code taken from: doc.openalpr.com/bindings.html
#          See README.md for operation
#--------------------------------------------------------------------------------------------------
from openalpr import Alpr

alpr = Alpr("us", "./config/openalpr.conf", "./runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("md")

results = alpr.recognize_file("/home/pi/Downloads/Test_GoogleCar.jpg")

i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
alpr.unload()
