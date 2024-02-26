import cv2
import os

# Path to the input video
video_path = "videos\\video5.mp4"
output_folder = "vid5"  # Folder to save frames
frame_rate_reduction = 60  # Reduce frame rate by saving every 5th frame

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a VideoCapture object to read the video
cap = cv2.VideoCapture(video_path)

# Check if the video is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize frame counter
frame_count = 0
frame_index = 0

# Read the video frame by frame and save frames at reduced frame rate
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Skip frames according to frame rate reduction
    if frame_index % frame_rate_reduction != 0:
        frame_index += 1
        continue

    # Define the output file path for the current frame
    output_path = os.path.join(output_folder, f"frsddsssddfdsssgsamess4_{frame_count:04d}.jpg")  # Example: frames/frame_0000.jpg

    # Save the current frame as an image
    cv2.imwrite(output_path, frame)

    # Increment frame counter and frame index
    frame_count += 1
    frame_index += 1

# Release the VideoCapture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()

print(f"Frames extracted: {frame_count}")
