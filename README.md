# QR Code Scanner using ZED Camera

![QR Code Scanner Demo](https://github.com/saornek/ZED-QR-Code-Scanner/blob/main/demo.gif)

## Overview
This code utilizes the ZED Camera along with OpenCV and pyzbar libraries to create a real-time QR code scanner.

## Setup Instructions
1. **Install ZED SDK:**
   - Get the latest [ZED SDK](https://www.stereolabs.com/developers/release/) and [pyZED Package](https://www.stereolabs.com/docs/app-development/python/install/)

2. **Install Python Dependencies:**
   - Install the required Python libraries using pip:
     ```bash
     pip install pyzed pyzbar opencv-python
     ```

## Running the Code
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/saornek/ZED-QR-Code-Scanner
   ```
2. **Navigate to the Code Directory:**
   ```bash
   cd ZED-QR-Code-Scanner
   ```
3. **Run the Code:**
   ```bash
   python qr_scanner.py
   ```
4. **Usage:**
   - Once the code is running, point the ZED Camera towards QR codes to detect and decode them in real-time.
   - Press 'q' to exit the application.

## Notes
- Ensure the ZED Camera is connected and configured properly before running the code.
- Adjust any parameters or settings in the code as needed for your specific use case.

## Contributing
Contributions to this repository are welcome.  If you find any bugs or have suggestions for improvements, please feel-free to submit a pull request.

## Acknowledgments
Thank you to Stereolabs for providing the ZED SDK.

## Support
For any questions or support related to this code, you can contact me via the repository issues page.
