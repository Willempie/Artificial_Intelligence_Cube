## Dick Bruin, 01/03/2014
## Genetic search demo

from Tkinter import *
from random import randint, uniform
from math import floor, cos, sin, exp, pi

class GUIBuilder:
    mainwindow = None
    
    def __init__(self, padx=1, pady=1):
        self.padx = padx
        self.pady = pady
        if GUIBuilder.mainwindow == None:
            GUIBuilder.mainwindow = Tk()
            GUIBuilder.mainwindow.protocol("WM_DELETE_WINDOW", self.stop)
        
    def start(self):
        GUIBuilder.mainwindow.mainloop()

    def stop(self):
        GUIBuilder.mainwindow.destroy()
        GUIBuilder.mainwindow.quit()

    def mainWindow(self, title, vResize=False, hResize=False):
        result = GUIBuilder.mainwindow
        result.title(title)
        result.resizable(width=hResize, height=vResize)
        return result

    def toplevel(self, title, vResize=False, hResize=False):
        result = Toplevel()
        result.title(title)
        result.resizable(width=hResize, height=vResize)
        result.protocol("WM_DELETE_WINDOW", lambda:result.withdraw())
        return result

    def frame(self, parent, row, col, vResize=False, hResize=False):
        result = Frame(parent)
        result.isGUIBuilderFrame = True
        self.setPos(parent, result, row, col, vResize, hResize)
        return result

    def button(self, parent, caption, command, row, col, vResize=False, hResize=False):
        result = Button(parent, text=caption, command=command)
        self.setPos(parent, result, row, col, vResize, hResize)
        return result

    def checkbutton(self, parent, caption, state, row, col, vResize=False, hResize=False):
        iv = IntVar()
        iv.set(state)
        result = Checkbutton(parent, text=caption, variable=iv)
        self.setPos(parent, result, row, col, vResize, hResize)
        return (result, iv)

    def label(self, parent, caption, row, col, vResize=False, hResize=False):
        sv = StringVar()
        sv.set(caption)
        result = Label(parent, textvariable=sv)
        self.setPos(parent, result, row, col, vResize, hResize)
        return (result, sv)

    def entry(self, parent, caption, width, row, col, vResize=False, hResize=False):
        sv = StringVar()
        sv.set(caption)
        result = Entry(parent, textvariable=sv, width=width)
        self.setPos(parent, result, row, col, vResize, hResize)
        return (result, sv)

    def optionMenu(self, parent, optionList, row, col, vResize=False, hResize=False):
        sv = StringVar()
        sv.set(optionList[0])
        result = OptionMenu(parent, sv, *optionList)
        result.config(width=max(len(option) for option in optionList))
        self.setPos(parent, result, row, col, vResize, hResize)
        return (result, sv)

    def canvas(self, parent, width, height, row, col, vResize=False, hResize=False):
        result = Canvas(parent, width=width, height=height)
        self.setPos(parent, result, row, col, vResize, hResize)
        return result

    def listbox(self, parent, width, height, row, col, vResize=False, hResize=False):
        frame = self.frame(parent, row, col, vResize, hResize)
        result = Listbox(frame, width=width, height=height, selectmode=MULTIPLE)
        vscroller = Scrollbar(frame, orient=VERTICAL, command=result.yview)
        result.config(yscrollcommand=vscroller.set)
        self.setPos(frame, result, 0, 0, vResize, hResize)
        self.setPos(frame, vscroller, 0, 1)
        return result

    def text(self, parent, width, height, row, col, vResize=False, hResize=False):
        frame = self.frame(parent, row, col, vResize, hResize)
        result = Text(frame, width=width, height=height, wrap=NONE)
        hscroller = Scrollbar(frame, orient=HORIZONTAL, command=result.xview)
        vscroller = Scrollbar(frame, orient=VERTICAL, command=result.yview)
        result.config(xscrollcommand=hscroller.set, yscrollcommand=vscroller.set)
        self.setPos(frame, result, 0, 0, vResize, hResize)
        self.setPos(frame, hscroller, 1, 0)
        self.setPos(frame, vscroller, 0, 1)
        return result

    def tableInput(self, parent, labels, row, col, vResize=False, hResize=False):
        svs = []
        frame = self.frame(parent, row, col, vResize, hResize)
        for k in range(len(labels)):
            self.label(frame, labels[k][0], k, 0)
            options = labels[k][1]
            if len(options) == 0:
                res = self.entry(frame, '', 10, k, 1, False, True)
            elif len(options) == 1:
                res = self.entry(frame, options[0], 10, k, 1, False, True)
            else:
                res = self.optionMenu(frame, options, k, 1, False, True)
            svs.append(res[1])
        return svs

    def menubar(self, parent):
        result = Menu()
        parent.config(menu=result)
        return result

    def menu(self, parent, caption):
        result = Menu()
        parent.add_cascade(label=caption, menu=result)
        return result

    def menuItem(self, parent, caption, command):
        parent.add_command(label=caption, command=command)

    def menuCheckbutton(self, parent, caption, state):
        iv = IntVar()
        iv.set(state)
        parent.add_checkbutton(label=caption, variable=iv)
        return iv

    def menuSeparator(self, parent):
        parent.add_separator()

    def setPos(self, parent, widget, row, col, vResize=False, hResize=False):
        if vResize: parent.rowconfigure(row, weight=1)
        if hResize: parent.columnconfigure(col, weight=1)
        try:
            if widget.isGUIBuilderFrame:
                widget.grid(row=row, column=col, sticky=N+S+W+E)
            else:
                widget.grid(row=row, column=col, padx=self.padx, pady=self.pady, sticky=N+S+W+E)
        except:
                widget.grid(row=row, column=col, padx=self.padx, pady=self.pady, sticky=N+S+W+E)
        return widget

def ga():
    class Self:
        def __init__(self):
            self.w     = 600
            self.h     = 600
            self.size  = 150
            self.pop   = []
            self.steps = 0

    class Rect:
        def __init__(self, rect):
            self.rect  = rect
            self.value = 0
            self.color = 'white'
    
    self = Self()        

    gui = GUIBuilder()
    self.mainWindow = gui.mainWindow('genetic search')
    
    self.canvas = gui.canvas(self.mainWindow, self.w+1, self.h+1, 0, 0)  

    frame = gui.frame(self.mainWindow, 1, 0)
    gui.button(frame, 'init', lambda:init(self), 0, 0)
    self.popEntry = gui.entry(frame, '10', 3, 0, 1)[1]
    gui.button(frame, 'search', lambda:search(self), 0, 2)
    self.stepsEntry = gui.entry(frame, '50', 3, 0, 3)[1]
    gui.label(frame, 'mixes', 0, 4)
    self.nrMixesEntry = gui.entry(frame, '10', 3, 0, 5)[1]
    gui.label(frame, 'mutants', 0, 6)
    self.nrMutantsEntry = gui.entry(frame, '10', 3, 0, 7)[1]

    dx = self.w / self.size
    dy = self.h / self.size
    self.rects = [[Rect(self.canvas.create_rectangle(x*dx+1, y*dy+1, (x+1)*dx+1, (y+1)*dy+1)) for y in range(self.size)] for x in range(self.size)]
    
    display(self)

    gui.start()

def display(self):
    minval, maxval = 10**6, -10**6
    for x in range(self.size):
        for y in range(self.size):
            val = terrain(x / (1.0 * self.size), y / (1.0 * self.size))
            if val < minval: minval = val
            if val > maxval: maxval = val
            self.rects[x][y].value = val
    for x in range(self.size):
        for y in range(self.size):
            val = int((self.rects[x][y].value - minval) / (maxval - minval) * 255)
            self.rects[x][y].color = '#00{0:02X}00'.format(val)
            self.canvas.itemconfigure(self.rects[x][y].rect, fill=self.rects[x][y].color, outline=self.rects[x][y].color)

def displayPop(self, visible):
    for x, y in self.pop:
        color = 'yellow' if visible else self.rects[x][y].color
        self.canvas.itemconfigure(self.rects[x][y].rect, fill=color, outline=color)        

def terrain(x, y):
    return 2.0 * (x**2 + y**2) - 1.0 * (1.0-cos(8.0*pi*(x-0.1*y))) * (1.0-cos(8.0*pi*(y-0.1*x)))

def init(self):
    displayPop(self, False)
    self.steps = 0
    popSize    = int(self.popEntry.get())
    self.pop   = [[randint(0, self.size-1) for l in range(2)] for k in range(popSize)]
    displayPop(self, True)

def search(self):
    self.steps     = int(self.stepsEntry.get())
    self.nrMixes   = int(self.nrMixesEntry.get())
    self.nrMutants = int(self.nrMutantsEntry.get())
    doSearch(self)

def doSearch(self):
    if self.steps > 0:
        displayPop(self, False)
        self.steps = self.steps - 1
        fitness    = lambda x,y:self.rects[x][y].value if 0 <= x and x < self.size and 0 <= y and y < self.size else 10**6
        self.pop   = evolution(fitness, self.pop, self.size, self.nrMixes, self.nrMutants) 
        displayPop(self, True)
        self.mainWindow.after(500, lambda:doSearch(self))

def evolution(fitness, pop, size, nrMixes, nrMutants):
    neighbors = [fittest(fitness, 1, [[x+dx, y+dy] for dx in [-1, 0, 1] for dy in [-1, 0, 1]])[0] for x, y in pop]
    mixes     = [[pop[randint(0, len(pop)-1)][0], pop[randint(0, len(pop)-1)][1]] for k in range(nrMixes)]
    mutants   = [[randint(0, size-1) for l in range(2)] for k in range(nrMutants)]
    return fittest(fitness, len(pop), neighbors + mixes + mutants)

def fittest(fitness, size, pop):
    return sorted(pop, key=lambda xy:fitness(xy[0], xy[1]))[0:size]

ga()
