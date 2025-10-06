import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Webcam Setup
cap = cv2.VideoCapture(0)
time.sleep(2)

# Initialize center positions
center_x, center_y = None, None
calibrated = False  # Track whether the center has been set

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    h, w, _ = frame.shape

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            # Get the nose tip landmark (ID 1)
            nose = face_landmarks.landmark[1]
            nose_x, nose_y = int(nose.x * w), int(nose.y * h)

            # Define head movement thresholds
            x_threshold = 40  # Left-Right movement sensitivity
            y_threshold = 20  # Up-Down movement sensitivity

            # Detect Head Movements
            if nose_x < center_x - x_threshold:  # Head Moved Left
                pyautogui.press('left')
                print("MOVE LEFT")
                time.sleep(0.2)

            elif nose_x > center_x + x_threshold:  # Head Moved Right
                pyautogui.press('right')
                print("MOVE RIGHT")
                time.sleep(0.2)

            if nose_y < center_y - y_threshold:  # Head Moved Up
                pyautogui.press('up')
                print("JUMP")
                time.sleep(0.3)

            elif nose_y > center_y + y_threshold:  # Head Moved Down
                pyautogui.press('down')
                print("ROLL")
                time.sleep(0.3)

    # Show webcam feed
    cv2.imshow("🎮 Subway Surfers Head Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
