import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Add text using putText() for each planet
# Planet 1: Mercury
cv2.putText(img, "Mercury", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Planet 2: Venus
cv2.putText(img, "Venus", (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Planet 3: Earth
cv2.putText(img, "Earth", (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# ... Add putText() for other planets ...

# Display the image with added text
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)

# Close all windows
cv2.destroyAllWindows()
