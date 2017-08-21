""" recursive zip expander """
import os
import sys
import zipfile
import glob

expanddir = ""

def unzip(filename,dirname):
    """ unzip file """
    try:
        with zipfile.ZipFile(filename, "r") as zf:
            zf.extractall(path=expanddir)
            print(expanddir)
    except zipfile.BadZipFile:
        print("BadZipFile:"+ filename)
    delete_zip(filename)


def delete_zip(zip_file):
    """ delete file """
    os.remove(zip_file)


def walk_in_dir(dir_path):
    """ explore directory """
    for filename in glob.glob(os.path.join(dir_path, "*.zip")):
        unzip(filename=os.path.join(dir_path,filename),dirname=dir_path)

    for dirname in (d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))):
        walk_in_dir(os.path.join(dir_path, dirname))


if __name__ == "__main__":
    ARGS = sys.argv
    try:
        if(os.path.isdir(ARGS[1])):
            expanddir = ARGS[1]
            walk_in_dir(ARGS[1])
        """
        else: 
            unzip(os.path.join(ARGS[1]))
            name, _ = os.path.splitext(ARGS[1])
            if (os.path.isdir(name)):
                walk_in_dir(name)
        """
    except IndexError:
        print('IndexError: Usage "python %s ZIPFILE_NAME" or "python %s DIR_NAME"' % (ARGS[0], ARGS[0]))
    except IOError:
        print('IOError: Couldn\'t open "%s"' % ARGS[1])
