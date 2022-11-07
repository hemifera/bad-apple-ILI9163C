import imageio.v3 as iio
import os
os.mkdir("frames")
video_file = os.path.join(os.getcwd(), "bad_apple.mp4")
print("Loading...")
for idx, frame in enumerate(iio.imiter(video_file)):
    iio.imwrite(f"frames/{idx:05d}.bmp", frame)
print("All files generated successfully")
