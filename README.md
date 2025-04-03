# Real-Time Object Detection with Camera Feed

This project demonstrates real-time object detection from a camera feed using the `RFDETR` model for object detection. The model processes frames captured from a webcam and displays the results with bounding boxes and labels overlaid on the video feed.

## Features
- Real-time object detection on webcam feed.
- Bounding boxes and labels are annotated on the frames.
- Multi-threading to handle frame capture and processing concurrently for improved performance.
- Resizes frames to optimize detection speed without sacrificing much accuracy.

## Requirements

Before running the project, you need to install the necessary dependencies.

### Python Libraries:
- `opencv-python` (OpenCV)
- `supervision`
- `rfdetr` (Custom or any available implementation of the RFDETR model)

### Installation

You can install the required libraries by running:

```bash
pip install opencv-python supervision rfdetr
```

Alternatively, you can install the libraries manually by adding them to a `requirements.txt` file:

```
opencv-python
supervision
rfdetr
```

Then, install them using:

```bash
pip install -r requirements.txt
```

## Usage

### Running the script

To run the real-time object detection script with your webcam, execute the following Python script:

```bash
python object_detection_camera.py
```

### How it works:
1. **Capture Frames**: The program captures frames from your default webcam (you can change the index for different cameras).
2. **Process Frames**: The frames are processed by the `RFDETR` model for object detection. The detected objects are labeled and displayed on the video feed.
3. **Display Video Feed**: The camera feed is displayed with bounding boxes and labels for the detected objects. 
4. **Exit**: Press the **`q`** key to exit the program.

### Code Breakdown:

1. **Capture Frames**: 
   - A separate thread (`capture_frames()`) continuously reads frames from the webcam.
   - Frames are resized to `640x480` to optimize processing speed.

2. **Processing Frames**: 
   - Another thread (`process_frames()`) runs in parallel, which takes frames from the capture thread and performs object detection on them.
   - The object detection results (labels and bounding boxes) are overlaid on the frames.
   
3. **Display the Feed**: 
   - The annotated frames are displayed in a real-time window using `cv2.imshow()`.

4. **Exit the Program**: 
   - The program can be exited by pressing the `q` key.

## Example Output

Upon running the script, a video feed from your camera will be displayed. Detected objects will be annotated with bounding boxes and their class labels. The following example output might show:

- `person 0.85`
- `dog 0.91`

The confidence score is displayed alongside the object label.

## Troubleshooting

### Camera not opening
- Make sure your webcam is properly connected to the computer.
- If you're using an external camera, try changing the argument `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or `cv2.VideoCapture(2)`.

### Slow performance
- Reduce the frame resolution by resizing it in the script (`cv2.resize(captured_frame, (640, 480))`).
- Use a GPU for inference if supported, which will significantly speed up the detection.

## Contributing

If you'd like to contribute to this project:
1. Fork this repository.
2. Make changes in a separate branch.
3. Submit a pull request for review.

## License

This project is licensed under the MIT License.