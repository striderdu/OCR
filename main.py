import sys
import untitled
import json

from utils import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class window(untitled.Ui_MainWindow):
    def setupUi(self, window):
        super().setupUi(window)
        self.pushButton.clicked.connect(self.change)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Key', 'Value'])
        #self.update()
    def change(self):
        self.update()

        print("UploadButton")
        imgName, imgType = QFileDialog.getOpenFileName(None, "选取文件夹","C:/")
        print(imgName)

        res = upload(imgName)
        print(res)
        #if(res):
        #    dict = json.loads(res)
            #self.label_2.setText(str(dict1))
        #    self.update(dict)

        png = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)

    def update(self):
        #i = 0
        #i = self.tableWidget.rowCount()
        dict = {"1":"1","2":"2",'att':[{'name':'1','5':'5'}],"3":"3","4":"4"}
        '''
        for key in dict:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            print(self.tableWidget.rowCount())
            if type(dict[key])!=list:
                item1 = QtWidgets.QTableWidgetItem()
                item1.setText(key)
                item2 = QtWidgets.QTableWidgetItem()
                item2.setText(str(dict[key]))
            #print(key + ':' + dict[key])
            self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, item1)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, item2)
            #self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        '''
        for key in dict:
            if type(dict[key]) != list:
                print(key)
                self.insertFather(key, dict[key])
            else:
                #print(dict[key][0]['name'])
                self.insertFather(key, dict[key][0]['name'])
                #item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()-1))
                #item.setText(0, key)
                #item.setText(1, dict[key][0]['name'])
                #item1 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()))
                #item1.setText(0, '1')
                #item1.setText(1, '11111')
                self.insertChilds(dict[key])

    def insertFather(self, key, value):
        item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item.setText(0, key)
        item.setText(1, value)

    def insertChilds(self, list):
        #print('!!!')
        for key in list[0]:
            print(key)
            item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()-1))
            item.setText(0, key)
            item.setText(1, list[0][key])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui=window()
    ui.setupUi(w)
    #w.move(300, 300)
    w.setWindowTitle('TinySun')
    #w.setCentralWidget(w)
    w.show()
    sys.exit(app.exec_())