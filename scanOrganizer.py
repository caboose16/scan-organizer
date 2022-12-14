import os
import shutil

# debugging options
dry_run = False
verbose = True

file_path = os.path.realpath(__file__)
file_dir = os.path.dirname(file_path)
paths_by_keyword = {
    "accord2016": "../car/2016accord",
    "paystub": "../work/payStub",
    "purchasedgoods": "../purchasedGoods",

    # dogs
    "chato": "../dogs/Chato",
    "coco": "../dogs/Coco",
    "dulce": "../dogs/Dulce",
    "juanito": "../dogs/Juanito",
    "rubi": "../dogs/Rubi",
}

def get_file_tuple(file_name):
    keyword = file_name.split(" ")[0]
    file_type = keyword.lower()
    file_type = file_type if file_type in paths_by_keyword else "unknown"
    return (file_type, file_name)

def move_file(file_tuple):
    file_keyword = file_tuple[0] # the keyword to use for the dictionary
    file_name = file_tuple[1] # name of file, no path

    source = os.path.join(file_dir, file_name)
    source = os.path.normpath(source)
    destination = os.path.join(file_dir, paths_by_keyword[file_keyword])
    destination = os.path.normpath(destination)

    message = ""
    if dry_run:
        message += "Dry Run: "
    else:
        # ToDo: handle destination file already exists
        shutil.move(source, destination)
    
    message += f'Moved "{source}" to "{destination}"'
    print(message)
    exit

def main():
    files = os.listdir(file_dir)
    filter(lambda path: path.endwith(".pdf"), files)

    # get file tuples for unknown and known types
    file_tuples = [get_file_tuple(f) for f in files]
    unknown_file_tuples = []
    known_file_tuples = []
    for file in file_tuples:
        if file[0] == "unknown":
            unknown_file_tuples.append(file)
        else:
            known_file_tuples.append(file)
    if verbose:
        print(f"Known file type count: {len(known_file_tuples)}")
        print(f"Unknown file type count:  {len(unknown_file_tuples)}")
        print()

    # move files
    for tuple in known_file_tuples:
        move_file(tuple)
    print()

    # print files that weren't moved due to unknown type
    unknown_file_names = [t[1] for t in unknown_file_tuples]
    print("Found unkown type for files:")
    for f in unknown_file_names:
        print(f"  {f}")

if __name__=="__main__":
    main()
    