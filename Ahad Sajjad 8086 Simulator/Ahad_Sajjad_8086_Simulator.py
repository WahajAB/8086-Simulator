from tkinter import *
window = Tk()
window.title("8086 Simulator")
window.resizable(False, False)
window.state("zoomed")
Registers = ["AX", "BX", "CX", "DX", "SI", "DI", "BP", "SP"]
Reg_Values = ["0x1234", "0x9523", "0x5432",
              "0x3215", "0x1245", "0x6142", "0x1632", "0x7341"]
Mems = ["0x3010", "0x3011", "0x3012", "0x3013", "0x3014", "0x3015", "0x3016",
        "0x3017", "0x3018", "0x3019", "0x301A", "0x301B", "0x301C", "0x301D", "0x301E", "0x301F"]
Mem_Values = ["0x00A0", "0x00B0", "0x00C0", "0x00D0", "0x00E0", "0x00F0", "0x00AB",
              "0x00AC", "0x00AD", "0x00AE", "0x00AF", "0x00BA", "0x00BB", "0x00BC", "0x00BD", "0x00BE"]
Reg_Table = ["000", "011", "001", "010", "110", "111", "101", "100"]
Instructions = ["MOV", "DIV", "MUL", "ADD", "CDQ", "XCHG",
                "SUB", "INC", "DEC", "AND", "OR", "NOT", "XOR", "SHR", "SHL"]

Ins = ["1000 10", "1111 01", "1111 01", "0000 00", "1001 1001", "1000 01", "0010 10",
       "1111 11", "1111 11", "0010 00", "0000 10", "1111 01", "0011 00", "1100 00", "1100 00"]
bg = PhotoImage(
    file="vecteezy_abstract-futuristic-background-blue-glowing-technology-sci_.png")

lbl = Label(window, image=bg)
lbl.place(x=0, y=0)
p1 = PhotoImage(
    file="cpu-icon-microprocessor-and-processor-symbol-vector-5524341.png")
window.iconphoto(False, p1)
buttoncolor = '#010329'
headercolor = 'white'
textbackground = '#010329'
buttontextbackground = 'white'

framecolor = "black"

# Helpers


def convert(value):
    value = value[2:]
    value = int(value, 16)
    temp = format(value, "b")
    while (len(temp) != 16):
        temp = "0" + temp
    temp1 = temp[8:12]
    temp2 = temp[12:16]
    temp3 = temp[0:4]
    temp4 = temp[4:8]
    value = temp1 + " " + temp2 + " " + temp3 + " " + temp4
    return value


def filler(value):
    value = value[2:]
    while len(value) != 4:
        value = "0"+value
    value = "0x" + value.upper()
    return value


def destruct(master):
    master.destroy()


def validate(value):
    try:
        value = int(value, 16)
        if value < 0 or value > 65535:
            return 0
        else:
            return 1
    except:
        return 0


def validate2(value):
    try:
        value = int(value)
        if value < 0:
            return 0
        else:
            return 1
    except:
        return 0
# XChange


def xchg_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    elif S1.upper() not in Registers and S1 not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        i = Registers.index(S)
        if S1.upper() in Registers:
            i2 = Registers.index(S1)
            temp = Reg_Values[i]
            Reg_Values[i] = Reg_Values[i2]
            Reg_Values[i2] = temp
            reg_labels[i].config(text=S + " : " + Reg_Values[i])
            reg_labels[i2].config(text=S1 + " : " + Reg_Values[i2])
            Mod = "11"
            R_M = Reg_Table[i2]
        elif S1 in Mems:
            i2 = Mems.index(S1)
            temp = Reg_Values[i]
            Reg_Values[i] = Mem_Values[i2]
            Mem_Values[i2] = temp
            reg_labels[i].config(text=S + " : " + Reg_Values[i])
            Meg_labels[i2].config(text=S1 + " : " + Mem_Values[i2])
            R_M = "110"
            Mod = "00"
        opcode = Ins[5]
        D = "1"
        WORD = "1"
        Reg = Reg_Table[i]
        opcodegen.config(text=opcode + D + WORD + " " +
                         Mod + Reg[0:2] + " " + Reg[2:3] + R_M)

        destruct(newWindow)


def xchg_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg/Mem: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: xchg_check(entry1, entry2), fg='white', bg='#010329')
    btn.grid(row=0, column=2, rowspan=2)

# Left Shift


def shl_check(E1, entry2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = entry2.get()
    if S not in Registers or validate2(S1) == 0:
        error.config(text="Invalid Input(s)")
    else:
        S2 = int(S1)
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16)
        r3 = r3 << S2
        s3 = hex(r3)
        if (r3 > 65535):
            s3 = s3[3:]
            s3 = "0x"+s3
            # r - r
        Reg_Values[i] = filler(s3)
        reg_labels[i].config(text=S + ": " + Reg_Values[i])
        Opcode = "1100 00"
        D = "0"
        WORD = "1"
        Mod = "00"
        Reg = "100"
        R_M = Reg_Table[i]
        opcodegen.config(text=Opcode + D + WORD + " " +
                         Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
        destruct(newWindow)


def shl_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", fg='white', bg='#010329')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Num places: ",
                       fg='white', bg='#010329')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)

    btn = Button(newWindow, text="Enter",
                 command=lambda: shl_check(entry1, entry2), fg='white', bg='#010329')
    btn.grid(row=0, column=2, rowspan=2)

# Right Shift


def shr_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers or validate2(S1) == 0:
        error.config(text="Invalid Input(s)")
    else:
        S2 = int(S1)
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16)
        r3 = r3 >> S2
        if (r3 > 65535):
            error.config(text="Error: Shift greater than 0xFFFF.")
        else:
            s3 = hex(r3)
            # r - r
            Reg_Values[i] = filler(s3)
            reg_labels[i].config(text=S + ": " + Reg_Values[i])
            Opcode = "1100 00"
            D = "0"
            WORD = "1"
            Mod = "00"
            Reg = "101"
            R_M = Reg_Table[i]
            opcodegen.config(text=Opcode + D + WORD + " " +
                             Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            destruct(newWindow)


def shr_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Num places: ",
                       bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)

    btn = Button(newWindow, text="Enter",
                 command=lambda: shr_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


# XOR instruction
def XOR_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Registers.index(y)
    r1 = Reg_Values[i]
    r2 = Reg_Values[i2]
    r3 = int(r1, 16)
    r3 = format(r3, "b")
    r4 = int(r2, 16)
    r4 = format(r4, "b")
    while (len(r3) != 16):
        r3 = "0"+r3
    while (len(r4) != 16):
        r4 = "0"+r4
    list1 = []
    list2 = []
    list3 = []
    list1[:0] = r3
    list2[:0] = r4
    for a, b in zip(list1, list2):
        if a == "1" and b == "0":
            list3.append("1")
        elif a == "0" and b == "1":
            list3.append("1")
        else:
            list3.append("0")
    r3 = "".join(list3)
    r3 = int(r3, 2)
    s3 = hex(r3)
    Reg_Values[i] = filler(s3)
    reg_labels[i].config(text=x + ": " + Reg_Values[i])
    Opcode = Ins[12]
    D = "1"
    Word = "1"
    Mod = "11"
    Reg = Reg_Table[i]
    R_M = Reg_Table[i2]
    opcodegen.config(text=Opcode + D + Word + " " + Mod +
                     Reg[0:2] + " " + Reg[2:3] + R_M)
    destruct(newWindow)


def XOR_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    S1 = S1.upper()
    if S and S1 not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        XOR_getEntry(S, S1)


def XOR_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("XOR Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg 1: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg 2: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: XOR_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)

# Multiply


def mul_check(text1, E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    temp = "Do"
    S = E1.get()
    if text1 == "Reg":
        if (S.upper() not in Registers):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Registers.index(S)
            temp = Reg_Values[i2]
            R_M = Reg_Table[i2]
            Mod = "11"
    elif text1 == "Mem":
        if (S not in Mems):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Mems.index(S)
            temp = Mems[i2]
            Mod = "00"
            R_M = "110"
            Disp = convert(Mems[i2])
    if temp != "Do":
        temp2 = int(temp, 16) * int(Reg_Values[0], 16)
        if (temp2 > 4294967295):
            error.config(text="Error: Product greater than 0 x FFFF FFFF.")
        else:
            temp3 = hex(temp2)
            temp3 = temp3[2:]
            while len(temp3) != 8:
                temp3 = "0" + temp3
            temp3 = temp3.upper()
            Reg_Values[0] = "0x" + temp3[4:8]
            Reg_Values[3] = "0x" + temp3[0:4]
            reg_labels[0].config(text=Registers[0] + " : " + Reg_Values[0])
            reg_labels[3].config(text=Registers[3] + " : " + Reg_Values[3])
            Opcode = Ins[2]
            D = "1"
            W = "1"
            Reg = "100"
            if text1 == "Reg":
                opcodegen.config(text=Opcode + D + W + " " +
                                 Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            else:
                opcodegen.config(text=Opcode + D + W + " " + Mod +
                                 Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)


def mul_createFormUni(text1):
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text=text1 + ": ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mul_check(text1, entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2, rowspan=1)


def mul_formselect():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Select multiplier: ",
                      bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    btn1 = Button(newWindow, text="Reg", height=2, width=15,
                  command=lambda: mul_createFormUni("Reg"), bg='#010329', fg='white')
    btn1.grid(row=1, column=0, rowspan=1)
    btn2 = Button(newWindow, text="Mem", height=2, width=15,
                  command=lambda: mul_createFormUni("Mem"), bg='#010329', fg='white')
    btn2.grid(row=2, column=0, rowspan=1)

# Division


def div_check(text1, E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    temp = "Do"
    S = E1.get()
    if text1 == "Reg":
        if (S.upper() not in Registers):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Registers.index(S)
            temp = Reg_Values[i2]
            R_M = Reg_Table[i2]
            Mod = "11"
    elif text1 == "Mem":
        if (S not in Mems):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Mems.index(S)
            temp = Mem_Values[i2]
            Mod = "00"
            R_M = "110"
            Disp = convert(Mems[i2])
    if temp != "Do":
        DX_AX = Reg_Values[3][2:6] + Reg_Values[0][2:6]
        tempQ = int(DX_AX, 16) // int(temp, 16)
        if tempQ > 65535:
            error.config(text="Error: Quotient > 16 bits. Cannot store.")
        else:
            tempR = int(DX_AX, 16) % int(temp, 16)
            tempAX = hex(tempQ)
            tempDX = hex(tempR)
            Reg_Values[0] = filler(tempAX)
            Reg_Values[3] = filler(tempDX)
            reg_labels[0].config(text=Registers[0] + " : " + Reg_Values[0])
            reg_labels[3].config(text=Registers[3] + " : " + Reg_Values[3])
            Opcode = Ins[1]
            D = "1"
            W = "1"
            Reg = "110"
            if text1 == "Reg":
                opcodegen.config(text=Opcode + D + W + " " +
                                 Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            else:
                opcodegen.config(text=Opcode + D + W + " " + Mod +
                                 Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)


def div_createFormUni(text1):
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text=text1 + ": ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: div_check(text1, entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2, rowspan=1)


def div_formselect():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Select divisor: ",
                      bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    btn1 = Button(newWindow, text="Reg", height=2, width=15,
                  command=lambda: div_createFormUni("Reg"), bg='#010329', fg='white')
    btn1.grid(row=1, column=0, rowspan=1)
    btn2 = Button(newWindow, text="Mem", height=2, width=15,
                  command=lambda: div_createFormUni("Mem"), bg='#010329', fg='white')
    btn2.grid(row=2, column=0, rowspan=1)
    btn3 = Button(newWindow, text="Value", height=2, width=15,
                  command=lambda: div_createFormUni("Value"), bg='#010329', fg='white')
    btn3.grid(row=3, column=0, rowspan=1)
# Not


def Not_():
    global newWindow
    newWindow = Tk()
    newWindow.title("Enter Reg")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter", command=lambda: Not_Check(
        entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2)


def Not_Check(entry1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = entry1.get()
    S = S.upper()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16)
        r3 = format(r3, "b")
        while (len(r3) != 16):
            r3 = "0" + r3
        list1 = []
        list2 = []
        list1[:0] = r3
        for a in list1:
            if a == "0":
                list2.append("1")
            if a == "1":
                list2.append("0")
        r3 = "".join(list2)
        r3 = int(r3, 2)
        s3 = hex(r3)
        Reg_Values[i] = filler(s3)
        reg_labels[i].config(text=S + ": " + Reg_Values[i])
        Opcode = Ins[11]
        D = "1"
        Word = "1"
        Mod = "11"
        Reg = "010"
        R_M = Reg_Table[i]
        opcodegen.config(text=Opcode + D + Word + " " +
                         Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
        destruct(newWindow)

# AND Instruction


def AND_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Registers.index(y)
    r1 = Reg_Values[i]
    r2 = Reg_Values[i2]
    r3 = int(r1, 16)
    r3 = format(r3, "b")
    r4 = int(r2, 16)
    r4 = format(r4, "b")
    while (len(r3) != 16):
        r3 = "0" + r3
    while (len(r4) != 16):
        r4 = "0" + r4
    list1 = []
    list2 = []
    list3 = []
    list1[:0] = r3
    list2[:0] = r4
    for a, b in zip(list1, list2):
        if a == "1" and b == "1":
            list3.append("1")
        else:
            list3.append("0")
    r3 = "".join(list3)
    r3 = int(r3, 2)
    s3 = hex(r3)
    Reg_Values[i] = filler(s3)
    reg_labels[i].config(text=x + ": " + Reg_Values[i])
    Opcode = Ins[9]
    D = "1"
    Word = "1"
    Mod = "11"
    Reg = Reg_Table[i]
    R_M = Reg_Table[i2]
    opcodegen.config(text=Opcode + D + Word + " " + Mod +
                     Reg[0:2] + " " + Reg[2:3] + R_M)
    destruct(newWindow)


def AND_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    S1 = S1.upper()
    if S and S1 not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        AND_getEntry(S, S1)


def AND_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("AND Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg 1: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg 2: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: AND_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)

# OR instruction


def OR_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Registers.index(y)
    r1 = Reg_Values[i]
    r2 = Reg_Values[i2]
    r3 = int(r1, 16)
    r3 = format(r3, "b")
    r4 = int(r2, 16)
    r4 = format(r4, "b")
    while (len(r3) != 16):
        r3 = "0" + r3
    while (len(r4) != 16):
        r4 = "0" + r4
    list1 = []
    list2 = []
    list3 = []
    list1[:0] = r3
    list2[:0] = r4
    for a, b in zip(list1, list2):
        if a == "1" or b == "1":
            list3.append("1")
        else:
            list3.append("0")
    r3 = "".join(list3)
    r3 = int(r3, 2)
    s3 = hex(r3)
    Reg_Values[i] = filler(s3)
    reg_labels[i].config(text=x + ": " + Reg_Values[i])
    Opcode = Ins[10]
    D = "1"
    Word = "1"
    Mod = "11"
    Reg = Reg_Table[i]
    R_M = Reg_Table[i2]
    opcodegen.config(text=Opcode + D + Word + " " + Mod +
                     Reg[0:2] + " " + Reg[2:3] + R_M)
    destruct(newWindow)


def OR_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    S1 = S1.upper()
    if S and S1 not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        OR_getEntry(S, S1)


def OR_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("OR Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg 1: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg 2: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: OR_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


#MOV (Reg <- Reg)


def mov1_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Registers.index(y)
    Reg_Values[i] = Reg_Values[i2]
    reg_labels[i].config(text=x + " : " + Reg_Values[i])
    reg_labels[i2].config(text=y + " : " + Reg_Values[i2])
    Opcode = Ins[0]
    D = "1"
    Word = "1"
    Mod = "11"
    Reg = Reg_Table[i]
    R_M = Reg_Table[i2]
    opcodegen.config(text=Opcode + D + Word + " " + Mod +
                     Reg[0:2] + " " + Reg[2:3] + R_M)
    destruct(newWindow)
    destruct(aNewWindow)


def mov1_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    S1 = S1.upper()
    if S and S1 not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        mov1_getEntry(S, S1)


def mov1_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mov1_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)

#Mov (Mem <- Reg)


def mov2_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global Meg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Mems.index(y)
    Mem_Values[i2] = Reg_Values[i]
    Meg_labels[i2].config(text=y + " : " + Mem_Values[i2])
    Opcode = Ins[0]
    D = "0"
    Word = "1"
    Mod = "00"
    Reg = Reg_Table[i]
    R_M = "110"
    Disp = convert(Mems[i2])
    opcodegen.config(text=Opcode + D + Word + " " + Mod +
                     Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
    destruct(newWindow)
    destruct(aNewWindow)


def mov2_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    elif S1 not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        mov2_getEntry(S, S1)


def mov2_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Mem: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mov2_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)

#Mov (Reg <- Mem)


def mov3_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global Meg_labels
    x = entry1
    y = entry2
    i = Registers.index(x)
    i2 = Mems.index(y)
    Reg_Values[i] = Mem_Values[i2]
    reg_labels[i].config(text=x + " : " + Reg_Values[i])
    Opcode = Ins[0]
    D = "1"
    Word = "1"
    Mod = "00"
    Reg = Reg_Table[i]
    R_M = "110"
    Disp = convert(Mems[i2])
    opcodegen.config(text=Opcode + D + Word + " " + Mod +
                     Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
    destruct(newWindow)
    destruct(aNewWindow)


def mov3_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    elif S1 not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        mov3_getEntry(S, S1)


def mov3_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    templabel2 = Label(newWindow, text="Mem: ", bg='#010329', fg='white')
    templabel2.grid(row=0, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=0, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mov3_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def mov1():
    mov1_createFormBi()


def mov2():
    mov2_createFormBi()


def mov3():
    mov3_createFormBi()


# Addition
def add_rr_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    S1 = S1.upper()
    if S and S1 not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        i2 = Registers.index(S1)
        r1 = Reg_Values[i]
        r2 = Reg_Values[i2]
        r3 = int(r1, 16) + int(r2, 16)
        if (r3 > 65535):
            error.config(text="Error: Sum greater than 0xFFFF.")
        else:
            s3 = hex(r3)
            # r - r
            Reg_Values[i] = filler(s3)
            reg_labels[i].config(text=S + ": " + Reg_Values[i])
            Opcode = Ins[3]
            D = "1"
            Word = "1"
            Mod = "11"
            Reg = Reg_Table[i]
            R_M = Reg_Table[i2]
            opcodegen.config(text=Opcode + D + Word + " " +
                             Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            destruct(newWindow)
            destruct(aNewWindow)


def add_rr_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: add_rr_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def add_rm_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    elif S1 not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        global Reg_Values
        global Meg_labels
        i = Registers.index(S)
        i2 = Mems.index(S1)
        r1 = Mem_Values[i2]
        r2 = Reg_Values[i]
        r3 = int(r1, 16) + int(r2, 16)
        if (r3 > 65535):
            error.config(text="Error: Sum greater than 0xFFFF.")
        else:
            s3 = hex(r3)
            # r-m
            Reg_Values[i] = filler(s3)
            reg_labels[i].config(text=S + ": " + Reg_Values[i])
            Opcode = Ins[3]
            D = "1"
            Word = "1"
            Mod = "00"
            Reg = Reg_Table[i]
            R_M = "110"
            Disp = convert(Mems[i2])
            opcodegen.config(text=Opcode + D + Word + " " +
                             Mod + Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)
            destruct(aNewWindow)


def add_rm_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Mem: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: add_rm_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def add_mr_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    elif S1 not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        global Reg_Values
        global Meg_labels
        i = Registers.index(S)
        i2 = Mems.index(S1)
        r1 = Mem_Values[i2]
        r2 = Reg_Values[i]
        r3 = int(r1, 16) + int(r2, 16)
        if (r3 > 65535):
            error.config(text="Error: Sum greater than 0xFFFF.")
        else:
            s3 = hex(r3)
            # r-m
            Mem_Values[i2] = filler(s3)
            Meg_labels[i2].config(text=S1 + ": " + Mem_Values[i2])
            Opcode = Ins[3]
            D = "0"
            Word = "1"
            Mod = "00"
            Reg = Reg_Table[i]
            R_M = "110"
            Disp = convert(Mems[i2])
            opcodegen.config(text=Opcode + D + Word + " " +
                             Mod + Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)
            destruct(aNewWindow)


def add_mr_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    templabel2 = Label(newWindow, text="Mem: ", bg='#010329', fg='white')
    templabel2.grid(row=0, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=0, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: add_mr_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def add_ri_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if (validate(S1) == 0):
        error.config(text="Invalid Input(s)")
    elif (S not in Registers):
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        i2 = Registers.index(S)
        temp = Reg_Values[i2]
        temp2 = int(temp, 16) + int(S1, 16)
        if (temp2 > 65535):
            error.config(text="Error: Sum greater than 0xFFFF.")
        else:
            temp3 = hex(temp2)
            Reg_Values[i2] = filler(temp3)
            reg_labels[i2].config(text=S + " : " + Reg_Values[i2])
            Opcode = "1000 00"
            D = "0"
            Word = "1"
            Mod = "00"
            Reg = Reg_Table[i2]
            R_M = "110"
            opcodegen.config(text=Opcode + D + Word + " " +
                             Mod + R_M + Reg[0:2] + " " + Reg[2:3])

            destruct(newWindow)
            destruct(aNewWindow)


def add_ri_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Immi: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    templabel2 = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel2.grid(row=0, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=0, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: add_ri_check(entry2, entry1), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def add_mi_check(E1, E2):
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S1 = E2.get()
    if (validate(S1) == 0):
        error.config(text="Invalid Input(s)")
    elif (S not in Mems):
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        i2 = Mems.index(S)
        temp = Mem_Values[i2]
        temp2 = int(temp, 16) + int(S1, 16)
        if (temp2 > 65535):
            error.config(text="Error: Sum greater than 0xFFFF.")
        else:
            temp3 = hex(temp2)
            Mem_Values[i2] = filler(temp3)
            Meg_labels[i2].config(text=S + " : " + Mem_Values[i2])
            Opcode = "1000 00"
            D = "0"
            Word = "1"
            Mod = "00"
            Reg = "000"
            R_M = "110"
            Disp1 = convert(Mems[i2])
            Disp = convert(Mem_Values[i2])
            opcodegen.config(text=Opcode + D + WORD + " " + Mod +
                             Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp1 + " " + Disp)
            destruct(newWindow)
            destruct(aNewWindow)


def add_mi_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Mem: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    templabel2 = Label(newWindow, text="Immi: ", bg='#010329', fg='white')
    templabel2.grid(row=0, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=0, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: add_mi_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def add_createFormSelector():
    global aNewWindow
    aNewWindow = Tk()
    aNewWindow.title = "ADD MODE SELECTOR"
    aNewWindow.resizable(False, False)
    aNewWindow.configure(background='#010329')

    lab1 = Label(aNewWindow, text="Select the mode of addition ",
                 bg='#010329', fg='white')
    lab1.grid(row=0, column=1)

    but1 = Button(aNewWindow, text="REG + REG", height=2,
                  width=15, command=lambda: add_rr_createFormBi(), bg='#010329', fg='white')
    but1.grid(pady=1, row=1, column=1)

    but2 = Button(aNewWindow, text="REG + MEM", height=2,
                  width=15, command=lambda: add_rm_createFormBi(), bg='#010329', fg='white')
    but2.grid(row=2, column=1)

    but3 = Button(aNewWindow, text="MEM + REG", height=2,
                  width=15, command=lambda: add_mr_createFormBi(), bg='#010329', fg='white')
    but3.grid(row=3, column=1)

    but4 = Button(aNewWindow, text="REG + IMMEDIATE", height=2,
                  width=15, command=lambda: add_ri_createFormBi(), bg='#010329', fg='white')
    but4.grid(row=4, column=1)

    but5 = Button(aNewWindow, text="MEM + IMMEDIATE", height=2,
                  width=15, command=lambda: add_mi_createFormBi(), bg='#010329', fg='white')
    but5.grid(row=5, column=1)


def add():
    add_createFormSelector()
# mov form selector code


def mov_createFormSelector():
    global aNewWindow
    aNewWindow = Tk()
    aNewWindow.title = "Mov MODE SELECTOR"
    aNewWindow.configure(background='#010329')

    lab1 = Label(aNewWindow, text="Select the mode of Move ",
                 bg='#010329', fg='white')
    lab1.grid(row=0, column=1)

    but1 = Button(aNewWindow, text="REG <- REG", height=2,
                  width=15, command=lambda: mov1(), bg='#010329', fg='white')
    but1.grid(pady=1, row=1, column=1)

    but2 = Button(aNewWindow, text="REG <- MEM", height=2,
                  width=15, command=lambda: mov3(), bg='#010329', fg='white')
    but2.grid(row=2, column=1)

    but3 = Button(aNewWindow, text="MEM <- REG", height=2,
                  width=15, command=lambda: mov2(), bg='#010329', fg='white')
    but3.grid(row=3, column=1)

    but4 = Button(aNewWindow, text="REG <- IMMEDIATE", height=2,
                  width=15, command=lambda: mov_4_ri(), bg='#010329', fg='white')
    but4.grid(row=4, column=1)

    but5 = Button(aNewWindow, text="MEM <- IMMEDIATE", height=2,
                  width=15, command=lambda: mov_5_mi(), bg='#010329', fg='white')
    but5.grid(row=5, column=1)


def mov():
    mov_createFormSelector()

# Cdq


def cdq():
    Reg_Values[3] = "0x0000"
    reg_labels[3].config(text="DX: " + Reg_Values[3])
    opcodegen.config(text=Ins[4])
# Increment


def inc_check(E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16) + 1
        if (r3 > 65535):
            error.config(text="Error: Value Overflows over 0xFFFF.")
        else:
            s3 = hex(r3)
            # r - r
            Reg_Values[i] = filler(s3)
            reg_labels[i].config(text=S + ": " + Reg_Values[i])
            Opcode = Ins[7]
            D = "1"
            Word = "1"
            Mod = "11"
            Reg = "000"
            R_M = Reg_Table[i]
            opcodegen.config(text=Opcode + D + Word + " " +
                             Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            destruct(newWindow)


def inc():
    global newWindow
    newWindow = Tk()
    newWindow.title("Enter Reg")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter", command=lambda: inc_check(
        entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2)


# Decrement
def dec_check(E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    if S not in Registers:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        global Reg_Values
        global reg_labels
        i = Registers.index(S)
        r1 = Reg_Values[i]
        r3 = int(r1, 16) - 1
        if (r3 < 0):
            error.config(text="Error: Value Underflows from 0x0000.")
        else:
            s3 = hex(r3)
            # r - r
            Reg_Values[i] = filler(s3)
            reg_labels[i].config(text=S + ": " + Reg_Values[i])
            Opcode = Ins[8]
            D = "1"
            Word = "1"
            Mod = "11"
            Reg = "001"
            R_M = Reg_Table[i]
            opcodegen.config(text=Opcode + D + Word + " " +
                             Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            destruct(newWindow)


def dec():
    global newWindow
    newWindow = Tk()
    newWindow.title("Enter Reg")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter", command=lambda: dec_check(
        entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2)

# Mov4


def mov4_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = "0x" + entry2
    i = Registers.index(x)
    Reg_Values[i] = filler(y)
    opcode = "101"
    D = "1"
    WORD = "1"
    Reg = Reg_Table[i]
    Disp = convert(Reg_Values[i])
    opcodegen.config(text=opcode + D + " " + WORD + Reg + " " + Disp)
    reg_labels[i].config(text=x + ": " + Reg_Values[i])

    destruct(newWindow)
    destruct(aNewWindow)


def mov4_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S = S.upper()
    S1 = E2.get()
    if validate(S1) == 0:
        error.config(text="Invalid Input(s)")
    elif (S not in Registers):
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        mov4_getEntry(S, S1)


def mov4_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Immi: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mov4_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def mov_4_ri():
    mov4_createFormBi()

# Mov5


def mov5_getEntry(entry1, entry2):
    global Registers
    global Reg_Values
    global reg_labels
    x = entry1
    y = "0x" + entry2
    i = Mems.index(x)
    Mem_Values[i] = filler(y)
    Meg_labels[i].config(text=x + ": " + Mem_Values[i])
    opcode = "1100 01"
    D = "1"
    WORD = "1"
    MOD = "00"
    Reg = "000"
    R_M = "110"
    Disp1 = convert(Mems[i])
    Disp = convert(Mem_Values[i])
    opcodegen.config(text=opcode + D + WORD + " " + MOD +
                     Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp1 + " " + Disp)
    destruct(newWindow)
    destruct(aNewWindow)


def mov5_check(E1, E2):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    S = E1.get()
    S1 = E2.get()
    if validate(S1) == 0:
        error.config(text="Invalid Input(s)")
    elif S not in Mems:
        error.config(text="Invalid Input(s)")
    else:
        error.config(text="")
        mov5_getEntry(S, S1)


def mov5_createFormBi():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.configure(background='#010329')
    templabel = Label(newWindow, text="Mem: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=0, column=1)
    templabel2 = Label(newWindow, text="Immi: ", bg='#010329', fg='white')
    templabel2.grid(row=1, column=0)
    entry2 = Entry(newWindow, bg='black', fg='white')
    entry2.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: mov5_check(entry1, entry2), bg='#010329', fg='white')
    btn.grid(row=0, column=2, rowspan=2)


def mov_5_mi():
    mov5_createFormBi()


def sub():
    sub_formselect()


# SUBTRACTION
def sub_check(text1, E0, E1):
    global Registers
    error = Label(newWindow, text="")
    error.grid(row=2, column=0, columnspan=3)
    temp = "Do"
    S0 = E0.get()
    S0 = S0.upper()
    S = E1.get()
    if (S0 not in Registers):
        error.config(text="Invalid Input(s)")
    elif text1 == "Reg":
        if (S.upper() not in Registers):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Registers.index(S)
            temp = Reg_Values[i2]
            Opcode = Ins[6]
            D = "1"
            iT = Registers.index(S0)
            Reg = Reg_Table[iT]
            Mod = "11"
            R_M = Reg_Table[i2]

    elif text1 == "Mem":
        if (S not in Mems):
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            i2 = Mems.index(S)
            temp = Mems[i2]
            Opcode = Ins[6]
            D = "1"
            Mod = "00"
            iT = Registers.index(S0)
            Reg = Reg_Table[iT]
            R_M = "110"
            Disp = convert(S)

    elif text1 == "Value":
        if validate(S) == 0:
            error.config(text="Invalid Input(s)")
        else:
            error.config(text="")
            temp = S
            Opcode = "1000 00"
            D = "0"
            Mod = "00"
            iT = Registers.index(S0)
            R_M = Reg_Table[iT]
            Reg = "101"
            Disp = convert(hex(int(temp, 16)))

    if temp != "Do":
        i = Registers.index(S0)
        tempReg = Reg_Values[i]
        temp2 = int(tempReg, 16) - int(temp, 16)
        if (temp2 < 0):
            error.config(text="Error: Underflow - Value less than 0x0000.")
        else:
            temp3 = hex(temp2)
            Reg_Values[i] = filler(temp3)
            reg_labels[i].config(text=Registers[i] + ": " + Reg_Values[i])
            Word = "1"
            if text1 == "Reg":
                opcodegen.config(text=Opcode + D + Word + " " +
                                 Mod + Reg[0:2] + " " + Reg[2:3] + R_M)
            else:
                opcodegen.config(text=Opcode + D + Word + " " +
                                 Mod + Reg[0:2] + " " + Reg[2:3] + R_M + " " + Disp)
            destruct(newWindow)


def sub_createFormUni(text1):
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='#010329')
    templabel1 = Label(newWindow, text="Reg: ", bg='#010329', fg='white')
    templabel1.grid(row=0, column=0)
    entry0 = Entry(newWindow, bg='black', fg='white')
    entry0.grid(row=0, column=1)
    templabel = Label(newWindow, text=text1 + ": ", bg='#010329', fg='white')
    templabel.grid(row=1, column=0)
    entry1 = Entry(newWindow, bg='black', fg='white')
    entry1.grid(row=1, column=1)
    btn = Button(newWindow, text="Enter",
                 command=lambda: sub_check(text1, entry0, entry1), bg='#010329', fg='white')
    btn.grid(row=1, column=2, rowspan=1)


def sub_formselect():
    global newWindow
    newWindow = Tk()
    newWindow.title("Input")
    newWindow.resizable(False, False)
    newWindow.configure(background='')
    templabel = Label(newWindow, width=19,
                      text="Select second operand: ", bg='#010329', fg='white')
    templabel.grid(row=0, column=0)
    btn1 = Button(newWindow, text="Reg", height=2, width=18,
                  command=lambda: sub_createFormUni("Reg"), bg='#010329', fg='white')
    btn1.grid(row=1, column=0, rowspan=1)
    btn2 = Button(newWindow, text="Mem", height=2, width=18,
                  command=lambda: sub_createFormUni("Mem"), bg='#010329', fg='white')
    btn2.grid(row=2, column=0, rowspan=1)
    btn3 = Button(newWindow, text="Value", height=2, width=18,
                  command=lambda: sub_createFormUni("Value"), bg='#010329', fg='white')
    btn3.grid(row=3, column=0, rowspan=1)


def initializer():
    # opcode display
    mylabel = Label(window, text="MACHINE CODE GENERATOR", font=(
        'TIMESNEWROMAN 14 bold italic'), relief="raised", bd=2, foreground=headercolor, background=textbackground)
    mylabel.place(x=65, y=375)
    global opcodegen
    opcodegen = Label(window, font=('TimesNewRoman 10 bold'),
                      background="black", fg="white", width=31)
    opcodegen.place(x=75, y=450)
    # mem code
    mlabel = Label(window, bd=2, height=2, width=20, relief="raised", text="MEMORY LOCATIONS", font=(
        'TimesNewRoman 14 bold italic'), foreground=headercolor, background=textbackground)
    mlabel.place(x=1105, y=525)
    ml1 = Label(window, borderwidth=3, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[0] + ": " + Mem_Values[0])
    ml1.place(x=935, y=635)

    ml2 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[1] + ": " + Mem_Values[1])
    ml2.place(x=1080, y=635)

    ml3 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[2] + ": " + Mem_Values[2])
    ml3.place(x=1225, y=635)

    ml4 = Label(window, bd=2, width=12, relief="ridge", height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[3] + ": " + Mem_Values[3])
    ml4.place(x=1370, y=635)

    ml5 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[4] + ": " + Mem_Values[4])
    ml5.place(x=935, y=695)

    ml6 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[5] + ": " + Mem_Values[5])
    ml6.place(x=1080, y=695)

    ml7 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[6] + ": " + Mem_Values[6])
    ml7.place(x=1225, y=695)

    ml8 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[7] + ": " + Mem_Values[7])
    ml8.place(x=1370, y=695)

    ml9 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                foreground=buttontextbackground, background=buttoncolor, text=Mems[8] + ": " + Mem_Values[8])
    ml9.place(x=935, y=755)

    ml10 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[9] + ": " + Mem_Values[9])
    ml10.place(x=1080, y=755)

    ml11 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[10] + ": " + Mem_Values[10])
    ml11.place(x=1225, y=755)

    ml12 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[11] + ": " + Mem_Values[11])
    ml12.place(x=1370, y=755)

    ml13 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[12] + ": " + Mem_Values[12])
    ml13.place(x=935, y=815)

    ml14 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[13] + ": " + Mem_Values[13])
    ml14.place(x=1080, y=815)

    ml15 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[14] + ": " + Mem_Values[14])
    ml15.place(x=1225, y=815)

    ml16 = Label(window, relief="ridge", bd=2, width=12, height=2, font=('TimesNewRoman 11 bold'),
                 foreground=buttontextbackground, background=buttoncolor, text=Mems[15] + ": " + Mem_Values[15])
    ml16.place(x=1370, y=815)
    global Meg_labels
    Meg_labels = [ml1, ml2, ml3, ml4, ml5, ml6, ml7,
                  ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16]

    # reg code
    labl = Label(window, relief="raised", bd=2, text="REGISTERS", width=20, height=2, font=(
        'TimesNewRoman 14 bold italic'), foreground=headercolor, background=textbackground)
    labl.place(x=1100, y=110)
    l0 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[0] + " : " + Reg_Values[0])
    l0.place(x=965, y=235)
    l1 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[1] + " : " + Reg_Values[1])
    l1.place(x=1155, y=235)
    l2 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[2] + " : " + Reg_Values[2])
    l2.place(x=1325, y=235)
    l3 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[3] + " : " + Reg_Values[3])
    l3.place(x=965, y=315)
    l4 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[4] + " : " + Reg_Values[4])
    l4.place(x=1155, y=315)
    l5 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[5] + " : " + Reg_Values[5])
    l5.place(x=1325, y=315)
    l6 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[6] + " : " + Reg_Values[6])
    l6.place(x=1055, y=385)
    l7 = Label(window, relief="ridge", bd=2, height=2, width=13, font=('TimesNewRoman 12 bold '),
               foreground=buttontextbackground, background=buttoncolor, text=Registers[7] + " : " + Reg_Values[7])
    l7.place(x=1230, y=385)
    global reg_labels
    reg_labels = [l0, l1, l2, l3, l4, l5, l6, l7]
    # button code
    newLabel = Label(window, relief="raised", bd=2, height=2, width=20, text="8086 COMMANDS", font=(
        'TimesNewRoman 14 bold italic '), foreground=headercolor, background=textbackground)
    newLabel.place(x=463, y=213)

    button16 = Button(window, bd=5, relief="raised", cursor='cross', text="MOV",
                      height=2, width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: mov())
    button16.place(x=440, y=300)
    button1 = Button(window, bd=5, relief="raised", cursor='cross', text="DIV",
                     height=2, activebackground='#9B8B91', width=12, font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: div_formselect())
    button1.place(x=590, y=300)
    button2 = Button(window, bd=5, relief="raised", cursor='cross', text="MUL",
                     height=2, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, width=12, command=lambda: mul_formselect())
    button2.place(x=440, y=370)
    button3 = Button(window, bd=5, relief="raised", cursor='cross', text="ADD", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: add())
    button3.place(x=590, y=370)
    button4 = Button(window, bd=5, relief="raised", cursor='cross', text="CDQ", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: cdq())
    button4.place(x=440, y=440)
    button5 = Button(window, bd=5, relief="raised", cursor='cross', text="XCHG", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: xchg_createFormBi())
    button5.place(x=590, y=440)
    button6 = Button(window, bd=5, relief="raised", cursor='cross', text="SUB", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: sub())
    button6.place(x=440, y=510)
    button7 = Button(window, bd=5, relief="raised", cursor='cross', text="INC", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: inc())
    button7.place(x=590, y=510)
    button8 = Button(window, bd=5, relief="raised", cursor='cross', text="DEC", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: dec())
    button8.place(x=440, y=580)
    button9 = Button(window, bd=5, relief="raised", cursor='cross', text="AND", height=2,
                     width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: AND_createFormBi())
    button9.place(x=590, y=580)
    button10 = Button(window, bd=5, relief="raised", cursor='cross', text="OR", height=2,
                      width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: OR_createFormBi())
    button10.place(x=440, y=650)
    button11 = Button(window, bd=5, relief="raised", cursor='cross', text="NOT", height=2,
                      width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: Not_())
    button11.place(x=590, y=650)
    button12 = Button(window, bd=5, relief="raised", cursor='cross', text="XOR", height=2,
                      width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: XOR_createFormBi())
    button12.place(x=440, y=720)
    button13 = Button(window, bd=5, relief="raised", cursor='cross', activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, text="SHR", height=2,
                      width=12, command=lambda: shr_createFormBi())
    button13.place(x=590, y=720)
    button14 = Button(window, bd=5, relief="raised", cursor='cross', text="SHL", height=2,
                      width=12, activebackground='#9B8B91', font=('TimesNewRoman 12 bold '), foreground=buttontextbackground, background=buttoncolor, command=lambda: shl_createFormBi())
    button14.place(x=515, y=795)


initializer()
mainloop()
