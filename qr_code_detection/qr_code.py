import cv2
from pyzbar.pyzbar import decode

SUCCESS = 1
FAIL = 0


def draw_rectangle_on_QR(captured_frame_image):
    decoded_QR = decode(captured_frame_image)

    if decoded_QR:
        decode_result_type = decoded_QR[0].type
        assert decode_result_type == "QRCODE", f"Decoded image type is {decode_result_type} but should be QRCODE"

        # Get coordinates of QR code
        QR_rectangle = decoded_QR[0].rect
        height = QR_rectangle.height
        width = QR_rectangle.width
        left = QR_rectangle.left
        top = QR_rectangle.top

        # draw box around QR code image
        top_left_coords = [left, top]
        bottom_right_coords = [left + width, top + height]
        thickness = 5
        color = (0, 0, 255)
        cv2.rectangle(captured_frame_image, top_left_coords, bottom_right_coords, color, thickness)
        return SUCCESS
    return FAIL