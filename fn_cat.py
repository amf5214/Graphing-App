from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
import PyQt5.QtCore as Qtc
from PyQt5.QtCore import QAbstractTableModel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import logging as lg

"""
This file creates the visual elements of the App class and there are
two files that depend on it, main.py and __initUI__.py
"""


def all_functs(self):
    lg.info('all_functs ran')

    self.btn1 = QPushButton('Select File')
    self.btn1.setFont(QFont('Times', 15))

    self.set_title = QPushButton('Set Graph Title')
    self.set_title.setFont(QFont('Times', 15))

    self.x_axis_select = QComboBox()
    self.x_axis_select.addItem('Select the X Axis')
    self.x_axis_select.setFont(QFont('Times', 15))

    self.trend = QPushButton('Add a trendline')
    self.trend.setFont(QFont('Times', 15))

    self.info = QComboBox()
    self.info.addItem('Select the data to view?')
    self.info.addItem('Raw Data')
    self.info.addItem('Summary')
    self.info.setFont(QFont('Times', 15))

    self.y_axis_select = QComboBox()
    self.y_axis_select.addItem('Select the Y Axis')
    self.y_axis_select.setFont(QFont('Times', 15))

    self.proceed = QPushButton('Start Graphing')
    self.proceed.setFont(QFont('Times', 15))

    self.reset = QPushButton('Reset Data')
    self.reset.setFont(QFont('Times', 15))

    self.clean = QPushButton('Clean Data')
    self.clean.setFont(QFont('Times', 15))

    self.prep = QPushButton('Create Table')
    self.prep.setFont(QFont('Times', 15))

    self.about = QPushButton('About')
    self.about.setFont(QFont('Times', 15))

    self.graph_slt = QComboBox()
    self.graph_slt.addItem('Bar Graph')
    self.graph_slt.addItem('Line Graph')
    self.graph_slt.addItem('Scatter Plot')
    self.graph_slt.addItem('Histogram')
    self.graph_slt.setFont(QFont('Times', 15))

    self.save = QPushButton('Save Graph')
    self.save.setFont(QFont('Times', 15))

    self.menu = QPushButton('Exit')
    self.menu.setFont(QFont('Times', 15))

    self.graph_btn = QPushButton('Graph')
    self.graph_btn.setFont(QFont('Times', 15))

    self.y_var_mod = QComboBox()
    self.y_var_mod.addItem('Select the y data modifier?')
    self.y_var_mod.addItem('Raw Y Data')
    self.y_var_mod.addItem('Cummulative Sum')
    self.y_var_mod.addItem('Cummulative Max')
    self.y_var_mod.addItem('Cummulative Min')
    self.y_var_mod.addItem('Cummulative Product')
    self.y_var_mod.setFont(QFont('Times', 15))

    self.bin_input = QLineEdit()
    self.bin_input.setFont(QFont('Times', 15))
    self.bin_input.setText('Bin #')

    self.bin_lab = QLabel()
    self.bin_lab.setText('How many bins would you like?')
    self.bin_lab.setFont(QFont('Times', 15))

    self.btn1.clicked.connect(self.file_select)
    self.set_title.clicked.connect(self.title_selection)
    self.x_axis_select.activated[str].connect(self.x_set)
    self.info.activated[str].connect(self.take_input)
    self.proceed.clicked.connect(self.run)
    self.reset.clicked.connect(self.reset_chart_data)
    self.clean.clicked.connect(self.clean_prep)
    self.prep.clicked.connect(self.prep_data)
    self.about.clicked.connect(self.about_app)
    self.graph_slt.activated[str].connect(self.graph_type_selection)
    self.save.clicked.connect(self.save_graph)
    self.menu.clicked.connect(self.exit)
    self.graph_btn.clicked.connect(self.graph)
    self.y_var_mod.activated[str].connect(self.y_data_change)
    self.bin_input.textChanged.connect(self.bin_set)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, width=500, height=900, dpi=150):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)


class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qtc.Qt.DisplayRole):
        if index.isValid():
            if role == Qtc.Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qtc.Qt.Horizontal and role == Qtc.Qt.DisplayRole:
            return self._data.columns[col]
        return None


def btn_crtn_vlay(self):
    lg.info('btn_crtn_vlay ran')
    self.x_axis_select = QComboBox()
    self.x_axis_select.addItem('Select the X Axis')
    self.x_axis_select.setFont(QFont('Times', 15))
    self.x_axis_select.activated[str].connect(self.x_set)

    self.y_var_mod = QComboBox()
    self.y_var_mod.addItem('Select the y data modifier?')
    self.y_var_mod.addItem('Raw Y Data')
    self.y_var_mod.addItem('Cummulative Sum')
    self.y_var_mod.addItem('Cummulative Max')
    self.y_var_mod.addItem('Cummulative Min')
    self.y_var_mod.addItem('Cummulative Product')
    self.y_var_mod.setFont(QFont('Times', 15))
    self.y_var_mod.activated[str].connect(self.y_data_change)

    self.y_axis_select = QComboBox()
    self.y_axis_select.addItem('Select the Y Axis')
    self.y_axis_select.setFont(QFont('Times', 15))
    self.y_axis_select.activated[str].connect(self.y_set)

    self.bin_input = QLineEdit()
    self.bin_input.setFont(QFont('Times', 15))
    self.bin_input.setText('Bin #')
    self.bin_input.textChanged.connect(self.bin_set)

    self.bin_lab = QLabel()
    self.bin_lab.setText('How many bins would you like?')
    self.bin_lab.setFont(QFont('Times', 15))


def pic_label(self):
    pic = QLabel(self)
    pixmap = QPixmap('window_icon2.png')
    pic.setPixmap(pixmap)
    pic.setAlignment(Qtc.Qt.AlignCenter)
    self.grid.addWidget(pic, 0, 0, 5, 3)
    lg.info('pic_label ran')
