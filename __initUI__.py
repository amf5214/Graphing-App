import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QGridLayout
from PyQt5.QtWidgets import QFileDialog, QFrame, QMainWindow, QTableView
from fn_cat import *

"""
This is the __initUI__.py script that creates the entire UI within the App class. This script is 
dependent on the fn_cat.py script, which creates the visual elements. The main.py script is dependent
on this script. Also, this script relies on two .png items, ENSURE THAT YOU HAVE THEM IN THE SAME FILE
"""

run = 1
title = ''

lg.basicConfig(filename='app.log',
               level=lg.INFO,
               format='%(levelname)s : %(asctime)s : %(message)s',
               filemode='w')


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.setWindowTitle('Data Graphing App')
        self.setWindowIcon(QIcon('window_icon1.png'))

        self.startup()
        self.show()

    def setup(self):
        lg.info('setup ran')
        self.primary = QFrame(self)
        self.setCentralWidget(self.primary)
        self.grid = QGridLayout(self.primary)
        pic_label(self)
        self.sc = MplCanvas()
        self.run2 = 0
        self.run3 = 0
        self.run4 = 0
        self.run5 = 0
        self.state = 0

    def scr_clr_v(self):
        lg.info('scr_clr_v ran')
        while self.grid2.count():
            item = self.grid2.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


    def scr_clr_h(self):
        lg.info('scr_clr_h ran')
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())

    def startup(self):
        lg.info('startup ran')
        self.setGeometry(200, 200, 200, 350)
        all_functs(self)
        self.grid.addWidget(self.clean, 5, 0, 2, 5)
        self.grid.addWidget(self.proceed, 7, 0, 2, 5)
        self.grid.addWidget(self.about, 9, 0, 2, 5)

    def clean_prep(self):
        lg.info('clean_prep has been run because the clean data button has been clicked')
        self.scr_clr_h()
        self.data_clean()

    def run(self):
        lg.info('run has been run because the start button has been clicked')
        self.scr_clr_h()
        self.main()

    def main(self):
        lg.info('main ran')
        self.run7 = 1
        self.run8 = 0
        self.y_axis_select.activated[str].connect(self.y_set)
        self.setGeometry(200, 200, 500, 900)
        self.main_secondary = QFrame(self.primary)
        self.grid.addWidget(self.main_secondary, 2, 0, 18, 1)
        self.grid2 = QGridLayout(self.main_secondary)

        self.grid.addWidget(self.btn1, 0, 1, 1, 8)
        self.grid.addWidget(self.set_title, 0, 9, 1, 8)
        self.grid.addWidget(self.graph_slt, 1, 0)
        self.grid.addWidget(self.trend, 0, 17, 1, 8)
        self.grid.addWidget(self.graph_btn, 20, 0)
        self.grid.addWidget(self.save, 0, 25, 1, 8)
        self.grid.addWidget(self.menu, 0, 33, 1, 8)
        self.grid.addWidget(self.sc, 1, 1, 20, 40)

        self.file_name_lab = QLabel()
        self.file_name_lab.setFont(QFont('Times', 10))

    def take_input(self, select):
        global selection
        selection = select

    def data_clean(self):
        lg.info('data_clean ran')
        self.run7 = 0
        self.y_axis_select.activated[str].connect(self.col_drop)
        self.y_axis_select.clear()
        self.y_axis_select.addItem('Select a column to drop')
        self.state = 0
        self.grid.addWidget(self.btn1, 0, 1, 1, 11)
        self.grid.addWidget(self.info, 0, 12, 1, 8)
        self.grid.addWidget(self.prep, 0, 20, 1, 10)
        self.grid.addWidget(self.reset, 0, 30, 1, 10)
        self.grid.addWidget(self.menu, 0, 40, 1, 10)
        self.grid.addWidget(self.y_axis_select, 1, 0)
        self.view = QTableView()
        self.grid.addWidget(self.view, 1, 1, 25, 50)

    def prep_data(self):
        global filename_csv, file_sum, file_orig
        lg.info('prep_data ran')
        try:
            if selection == 'Summary':
                filename_csv_summ = file_sum.describe()
                filename_csv_summ['index'] = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
                pa = filename_csv_summ[filename_csv_summ.columns[filename_csv_summ.columns == 'index']]
                pb = filename_csv_summ[filename_csv_summ.columns[filename_csv_summ.columns != 'index']]
                file_sum = pd.concat([pa, pb], axis=1)
                # filename_csv = file_summary
                model = PandasModel(file_sum)
                self.state = 1
            else:
                model = PandasModel(file_orig)
                file_csv_mod = filename_csv
                self.state = 2

            self.view.setModel(model)
            for x in range(0, len(filename_csv.keys())):
                self.view.resizeColumnToContents(x)
        except NameError:
            QMessageBox.warning(self, 'Error', 'First select the file and the data to view')

    def col_drop(self, col):
        global file_sum, file_orig
        lg.info('col_drop ran')
        if self.state == 0:
            QMessageBox.warning(self, 'Error', 'First create the table')
            return
        if self.state == 1:
            file_sum = file_sum.drop(columns=col)
        elif self.state == 2:
            file_orig = file_orig.drop(columns=col)

    def bin_set(self, text1):
        lg.info('bin_set ran')

        global bin_count
        if type(int(text1)) != int:
            bin_count = 5
        else:
            bin_count = int(text1)

    def reset_chart_data(self):
        global file_orig, file_sum
        lg.info('reset_chart_data ran')

        file_orig = filename_csv
        file_sum = filename_csv

    def graph_type_selection(self, text):
        global graph_type_selected, bin_input_list
        lg.info('graph_type_selection ran')
        bin_input_list = []
        graph_type_selected = text
        self.run5 += 1

        self.scr_clr_v()
        btn_crtn_vlay(self)
        self.pull_columns()
        self.add_widget(text)

    def add_widget(self, text):
        lg.info('add_widget ran')
        if text == 'Bar Graph':
            self.grid2.addWidget(self.x_axis_select, 0, 0)
            self.grid2.addWidget(self.y_axis_select, 1, 0)
            self.grid2.addWidget(self.y_var_mod, 2, 0)
        elif text == 'Line Graph':
            self.grid2.addWidget(self.x_axis_select, 0, 0)
            self.grid2.addWidget(self.y_axis_select, 1, 0)
            self.grid2.addWidget(self.y_var_mod, 2, 0)
        elif text == 'Scatter Plot':
            self.grid2.addWidget(self.x_axis_select, 0, 0)
            self.grid2.addWidget(self.y_axis_select, 1, 0)
            self.grid2.addWidget(self.y_var_mod, 2, 0)
        elif text == 'Histogram':
            self.grid2.addWidget(self.x_axis_select, 0, 0)
            self.grid2.addWidget(self.bin_lab, 1, 0)
            self.grid2.addWidget(self.bin_input, 2, 0)

    def y_data_change(self, text):
        global y_g_type
        lg.info('y_data_change ran')
        y_g_type = text
        self.run4 += 1
        lg.info('the y data modifier has been run')

    def exit(self):
        lg.info('exit has been run because the exit button was pushed')
        self.scr_clr_h()
        self.setup()
        self.resize(300, 500)
        self.setWindowTitle('Data Graphing App')
        self.startup()

    def x_set(self, text):
        global x
        lg.info('x_set ran')
        x = text
        self.run2 += 1
        lg.info('x has been set')

    def y_set(self, text):
        global y
        lg.info('y_set ran')
        y = text
        self.run3 += 1
        lg.info('y has been set')

    def file_select(self):
        lg.info('file_select ran')
        global filename_csv, filename, file_orig, file_sum
        filename, all_columns = QFileDialog.getOpenFileName()
        if filename:
            filename_csv = pd.read_csv(filename, sep=',')
            lg.info('the drop na method has been run on the dataframe')
            filename_csv = filename_csv.dropna(how='any')
            self.run8 = 1
        else:
            QMessageBox.critical(self, 'ERROR', 'No file was selected')
            lg.error('The user did not select a file')
            return
        self.x_axis_select.clear()
        self.y_axis_select.clear()
        file_orig = filename_csv
        file_sum = filename_csv
        self.run2 = 0
        self.run3 = 0
        self.run4 = 0
        self.run5 = 0

        self.setWindowTitle('Data Graphing App - ' + filename.split(sep='/')[-1])

        self.pull_columns()

    def pull_columns(self):
        global filename_csv, filename, file_orig, file_sum
        lg.info('pull_columns ran')
        keys = list(filename_csv.keys())
        if self.run7 == 0:
            self.y_axis_select.addItem('Select a column to drop')
        for xvar in keys:
            self.x_axis_select.addItem(xvar)
        for yvar in keys:
            self.y_axis_select.addItem(yvar)

    def title_selection(self):
        global title
        lg.info('title_selection ran')
        title, done1 = QInputDialog.getText(self, 'Input data', 'What will the title be of the graph?')

    def about_app(self):
        QMessageBox.about(self, 'About', tot_about)
        lg.info('about ran')

    def graph(self):
        global run, x, y
        lg.info('graph ran')
        self.sc.axes.clear()
        self.sc.axes.set_title(title)
        self.sc.fig.tight_layout()

        if self.run8 != 1:
            QMessageBox.critical(self, 'Error', 'Select a csv file')
            lg.error('user skipped the select file button')
            return
        else:
            if self.run5 == 0:
                QMessageBox.warning(self, 'Error', 'Select a graph type')
                lg.warning('user skipped the select graph type box')
                return
            else:
                if graph_type_selected == 'Histogram':
                    if self.run2 == 0:
                        QMessageBox.warning(self, 'Error', 'Make Sure to select an X-Axis')
                        lg.warning('user skipped the select x axis box')
                        return
                    else:
                        self.sc.axes.set_xlabel(x)
                        self.do_graph()

                else:
                    if self.run2 == 0 and self.run3 == 0:
                        QMessageBox.warning(self, 'Error', 'Make Sure to select an X-Axis and a Y-Axis')
                        lg.warning('user skipped the x and y select boxes')
                        return
                    elif self.run2 == 0:
                        QMessageBox.warning(self, 'Error', 'Make Sure to select an X-Axis')
                        lg.warning('user skipped the select x axis box')
                        return
                    elif self.run3 == 0:
                        QMessageBox.warning(self, 'Error', 'Make sure to Select a Y-Axis')
                        lg.warning('user skipped the select y axis box')
                        return
                    elif self.run4 == 0:
                        QMessageBox.warning(self, 'Error', 'Select how you want to graph your data')
                        lg.warning('user skipped the select y data manipulation box')
                        return
                    else:
                        self.sc.axes.set_xlabel(x)
                        self.do_graph()

    def do_graph(self):
        lg.info('graph and do_graph ran because the graph button was pushed')
        global x, y
        if graph_type_selected == 'Bar Graph':
            self.sc.axes.set_ylabel(y)
            self.remove_na_text()
            if y_g_type == 'Cummulative Max':
                self.sc.axes.bar(filename_csv[x], filename_csv[y].cummax())
            elif y_g_type == 'Cummulative Sum':
                self.sc.axes.bar(filename_csv[x], filename_csv[y].cumsum())
            elif y_g_type == 'Cummulative Min':
                self.sc.axes.bar(filename_csv[x], filename_csv[y].cummin())
            elif y_g_type == 'Cummulative Product':
                self.sc.axes.bar(filename_csv[x], filename_csv[y].cumprod())
            else:
                self.sc.axes.bar(filename_csv[x], filename_csv[y])

            self.data_check()

        elif graph_type_selected == 'Line Graph':
            self.sc.axes.set_ylabel(y)
            self.remove_na_text()
            if y_g_type == 'Cummulative Max':
                self.sc.axes.plot(filename_csv[x], filename_csv[y].cummax())
            elif y_g_type == 'Cummulative Sum':
                self.sc.axes.plot(filename_csv[x], filename_csv[y].cumsum())
            elif y_g_type == 'Cummulative Min':
                self.sc.axes.plot(filename_csv[x], filename_csv[y].cummin())
            elif y_g_type == 'Cummulative Product':
                self.sc.axes.plot(filename_csv[x], filename_csv[y].cumprod())
            else:
                self.sc.axes.plot(filename_csv[x], filename_csv[y])

            self.data_check()

        elif graph_type_selected == 'Histogram':
            self.sc.axes.hist(x=filename_csv[x], bins=bin_count)

            self.data_check()

        elif graph_type_selected == 'Scatter Plot':
            self.sc.axes.set_ylabel(y)
            self.remove_na_text()
            if y_g_type == 'Cummulative Max':
                self.sc.axes.scatter(filename_csv[x], filename_csv[y].cummax())
            elif y_g_type == 'Cummulative Sum':
                self.sc.axes.scatter(filename_csv[x], filename_csv[y].cumsum())
            elif y_g_type == 'Cummulative Min':
                self.sc.axes.scatter(filename_csv[x], filename_csv[y].cummin())
            elif y_g_type == 'Cummulative Product':
                self.sc.axes.scatter(filename_csv[x], filename_csv[y].cumprod())
            else:
                self.sc.axes.scatter(filename_csv[x], filename_csv[y])

            self.data_check()

        else:
            return

    def data_check(self):
        global x, y, filename_csv
        lg.info('data_check ran')
        self.sc.fig.tight_layout()
        if graph_type_selected in ['Scatter', 'Line Graph', 'Bar Graph']:
            if type(filename_csv[x][0]) == str:
                self.sc.fig.autofmt_xdate(rotation=70)
            if type(filename_csv[y][0]) == str:
                self.sc.fig.autofmt_ydate(rotation=70)
        else:
            if type(filename_csv[x][0]) == str:
                self.sc.fig.autofmt_xdate(rotation=70)
        self.sc.draw()

    def remove_na_text(self):
        global filename_csv, y
        lg.info('the dataframe has been cleaned')
        filename_csv = filename_csv[pd.to_numeric(filename_csv[y], errors='coerce').notnull()]
        filename_csv[y] = filename_csv[y].astype(float)

    def save_graph(self):
        self.sc.fig.savefig('Graph.svg')
        lg.warning('the graph has been saved')


p1_ab = 'This app takes a csv file and allows you too analyze it by'
p2_ab = ' generating charts and graphs. Also, you can modify the data. \n \n By: Austin Fraley.'
tot_about = p1_ab + p2_ab
