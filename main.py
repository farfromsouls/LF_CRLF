import os  
  
def filedata(dir):  
    file = open(dir, "r+", encoding="utf-8")  
    replaced = file.read().replace("\n", "\r\n", -1)  
    file.write(replaced)  

def dir_recursion(dir_path):  
    try:  
        dirlist = os.listdir(dir_path)  
    except PermissionError:  
        print(f"No access to folder: {dir_path}")  
        return  
        
    for file in dirlist:  
        full_path = os.path.join(dir_path, file)  
        if os.path.isdir(full_path):  
            dir_recursion(full_path)  
        else:  
            filedata(full_path)  
            
def main(dir_path):  
    abs_path = os.path.abspath(dir_path)  
    print(f"Starting folder traversal: {abs_path}")  
    dir_recursion(abs_path)  

if __name__ == "__main__":  
    localdir = os.listdir(".")  
    folders = []  
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
        main(workdir)  
    except ValueError:  
        print("Please enter a number")
