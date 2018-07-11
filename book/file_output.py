# coding = utf-8
import os

'''
文件类
'''


class FileOutPut(object):
    def __init__(self):
        self.data = {}

    def file_output(self, data, dir_name, file_name, chapter_name):
        file_path = r'../novelfile/%s' % dir_name

        if os.path.exists(file_path) is False:
            os.makedirs(file_path)
        try:
            filehandle = open(file_path + chapter_name + ".txt", "wb")
            filehandle.write(data.encode("utf-8"))
            filehandle.close()
        except Exception as e:
            print("我是file异常", e)

        return file_path + chapter_name + ".txt"
