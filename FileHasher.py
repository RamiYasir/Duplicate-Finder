import hashlib

BUFFER_SIZE = 1024

class FileHasher:
    def __init__(self, filepath):
        self.filepath = filepath


    # public
    def hash_file(self):
        with self.filepath.open(mode='rb') as file:
            hasher = hashlib.sha1()
            self.__update_hash(hasher, file)
            return hasher.hexdigest()


    # private
    def __update_hash(self, hasher, file):
        end_of_data = False
        
        while not end_of_data:
            data = file.read(BUFFER_SIZE)
            end_of_data = self.__is_file_ended(data)
            hasher.update(data)


    def __is_file_ended(self, data):
        return True if not data else False
