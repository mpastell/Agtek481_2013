import sys
from PySide.QtGui import *
import matplotlib
matplotlib.rcParams['backend.qt4']='PySide'
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib as mpl
from pylab import *


class Sincx(QDialog):
    def __init__(self, parent=None):
        super(Sincx, self).__init__(parent)

        self.setWindowTitle('Sin(x) and Cos(x)')

        #Buttons
        self.sinButton = QPushButton("Sinc(x)")
        self.cosButton = QPushButton("Cos(x)")

        #Button callback
        self.sinButton.clicked.connect(self.sinButtonClick)
        self.cosButton.clicked.connect(self.cosButtonClick)

        #Figure
        self.figure = plt.figure()
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.axis.hold(False)
        self.figure.set_facecolor('0.95')

        # Create a layout, add elements and set it as main window layout
        self.layout = QVBoxLayout()
        self.hlayout = QHBoxLayout()

        #Add buttons to horizontal layout
        self.hlayout.addWidget(self.sinButton)
        self.hlayout.addWidget(self.cosButton)
        
        #horizontal layout and canvas to vertical layout
        self.layout.addLayout(self.hlayout)
        self.layout.addWidget(self.canvas)
        
        #Set layout of the dialog itself
        self.setLayout(self.layout)


    #Callback for Sin(x) button
    def sinButtonClick(self):
        x = arange(0, 2*pi, 0.01)
        sx = sin(x)
        self.axis.plot(x, sx)
        self.canvas.draw()

    #Callback for Cos(x) button
    def cosButtonClick(self):
        x = arange(0, 2*pi, 0.01)
        cx = cos(x)
        self.axis.plot(x, cx)
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Sincx()
    window.show()
    sys.exit(app.exec_())