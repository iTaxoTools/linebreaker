import logging
import zipfile
import argparse
import re
import sys
import warnings

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path, ext):
        super().__init__()
        self.path = path
        self.ext= ext


    def __repr__(self):
        return "name of file is " +"  "+ str(os.path.split(self.path)[-1]) + " and now linebreaks "+  "changed to" + " " + str(self.ext)


    def readlines(self):
        if not zipfile.is_zipfile(self.path) and os.path.isfile(self.path):
            if self.ext == "unix":
                with open(self.path, mode= "r") as f:

                    yield from f
            else:
                with open(self.path, mode= "r", newline= "") as f:

                    yield from f
        else:
            pass


    def readline(self):
        if not zipfile.is_zipfile(self.path) and os.path.isfile(self.path):
            return open(self.path, mode= "r", newline= "").readline()


    def write(self):
        folder, file= os.path.split(self.path)
        return os.path.join(folder, self.ext + "lb_"+ file)


class Worker(object):
    def __init__(self, input_data, input2, loc):
        self.input_data = input_data
        self.result = None
        self.input2 = input2
        self.loc= loc

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


platform= {"windows": "\r\n", "mac": "\r", "unix": "\n"}
io5= re.compile(r"\n", re.M)


class LineWorker(Worker):
    global platform

    def map(self):
        count= None
        line= self.input_data.readline()
        input2= self.input2
        try:
            if "\r\n" in str(line):
                count= sum(1 for x in self.input_data.readlines())
                ending= "windows"
            elif "\n" in str(line):
                count= sum(1 for x in self.input_data.readlines())
                ending= "unix"
            elif "\r" in str(line):
                count= sum(1 for x in self.input_data.readlines())
                ending= "mac"
            else:
                print("unknown line ending")


            logging.basicConfig(format='Date-Time : %(asctime)s - %(message)s', \
                                level = logging.INFO, filename = self.loc, filemode = 'w+')

            logging.info('The {} and had {} lines with {} linebreaks'.format(repr(self.input_data), count, ending))

            line= self.input_data.readline()
            input2= self.input2
            if ((line[-2:] != "\r\n") and (input2 == "windows")):
                translation = {13: 10}
                data= (data.translate(translation) for data in self.input_data.readlines())
                data = (io5.sub(x, "\r\n") for x in data)
                self.result= (x.lstrip("\r") for x in data)
                write= self.input_data.write()
                with open(write, mode= "wb") as f:
                    for x in self.result:
                        f.write(x.encode("utf-8"))


            elif ((line[-2:] == "\r\n") and (input2 == "mac")):
                self.result = (data.replace("\r\n", platform[input2]) for data in self.input_data.readlines())
                write= self.input_data.write()
                with open(write, mode= "wb") as f:
                    for x in self.result:
                        f.write(x.encode("utf-8"))

            elif ((line[-1:] == "\n") and (input2 == "mac")):
                translation2= {10: 13}
                self.result= (data.translate(translation2) for data in self.input_data.readlines())
                write= self.input_data.write()
                with open(write, mode= "wb") as f:
                    for x in self.result:
                        f.write(x.encode("utf-8"))

            elif (((line[-1:] != "\n") or (line[-2:] == "\r\n")) and (input2 == "unix")):
                self.result= (data for data in self.input_data.readlines())
                write= self.input_data.write()
                with open(write, mode= "wb") as f:
                    for x in self.result:
                        f.write(x.encode("utf-8"))

            else:
                pass

        except Exception as e:
            pass

import os
import zipfile
import shutil

def generate_inputs(data_dir, ext):
    try:
        for name in os.listdir(data_dir):
            if zipfile.is_zipfile(name):
                path = os.path.join(data_dir, name)
                with zipfile.ZipFile(name, 'r') as zip:
                    zip.extractall()
                file_1= name.split(".")[0]
                file_names = os.listdir(file_1)
                for file_name in file_names:
                    shutil.move(os.path.join(file_1, file_name), data_dir)

        for name in os.listdir(data_dir):
            if not zipfile.is_zipfile(name):
                yield PathInputData(os.path.join(data_dir, name), ext)

    except Exception as e:
        print(e)
        warnings.warn(f"The error {e} has been found")


def create_workers(input_list, input2, loc):
    try:
        workers = []
        for input_data in input_list:
            workers.append(LineWorker(input_data, input2, loc))
        return workers

    except Exception as e:
        print(e)
        warnings.warn(f"The error {e} has been found")


from threading import Thread

def execute(workers):
    try:
        threads = [Thread(target=w.map) for w in workers]
        for thread in threads: thread.start()
        for thread in threads: thread.join()

    except Exception as e:
        print(e)
        warnings.warn(f"The error {e} has been found")


def transform(data_dir, input2, loc= None):
    try:
        inputs = generate_inputs(data_dir, input2)
        if loc is None:
            loc= os.path.join(data_dir, "file.txt")
        workers = create_workers(inputs, input2, loc)
        return execute(workers)

    except Exception as e:
        print(e)
        warnings.warn(f"The error {e} has been found")


if __name__=="__main__":
        # configure the argument parser
    parser = argparse.ArgumentParser(
        description="Converts linebreaks for different os files with the user specified ones.The converted files generated in the same input directory named with prefix of output format. The original file remains unchanged.")

    parser.add_argument(
        '--cmd', help="activates the command-line interface", action='store_true')
    parser.add_argument("f",  action='store', help="the input directory path containing files to be converted")
    parser.add_argument('format', action='store', choices=['unix', 'windows', 'mac'], help="linebreak format of output files")
    parser.add_argument("-l", action = "store", help="the output log file path")

    args = parser.parse_args()

    try:
        with warnings.catch_warnings(record=True) as warns:
            transform(args.f, args.format, args.l)
            for w in warns:
                print(w.message)

    except FileNotFoundError as ex:
        sys.exit(ex)
