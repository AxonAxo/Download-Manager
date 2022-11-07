# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os


def main():
    print("Python Program to print list the files in a directory.")

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
        elif x.endswith(".stl"):
            direcwfile = Direc + "/" + x
            dest = Direc + "/STL/" + x
            os.rename(direcwfile, dest)
            print(f"Moved {x} into 'STL' ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
