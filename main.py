# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


def main():


    Direc = "/home/travis/Downloads"
    print(f"Files in the directory: {Direc}")

    files = os.listdir(Direc)
    files = [f for f in files if os.path.isfile(Direc + '/' + f)]  # Filtering only the files.

    for x in files:

        if x == "config.txt":
            pass
        elif x.endswith(".txt"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/Text/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'Text' ")
        elif x.endswith(".stl" or ".step" or ".f3d"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/3D_Models/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into '3D Models' ")
        elif x.endswith(".zip" or ".rar" or ".7z" or ".tar.gz"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/Archives/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'Archives' ")
        elif x.endswith(".png" or ".jpg" or ".jepg" or ".webm"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/Images/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'Images' ")
        elif x.endswith(".mov" or ".mp4" or ".mkv"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/Videos/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'Videos' ")
        elif x.endswith(".mp3" or ".wav" or ".ogg"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/Music/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'Music' ")
        elif x.endswith(".exe" or ".appimage" or ".msi"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/Programs/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'Programs' ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 3 > 2:
        main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
