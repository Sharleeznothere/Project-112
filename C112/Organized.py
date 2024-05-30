import os
import shutil

source = "/Users/sharleez/Downloads"
destination = "/Users/sharleez/Desktop"

list_of_files = os.listdir(source)
# print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    # print(name)
    # print(extension)
    if extension == "":
        continue
    if extension in [".png", ".jpg", ".jpeg", ".gif", ".jfif", ".webp"]:
        path1 = source + "/" + file_name
        path2 = destination + "/" + "Image_Files"
        path3 = destination + "/" + "Image_Files" + "/" + file_name

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)

    if extension in [".pdf",".docx",".txt", ".doc",".pptx", ".xlsx"]:
        path1 = source + "/" + file_name
        path2 = destination + "/" + "Doc_Files"
        path3 = destination + "/" + "Doc_Files" + "/" + file_name
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)