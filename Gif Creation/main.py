import imageio
filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('movie.gif', images, 'GIF', duration=1)