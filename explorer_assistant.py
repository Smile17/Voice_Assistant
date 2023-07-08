import os

program_pathes = {
    'pycharm': r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\bin\pycharm64.exe",
    'charm': r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\bin\pycharm64.exe",
    'download': r'C:\Users\kam\Downloads'
}

class ExplorerAssistant:
    'Open X'
    def open_program(self, query):
        print(query)
        os.startfile(program_pathes[query])


