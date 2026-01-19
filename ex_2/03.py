import matplotlib.pyplot as plt

img = create_gradient_image(300, 300)

img_np = brighten(img, 80, "np")
img_cv = brighten(img, 80, "cv2")

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("np.add")
plt.imshow(img_np, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("cv2.add")
plt.imshow(img_cv, cmap='gray')
plt.axis('off')

plt.show()
