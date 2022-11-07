from PIL import Image
import os
os.mkdir("reduced_frames")
frames_folder = os.path.join(os.getcwd(), "frames")
files_list = os.listdir(frames_folder)
files_list.sort()
print("Loading!!")
for file_index, file_name in enumerate(files_list):
    current_file = os.path.join(frames_folder, file_name)
    with Image.open (current_file) as im:
        resized = im.resize((120,90))
    reduced_frame_file = os.path.join(os.getcwd(), "reduced_frames", file_name)
    resized.save(reduced_frame_file)
    print(f"{file_name} reduced and saved in reduced_frames!")

print("Finished!")