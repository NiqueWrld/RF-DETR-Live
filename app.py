import cv2
import supervision as sv
from rfdetr import RFDETRBase
from rfdetr.util.coco_classes import COCO_CLASSES
import threading

model = RFDETRBase()

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Initialize annotators
box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# Shared variable to store the frame
frame_lock = threading.Lock()
frame = None

def capture_frames():
    global frame
    while True:
        success, captured_frame = cap.read()
        if not success:
            print("Failed to capture frame from camera.")
            break
        # Resize the frame to speed up processing
        captured_frame = cv2.resize(captured_frame, (640, 480))  # Resize to 640x480 or any suitable resolution
        with frame_lock:
            frame = captured_frame

def process_frames():
    while True:
        with frame_lock:
            if frame is None:
                continue
            # Run object detection
            detections = model.predict(frame, threshold=0.5)

            # Generate labels
            labels = [
                f"{COCO_CLASSES[class_id]} {confidence:.2f}"
                for class_id, confidence in zip(detections.class_id, detections.confidence)
            ]

            # Annotate frame
            annotated_frame = frame.copy()
            annotated_frame = box_annotator.annotate(annotated_frame, detections)
            annotated_frame = label_annotator.annotate(annotated_frame, detections, labels)

            # Display the frame
            cv2.imshow("Camera Feed", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Start the capture and processing threads
capture_thread = threading.Thread(target=capture_frames, daemon=True)
process_thread = threading.Thread(target=process_frames, daemon=True)

capture_thread.start()
process_thread.start()

# Wait for the threads to finish (if they ever do)
capture_thread.join()
process_thread.join()

cap.release()
cv2.destroyAllWindows()
