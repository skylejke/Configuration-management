import zipfile


def pwd(cur_dir):
    print(cur_dir)


def ls(archive, current_dir):
    file_zip = zipfile.ZipFile(archive, 'r')
    path = zipfile.Path(file_zip, current_dir)
    for paths in path.iterdir():
        print(str(paths)[len(archive) + len(current_dir) + 1:])


def cd(current_dir, command, archive_name_len):
    directory = command[3:]
    if directory == "..":
        current_dir = current_dir[:-1]
        while len(current_dir) > archive_name_len and current_dir[len(current_dir) - 1] != '/':
            current_dir = current_dir[:-1]
        if len(current_dir) >= archive_name_len:
            return current_dir
        else:
            return current_dir + '/'

    elif current_dir in directory:
        return directory + '/'

    else:
        return current_dir + directory + '/'


def cat(command, current_dir, archive):
    file = command[4:]
    file_zip = zipfile.ZipFile(archive, 'r')
    path = zipfile.Path(file_zip, current_dir + file)
    print(path.read_text())


def vshell(archive):
    archive_name_len = len(archive[:-4])
    current_dir = archive[:-4] + '/'

    while True:
        print(current_dir)
        command = input()

        if command == "pwd":
            pwd(current_dir)

        elif command == "ls":
            ls(archive, current_dir)

        elif command[0] == "c" and command[1] == "d":
            current_dir = cd(current_dir, command, archive_name_len)

        elif command[0] == "c" and command[1] == "a" and command[2] == "t":
            cat(command, current_dir, archive)

        elif command == "exit":
            break


def main():
    print("Enter archive name:")
    archive = input()
    vshell(archive)


if __name__ == "__main__":
    main()
