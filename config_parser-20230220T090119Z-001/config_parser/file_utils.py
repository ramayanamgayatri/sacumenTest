'''
utility functions for working with files. 
e.g. reading/writing files
'''
def get_file_extension(file_path):
    return '.' + file_path.split('.')[-1]
