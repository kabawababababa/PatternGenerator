knitGauge=[None,None] #stitches for [width, height] in 4" x 4"
import logging #Todo: set up logging file output
import sweater

class sweaterNo8:
    # Use a breakpoint in the code line below to debug your script.

    class Neckline(sweater.neckline):
        print("I'm not done yet")

    collarType="Turtle";
    sleeveLength="Full"
    bodyEase=[35,13.77]    #35 cm, or 13.77 inches
    validSizes=['XS','S','M','L','XL']

    originalGauge=[22,28] #[width in stitches, height in rows
    newGauge=[None,None]
    size=None

    def __init__(self, size, gauge):
        logging.info(f'"Generating Sweater No.8 in size {size} with gauge {gauge[0]} x {gauge[1]}"')
        # if size not in self.validSizes:
        #     return -1

        self.set_new_gauge(gauge)
        self.set_size(size)

    def set_size(self,size):
        if size not in self.validSizes:
            raise ValueError(f'"Your entered size should be one of {self.validSizes}')
        self.size = size
        sizeIndex = self.validSizes.index(size)
        

    def get_size(self):
        return self.size

    def set_new_gauge(self,knitGauge):
        if not all(isinstance(gauge, int) for gauge in knitGauge):
            raise ValueError(f'"Your gauge must use integers as values for [stitch width, row height]. Value: {knitGauge} is not valid"')
        elif len(knitGauge) != 2:
            raise ValueError(f'"Your gauge must use only two values, a width and a height"')
        elif knitGauge[0] == 0 or knitGauge[1] == 0:
            raise ValueError(f'"Your gauge must use non zero values"')
        self.newGauge=knitGauge
        return 0

    def get_new_gauge(self):
        return self.newGauge
