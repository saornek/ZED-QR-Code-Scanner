"""
Author: saornek
Date: 02/17/2024
Purpose: QR Code Scanner with ZED 2i Camera
"""

import cv2
from pyzbar.pyzbar import decode
import pyzed.sl as sl

def initialize_zed_camera():
    # Create a ZED camera object
    zed = sl.Camera()

    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE

    # Open the camera
    if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
        print("Failed to open the camera")
        return None

    return zed

def scan_qr_code(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    qr_codes = decode(gray)

    # Process the detected QR codes
    for qr_code in qr_codes:
        data = qr_code.data.decode("utf-8")
        print("QR Code Data:", data)

        # Extract bounding box coordinates
        (x, y, w, h) = qr_code.rect

        # Draw bounding box and label around the QR code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

def main():
    # Initialize ZED camera
    zed = initialize_zed_camera()
    if zed is None:
        return

    try:
        while True:
            # Capture a frame from the ZED Camera
            if zed.grab() == sl.ERROR_CODE.SUCCESS:
                left_image = sl.Mat()
                zed.retrieve_image(left_image, sl.VIEW.LEFT)

                # Convert the ZED image to a format compatible with OpenCV
                frame = left_image.get_data()

                # Call the QR code scanning function
                scan_qr_code(frame)

                cv2.imshow("ZED Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    finally:
        # Release resources
        zed.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
