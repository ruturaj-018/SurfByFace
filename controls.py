import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start Webcam
cap = cv2.VideoCapture(0)
time.sleep(3)  # Allow webcam to warm up

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    h, w, _ = frame.shape  # Get frame width and height

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get fingertip positions
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_finger = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_finger = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Get reference points for detecting hand gestures
            index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            middle_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

            # Gesture 1: Open Palm → Jump
            if (
                index_finger.y < index_mcp.y and
                middle_finger.y < middle_mcp.y and
                ring_finger.y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y and
                pinky_finger.y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y and
                thumb.y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
            ):
                pyautogui.press('up')  # Jump
                print("JUMP")
                time.sleep(0.3)

            # Gesture 2: Fist (All Fingers Down) → Roll
            elif (
                index_finger.y > index_mcp.y and
                middle_finger.y > middle_mcp.y and
                ring_finger.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y and
                pinky_finger.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
            ):
                pyautogui.press('down')  # Roll
                print("ROLL")
                time.sleep(0.3)

            # Gesture 3: 1 Finger (Index Only) → Move Left
            elif (
                index_finger.y < index_mcp.y and
                middle_finger.y > middle_mcp.y and
                ring_finger.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y and
                pinky_finger.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
            ):
                pyautogui.press('left')  # Move Left
                print("MOVE LEFT")
                time.sleep(0.2)

            # Gesture 4: 2 Fingers (Index & Middle) → Move Right
            elif (
                index_finger.y < index_mcp.y and
                middle_finger.y < middle_mcp.y and
                ring_finger.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y and
                pinky_finger.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
            ):
                pyautogui.press('right')  # Move Right
                print("MOVE RIGHT")
                time.sleep(0.2)

    # Show Webcam Feed
    cv2.imshow("🎮 Subway Surfers Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
