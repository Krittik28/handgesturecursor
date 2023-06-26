import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand model
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Set up PyAutoGUI screen size
screen_size = pyautogui.size()

# Initialize PyAutoGUI mouse control
mouse = pyautogui

prev_x, prev_y = 0, 0

# Set up MediaPipe Hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the hand detection
    results = hands.process(image_rgb)

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of index finger tip and thumb tip
            index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            x = int(index_finger_landmark.x * image.shape[1])
            y = int(index_finger_landmark.y * image.shape[0])

            # Check if the hand is in a closed fist gesture
            if thumb_tip_landmark.x < index_finger_landmark.x:
                # Perform a click action
                mouse.click(x, y)
            else:
                # Move the cursor
                delta_x = x - prev_x
                delta_y = y - prev_y
                mouse.moveRel(delta_x, delta_y)

                # Update previous cursor position
            prev_x, prev_y = x, y

    # Show the image with mouse cursor control
    cv2.imshow('MediaPipe Hands', image)

    # Exit when 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
