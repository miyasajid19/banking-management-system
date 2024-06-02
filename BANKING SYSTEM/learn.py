import cv2

def scan_qr_code():
    
    cap = cv2.VideoCapture(0)

    # Create a QR code detector
    detector = cv2.QRCodeDetector()

    while True:
        _, frame = cap.read()

        # Detect QR codes
        data, bbox, _ = detector.detectAndDecode(frame)

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Check if a QR code is detected
        if bbox is not None:
            # Print the data contained in the QR code
            print('Data:', data)
            if data !='':
                break

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
