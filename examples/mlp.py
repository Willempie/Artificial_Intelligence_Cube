## Dick Bruin, 23/02/2014
## Multi layer perceptron demo

from Tkinter import *
from random import randint, uniform
from math import exp

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

def mlp():
    class Self:
        def __init__(self):
            self.w        = 600
            self.h        = 600
            self.size     = 50
            self.weights1 = []
            self.weights2 = []

    class Rect:
        def __init__(self, rect):
            self.rect  = rect
            self.color = 0
    
    self = Self()        

    gui = GUIBuilder()
    mainWindow = gui.mainWindow('multi layer perceptron')
    
    self.canvas = gui.canvas(mainWindow, self.w+1, self.h+1, 0, 0)  

    frame = gui.frame(mainWindow, 1, 0)
    gui.button(frame, 'clear', lambda:reset(self, 1), 0, 0)
    gui.button(frame, 'reset', lambda:reset(self, 4), 0, 1)
    self.color = gui.optionMenu(frame, ['white', 'red', 'green', 'blue'], 0, 2)[1]
    gui.label(frame, '', 0, 3, False, True)
    gui.button(frame, 'init' , lambda:init(self), 0, 4)
    gui.button(frame, 'learn', lambda:learn(self), 0, 5)
    self.hidden = gui.entry(frame, '10', 3, 0, 6)[1]
    self.epochs = gui.optionMenu(frame, ['1', '10', '100', '1000', '10000'], 0, 7)[1]

    dx = self.w / self.size
    dy = self.h / self.size
    self.rects = [[Rect(self.canvas.create_rectangle(x*dx+1, y*dy+1, (x+1)*dx+1, (y+1)*dy+1)) for y in range(self.size)] for x in range(self.size)]
    
    self.canvas.bind('<Button-1>', lambda event:mouseclick(self, event))

    display(self)
    init(self)

    gui.start()

def mouseclick(self, event):
    colors = ['white', 'red', 'green', 'blue']
    x = event.x * self.size / self.w
    y = event.y * self.size / self.h
    self.rects[x][y].color = [k for k in range(len(colors)) if colors[k] == self.color.get()][0]
    draw(self, x, y)
    
def draw(self, x, y):
    colors = ['white', 'dark red', 'dark green', 'dark blue', 'coral', 'light green', 'light blue']
    self.canvas.itemconfigure(self.rects[x][y].rect, fill=colors[self.rects[x][y].color])

def display(self):
    for x in range(self.size):
        for y in range(self.size):
            draw(self, x, y)

def reset(self, limit):
    for x in range(self.size):
        for y in range(self.size):
            if self.rects[x][y].color >= limit:
                self.rects[x][y].color = 0
                draw(self, x, y)
        
def init(self):
    self.weights1 = []
    self.weights2 = []

def learn(self):
    hidden = int(self.hidden.get())
    if hidden <= 0 or hidden >= 1000: return
    if len(self.weights1) <> hidden:
        self.weights1 = [[uniform(-1, 1) for l in range(1+2)] for k in range(hidden)]
        self.weights2 = [[uniform(-1, 1) for l in range(1+hidden)] for k in range(3)]
    outputs = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    epochs = int(self.epochs.get())
    for epoch in range(epochs):
        for k in range(self.size):
            for l in range(self.size):
                if self.rects[k][l].color in [1, 2, 3]:
                    train(self.weights1, self.weights2, [k / (1.0 * self.size), l / (1.0 * self.size)], outputs[self.rects[k][l].color-1])
    for k in range(self.size):
        for l in range(self.size):
            if not(self.rects[k][l].color in [1, 2, 3]):
                values0 = [k / (1.0 * self.size), l / (1.0 * self.size)]
                values1 = calc(self.weights1, values0)
                values2 = calc(self.weights2, values1)
                self.rects[k][l].color = 4 + [m for maxval in [max(values2)] for m in range(len(values2)) if values2[m] >= maxval][0]
    display(self)
    
def calc(weights, inputs):
    values = [1] + inputs
    outputs = [1 / (1 + exp(-sum(weights[k][l] * values[l] for l in range(len(values))))) for k in range(len(weights))]
    return outputs

def propagateErrors(weights, outputs, errors):
    return [sum(weights[l][1+k] * errors[l] for l in range(len(errors))) * outputs[k] * (1 - outputs[k]) for k in range(len(outputs))]

def adjustWeights(weights, inputs, errors):
    values = [1] + inputs
    for k in range(len(errors)):
        for l in range(len(values)):
            weights[k][l] = weights[k][l] + errors[k] * values[l]

def train(weights1, weights2, inputs, outputs):
    values1 = calc(weights1, inputs)
    values2 = calc(weights2, values1)
    errors2 = [0.25 * (outputs[k] - values2[k]) * values2[k] * (1 - values2[k]) for k in range(len(outputs))]
    errors1 = propagateErrors(weights2, values1, errors2)
    adjustWeights(weights2, values1, errors2)
    adjustWeights(weights1, inputs, errors1)
    
mlp()
