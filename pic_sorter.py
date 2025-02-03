import os,hashlib,argparse,subprocess,sys

parser = argparse.ArgumentParser(description="Program for Automatically Copying and Sorting Photos")
parser.add_argument("-n","--names",help="Enter a list of family names. Ex: -n John,Sarah,Christopher",required=True)
parser.add_argument("-f","--file",help="Enter the file name. Ex: -f file.jpg",required=True)
parser.add_argument("-a","--addnames",action="store_true", help="Set flag to ignore <file_name.ext.copied> file",required=False)

args = vars(parser.parse_args())

def get_name_list(arguments: dict) -> list:
    new_list = arguments["names"].split(",")
    return new_list

def exists_already(abs_path: str) -> bool:
    if os.path.exists(abs_path):
        return True
    else:
        return False

def get_ab_paths(family_name: str, file_name: str) -> str:
    cwd = os.getcwd()
    path = os.path.join(cwd, family_name, file_name)
    return path

def get_file(file_name: str) -> bytes:
    file_data =b""
    with open(file_name,'rb') as temp:
        file_data += temp.read()
    return file_data

def get_unique_names(file_data: str,family_name: str) -> str:
    sha256_hash = hashlib.sha256(file_data).hexdigest()
    new_name = f"{family_name}-{sha256_hash[:10]}"
    return new_name

def copy_pics(path:str, file_data: bytes)-> bool:
    try:
        with open(path,'wb') as temp:
            temp.write(file_data)
        return True
    except:
        print(f'[+] Error writing: {path}')
        return False

def make_directory(family_name: str) -> bool:
    cwd = os.getcwd()
    joined_path = os.path.join(cwd, family_name)
    try:
        subprocess.run(["mkdir", joined_path], capture_output=False, text=False)
        return True
    except:
        return False

def mark_copied(file_name: str) -> None:
    try:
        subprocess.run(["cp", file_name, f"{file_name}.copied"], capture_output=False, text=False)
    except:
        print(f"Error copying file: {file_name}")

def already_copied(file_name: str) -> bool:
    cwd = os.getcwd()
    path = os.path.join(cwd, f"{file_name}.copied")
    if os.path.exists(path):
        return True
    else:
        return False

def main() -> None:

    successful_copies = []
    already_exits = []

    # Checks if the file exists
    if not exists_already(args["file"]):
        print(f"[+] {args['file']} does not exist.\n[+] Exiting...")
        sys.exit()

    # Read File Data
    f_data = get_file(args["file"])

    # Checks if file is already copied && If -a flag is not set; If so, exits
    if already_copied(f'{args["file"]}') and not args["addnames"]:
        print(f"[+] File {args['file']} is already copied")
        print(f"----{args['file']}")
        print(f"----{args['file']}.copied")
        sys.exit()

    # Gathers Names
    name_list = get_name_list(args)

    print(f"[+] Beginning copying process for file: {args['file']}")

    for name in name_list:

        # Check if family member directory exists; If not, then create the directory
        if not exists_already(name):
            make_directory(name)

        # Get unique file name && absolute path
        unique_file_name = get_unique_names(f_data,name)
        ab_path = get_ab_paths(name, unique_file_name)

        # Check if file already exists; If so, append to already_exist list; If not, then copy the file
        if exists_already(ab_path):
            already_exits.append(ab_path)
        else:
            status = copy_pics(ab_path, f_data)
        
            # Checks if the copy was successful; If so, append it to success list
            if status:
                successful_copies.append(ab_path)

    # Make "<file_name.ext>.copied" to avoid redundancy
    mark_copied(args["file"])
    
    print(f'\n[+] Successfully copied the following files:')
    for success in successful_copies:
        print(f"----{success}")
    
    print("\n[+] The following files already exist:")
    for exists in already_exits:
        print(f"----{exists}")
    
    print('\n[+] Completed!')


if __name__ == "__main__":
    main()
