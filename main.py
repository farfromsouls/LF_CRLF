import os
import re


def filedata(dir, point):
    try:
        with open(dir, "rb") as file:
            content = file.read()
        if point == 1:
            content = re.sub(b'(?<!\r)\n', b'\r\n', content)
        else:
            content = content.replace(b'\r\n', b'\n')
        with open(dir, "wb") as file:
            file.write(content)
    except Exception as e:
        print(f"Error processing file {dir}: {str(e)}")

def dir_recursion(dir_path, point):
    try:
        dirlist = os.listdir(dir_path)
    except PermissionError:
        print(f"No access to folder: {dir_path}")
        return
        
    for file in dirlist:
        full_path = os.path.join(dir_path, file)
        if os.path.isdir(full_path):
            dir_recursion(full_path, point)
        else:
            if file.endswith(('.txt', '.py', '.html', '.css', 
                              '.js', '.json', '.xml', '.md')):
                filedata(full_path, point)
            
def main(dir_path, point):
    abs_path = os.path.abspath(dir_path)
    print(f"Starting folder traversal: {abs_path}")
    dir_recursion(abs_path, point)

if __name__ == "__main__":
    localdir = os.listdir(".")
    folders = []

    print("1) LF -> CRLF\n2) CRLF -> LF")
    try:
        point = int(input())
        if point not in [1, 2]:
            raise ValueError("Invalid choice")
    except:
        print("Invalid input")
        exit()

    print("List of folders:")
    for i, item in enumerate(localdir):
        if os.path.isdir(item):
            folders.append(item)
            print(f"{len(folders)-1}) {item}")

    if not folders:
        print("No folders in current directory")
        exit()

    try:
        workdir_n = int(input("Select folder number: "))
        if workdir_n < 0 or workdir_n >= len(folders):
            print("Invalid folder number")
            exit()
           
        workdir = folders[workdir_n]
        main(workdir, point)
        print("Success!")

    except ValueError:
        print("Please enter a number")