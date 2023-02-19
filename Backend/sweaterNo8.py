knitGauge=[None,None] #stitches for [width, height] in 4" x 4"
import logging #Todo: set up logging file output
from sweater import sweater
import measurements

class sweaterNo8(sweater):

    collarType="Turtle";
    sleeveLength="Full"
    bodyEase=[35,13.77]    #35 cm, or 13.77 inches
    
    originalGauge=[22,28] #[width in stitches, height in row

    def __init__(self, measurements, gauge):
        # logging.info(f'"Generating Sweater No.8 in size {size} with gauge {gauge[0]} x {gauge[1]}"')
        print(f'"Generating Sweater No.8 with gauge {gauge[0]} x {gauge[1]} in 4" x 4" "')
        # if size not in self.validSizes:
        #     return -1
        super().__init__(self,measurements,gauge)
     