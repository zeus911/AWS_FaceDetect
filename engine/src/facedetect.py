"""Main file for the engine routine.

Expected to run on a AWS EC2 instance.
Exposes a FaceDetect class which expects an image as argument.
"""

import cv2


class FaceDetect:
    """Takes image as argument. Provides support for face detections."""

    def __init__(self, image=None):
        """Construct with only image as attribute."""
        self.image = image

    def isvalid(self):
        """Check if attribute has been set."""
        try:
            if self.image.all() is not None:
                return True
            else:
                return False
        except AttributeError:
            return False

    def convertgrey(self):
        """Convert image to grayscale."""
        if self.isvalid():
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        else:
            print("Image undefined.")

    def getimage(self):
        """Return the image."""
        return self.image

    def setimage(self, img):
        """Set the new image."""
        self.image = img
