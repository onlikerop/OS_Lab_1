import os
import json
import random
from sys import platform
import xml.etree.ElementTree as ET
import zipfile

import psutil as psutil

if platform == "win32":
    def printDisksInfo():
        print("Drives in system: ", end='')
        for disk in psutil.disk_partitions():
            print(f"{disk[0][0]}, ", end='')
        print('\b\b\n')
        for disk in psutil.disk_partitions():
            usage = psutil.disk_usage(disk.mountpoint)
            print(
                f"Device: {disk.device}."
                f"\nFilesystem: {disk.fstype}; "
                f"Options: {disk.opts}; "
                f"Max file name size: {disk.maxfile}; "
                f"Max path name size: {disk.maxpath}; "
                f"\nDisk size: {usage.total // 2**30}Gb "
                f"(Used {usage.used // 2**30}Gb, "
                f"Free {usage.free // 2**30}Gb)."
                f"\n"
            )


    def workWithFile():
        file = open('DO_NOT_DELETE_THIS_FILE.LIKE_EVER', 'w')
        s = str()
        print("Type your text (print \\0 for exit):")
        while True:
            s = input()
            if s == "\\0":
                break
            file.write(s)
            file.write("\n")
        file.close()
        file = open('DO_NOT_DELETE_THIS_FILE.LIKE_EVER', 'r')
        print(file.read())
        file.close()
        os.remove('DO_NOT_DELETE_THIS_FILE.LIKE_EVER')

    def workWithJson():
        class incident():
            def __init__(self, title, severity, TLP, assignee, date, tags):
                self.title = title
                self.severity = severity
                self.TLP = TLP
                self.assignee = assignee
                self.date = date
                self.tags = tags

            def assigne(self, assignee):
                if assignee == self.assignee:
                    print("You're already the assignee of this case")
                else:
                    self.assignee = assignee
                    print("Successfully assigned case to you")

            def toJSON(self):
                return json.dumps(self, default=lambda o: o.__dict__,
                                  sort_keys=True, indent=4)

        A = incident(
            input("Title: "),
            input("Severity: "),
            input("TLP: "),
            input("Assignee: "),
            input("Date: "),
            input("Tags: ").replace(', ', ',').split(",")
        )
        file = open('smth.json', 'w')
        file.write(A.toJSON())
        file.close()
        file = open('smth.json', 'r')
        print(file.read())
        file.close()
        os.remove("smth.json")


    def workWithXML():
        e1 = ET.Element('outside')
        e2 = ET.SubElement(e1, 'inside')
        e1.append(ET.Comment(r'____ comment ____'))
        tree = ET.ElementTree(e1)
        f = []

        for i in range(3):
            f.append(ET.SubElement(e2, input("Enter name of subelement: ")))
            f[i].append(ET.Comment(input('Enter comment: ')))

        tree.write("HGFHJKLMJNHBGFCDXS.xml")
        file = open('HGFHJKLMJNHBGFCDXS.xml', 'r')
        print(file.read())
        file.close()
        os.remove("HGFHJKLMJNHBGFCDXS.xml")


    def workWithzip():
        file = open('erwh.txt', 'w')
        for i in range(int(random.random() * 1024)):
            file.write("HJJRJJRTR -> " + str(random.random() * random.random() * 10) + '\n')
        file.close()
        with zipfile.ZipFile('HTRHWU754ye.zip', 'w') as myzip:
            myzip.write('erwh.txt')
            os.remove('erwh.txt')
            print('zip contains:')
            myzip.printdir()
            print('\nzip size: ' + str(os.stat('HTRHWU754ye.zip').st_size / 2**20) + "Mb")
            input('Press Enter for unzipping file....')
            myzip.extractall()
            myzip.close()
        input('Press Enter for removing files....')
        os.remove('erwh.txt')
        os.remove('HTRHWU754ye.zip')


    if __name__ == '__main__':
        while True:
            print(
                "Choose menu item:\n"
                  "1 - print disk info\n"
                  "2 - work with text-file\n"
                  "3 - work with Json-file\n"
                  "4 - work with XML-file\n"
                  "5 - work with zip-file\n"
                  "0 - exit"
            )
            switch = input()
            if switch == "1":
                printDisksInfo()
                print("\n")
            elif switch == "2":
                workWithFile()
                print("\n")
            elif switch == "3":
                workWithJson()
                print("\n")
            elif switch == "4":
                workWithXML()
                print("\n")
            elif switch == "5":
                workWithzip()
            elif switch == "0":
                break
            else:
                print("No such item, try again")
        print("Goodbye!")
else:
    print("You're using non-windows OS.\nPlease, stop doing this!")
