import os


def login(username, password):
    """
    user login

    :param username: username
    :param password: password
    :return:
    """
    if username == 'admin' and password == '123456':
        return True
    return False


def upload(file):
    """
    upload file

    :param file:
    :return:
    """
    files_folder = 'files'
    os.makedirs(files_folder, exist_ok=True)
    file_name = os.path.split(file.raw_filename)[1]
    path = os.path.join(files_folder, file_name)

    file.save(path, True)
    return 'File %s uploaded successfully!' % file_name

