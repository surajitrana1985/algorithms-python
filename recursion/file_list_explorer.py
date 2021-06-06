import os

FILE_PATH = "../files/"


def main():
    input_type = get_input_from_user()
    if input_type != "":
        files_dict = {}
        if os.path.exists(FILE_PATH) and os.path.isdir(FILE_PATH):
            root_dir = os.listdir(FILE_PATH)
            list_files_in_directory(root_dir, files_dict)
        if input_type == "all":
            files_all = []
            for key in files_dict:
                files_all.extend(files_dict[key])
            print(files_all)
        else:
            print(files_dict[input_type])


def get_input_from_user():
    input_type = input("File extension to search (Type 'all' to list all file types or Press enter to skip): ")
    if input_type == "":
        return ""
    else:
        return input_type


def list_files_in_directory(file_path, files_dict):
    for file_name in file_path:
        if os.path.exists(FILE_PATH + file_name) and os.path.isdir(FILE_PATH + file_name):
            file_dir = os.listdir(FILE_PATH + file_name)
            list_files_in_directory(file_dir, files_dict)
        else:
            if file_name.find(".") > -1:
                file_extn = file_name.split(".")[1]
                if file_extn not in files_dict:
                    files_dict[file_extn] = [file_name]
                else:
                    files_dict[file_extn].append(file_name)


if __name__ == "__main__":
    main()
