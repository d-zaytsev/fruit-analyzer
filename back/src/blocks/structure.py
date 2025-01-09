import cv2

from back.src.blocks.color import AbstractBlock


class StructureBlock(AbstractBlock):
    def __init__(self, cv_image):
        super().__init__(cv_image)
        self.__number_of_contours = self.__get_number_of_contours()

    def get_result(self):
        self.__set_detected_fruits()
        return super().get_result()

    def __set_detected_fruits(self):
        if self.__number_of_contours > 10:
            self.detected_fruits.Grapes = True
            self.detected_fruits.Pineapple = True

    def __get_number_of_contours(self):
        cv_image_gray = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(
            cv_image_gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            59,
            21,
        )
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        counter = 0
        for contour in contours:
            if cv2.contourArea(contour) > 200:
                counter += 1

        return counter