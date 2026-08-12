import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

original = img.copy()

while True:

    display = img.copy()

    cv2.putText(display,
                "R-Red G-Green B-Blue Y-Yellow O-Original ESC-Exit",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2)

    cv2.imshow("Color Changer", display)

    key = cv2.waitKey(0) & 0xFF

    if key == 27:      # ESC
        break

    elif key == ord('r'):
        img = original.copy()
        img[:, :, 0] = 0   # Remove Blue
        img[:, :, 1] = 0   # Remove Green

    elif key == ord('g'):
        img = original.copy()
        img[:, :, 0] = 0   # Remove Blue
        img[:, :, 2] = 0   # Remove Red

    elif key == ord('b'):
        img = original.copy()
        img[:, :, 1] = 0   # Remove Green
        img[:, :, 2] = 0   # Remove Red

    elif key == ord('y'):
        img = original.copy()
        img[:, :, 0] = 0   # Remove Blue

    elif key == ord('o'):
        img = original.copy()

cv2.destroyAllWindows()