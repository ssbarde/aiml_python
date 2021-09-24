import PyPDF2

def line():
    print("-----------------------------------------------------------------------------------------------------------")


def getUseFulIndex(main):
    indexes = [0, 1, 32, 45, 58, 71, 84, 97, 110, 123, 136]  # these are useful index to containing required information
    while " #" in main:  # removing #
        main.remove(" #")
    for m in main:
        if "$" in m and not "$/" in m:  # removing un-useful marks
            main.remove(m)
    for m in main:
        if "!" in m and not "!/" in m:  # removing un-useful marks
            main.remove(m)
    mylist = []
    for i in indexes:
        # if i < len(main):
        mylist.append(main[i])
    return mylist


def actualContent(main):
    indexes = [0, 1, 28, 41, 54, 67, 80, 94, 109,120,121,133,134,145,158,171,184,197,211,224,225,237,251,263,284]

    while " #" in main:
        main.remove(" #")
    for m in main:
        if "$" in m and not "$/" in m:
            main.remove(m)
        # for m in main:
        if "!" in m and not "!/" in m:
            main.remove(m)
        if "&" in m and not "P&" in m and not "&/" in m:
            main.remove(m)
    mylist = []
    for i in indexes:
        if i < len(main):
            mylist.append(main[i])
    return mylist


def calculate_total_marks(main):
    total_marks = 0
    for m in main[2:]:
        if m.isdigit():
            total_marks += int(m)
    return str(total_marks)


def calculate_total_marks123(main):
    if not main:
        return ''
    total_marks = 0
    for m in range(2, len(main) - 1):
        temp = main[m]
        if "/" in temp:
            temp = temp.split("/")[0]
        if temp.isdigit():
            total_marks += int(temp)
    return str(total_marks)


pdfFileObj = open(r'C:\SSB\from_Jan_2017\myWorld\ehb\AI ML\Code\acadflip prediction\TE.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

total_page = pdfReader.getNumPages()
print("total pages", total_page)
# total_page=1
# total_page=25
file1 = open("TEAll_final.csv", "a")

# file1.write("PNR number,Name,TOC,DBMS,SE&PM,IS&EE,CN,Skill Development Lab,DBMS Lab,CN Lab" + "\n")
# file1.write("PNR number,Name,410241,410241,410241,410242,410242,410242,410243,410243,410243,410244D,410244D,410244D,"
#             "410245B,410245B,410245B,410246,410246,410247,410247,410248,SGPA,Total" + "\n")

file1.write("PNR number,Name,210241,210241,210241,210242,210242,210242,210243,210243,210243,210244D,210244D,210244D,"
            "210245B,210245B,210245B,210246,210247,210248,210249,SGPA,Total" + "\n")
# list1=['g','t','M']
# file1.write(",".join(list1) + "\n")

for i in range(total_page):

    pageObj = pdfReader.getPage(i)

    obj = pageObj.extractText()

    obj = obj.split(
        "....................................................................................................")[
        1]

    # print("\n obj is:",obj)
    splitting = obj.split("DISTRIBUTION...........")
    main = splitting[0].split("  ")

    while "" in main:
        main.remove("")
    while " " in main:
        main.remove(" ")

    my_list = actualContent(main)

    my_list.append(calculate_total_marks123(my_list))
    print(my_list)
    if my_list:
        file1.write(",".join(my_list) + "\n")

    main = splitting[1].split("  ")
    while "" in main:
        main.remove("")
    while " " in main:
        main.remove(" ")

    if 136 > len(main):
        continue

    my_list = actualContent(main)
    my_list.append(calculate_total_marks123(my_list))
    # print(my_list)

    if my_list:
        # print("writing in file")
        file1.write(",".join(my_list) + "\n")

file1.close()