import cv2
import numpy as np

def load_image(image_path):
    # Load image as grayscale to simplify comparison
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return None
    # Resize to a standard size to make comparison fair
    image = cv2.resize(image, (100, 100))  # Resizing both images to 100x100
    return image

def compare_images(image1_path, image2_path):
    # Load both images
    img1 = load_image(image1_path)
    img2 = load_image(image2_path)

    if img1 is None or img2 is None:
        return "Error: One or both images could not be loaded."

    # Calculate absolute difference between the images
    difference = cv2.absdiff(img1, img2)
    # Sum all pixel differences
    total_difference = np.sum(difference)
    
    if total_difference < 100000:  # Set a threshold for similarity
        return "It's a match!"
    else:
        return "No match found."

# Test with two images
image1_path = r'C:\Users\zua20\PycharmProjects\FaceRecognition\images\img4.jpg'
image2_path = r'C:\Users\zua20\PycharmProjects\FaceRecognition\N_images\img2.jpg'
result = compare_images(image1_path, image2_path)
print(result)
