import sys
import untitled
import json

from utils import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QSplitter, QHeaderView

class window(untitled.Ui_MainWindow):
    def setupUi(self, window):
        super().setupUi(window)
        self.pushButton.clicked.connect(self.change)
        #model = QtGui.QStandardItemModel()
        #self.treeView.setModel(model)
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setHeaderLabels(['条目', '内容', '', ''])
        #self.treeWidget.setWordWrap(True)
        self.treeWidget.setIndentation(0)
        self.label.setStyleSheet("border:1px solid grey;")
        self.label_2.setStyleSheet("border:1px solid grey;")
        self.label_3.setStyleSheet("border:1px solid grey;")
        #QMessageBox.information(self.centralwidget, "提示", "图片识别失败", QMessageBox.Yes)
        #self.treeWidget.ho
        #QSplitter.addWidget(QtWidgets.QWidget()).setLayout(self.verticalLayout)
        #self.treeWidget.setTextElideMode(3)
        #self.update()
    def change(self):
        self.label.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.treeWidget.clear()
        #self.update()
        #a = QMessageBox.information(self.centralwidget, "a", "b", QMessageBox.Yes | QMessageBox.No)


        print("UploadButton")
        imgName, imgType = QFileDialog.getOpenFileName(None, "选取文件夹","C:/")
        #QMessageBox.information(self.centralwidget, "提示", "图片识别失败")
        if imgName != '':
            print(imgName)

            res = upload(imgName)
            if res!='-1':
                print(res)
                if(res):
                    dict = json.loads(res)
                    self.update(dict)

                png = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
                png2url, png3url=ROI(imgName)
                png2 = QtGui.QPixmap(png2url)
                png3 = QtGui.QPixmap(png3url)
                self.label.setPixmap(png)
                self.label_2.setPixmap(png3)
                self.label_3.setPixmap(png2)
            else:
                QMessageBox.information(self.centralwidget, "提示", "图片识别失败", QMessageBox.Yes)

    def update(self, dict):
        #i = 0
        #i = self.tableWidget.rowCount()
        #dict = {"1":"1","2":"2",'att':{'name':'name','content':{'6':'6','7':'7'}},"3":"3","4":"4",'com' = [{'name':'com1', 'amount':'1.1'}] }
        #dict = {"seller":{"name":"1","content":{"registerNum":"410305012345678","address":"1·61168744498","bank":"1123455668-234222226111"}},"purchaser":{"name":"1","content":{"registerNum":"410305123456789","address":"181234567","bank":"1000012345678"}},"invoiceDate":"2018","commodity":[{"name":"1","amount":"5999.00"}],"invoiceCode":"1100094140","invoiceNum":"87654321","checkCode":""}

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
        #for key in dict:
        #    model = QtGui.QStandardItemModel()




        for key in dict:
            if type(dict[key]).__name__ != 'dict' and type(dict[key]).__name__ != 'list':
                self.insertFather(key, dict[key])
            elif type(dict[key]) == list:
                self.insertFather(key, '金额')
                self.insertCommodity(dict[key])
            else:
                #print(dict[key][0]['name'])
                self.insertFather(key, dict[key]['name'])
                #item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()-1))
                #item.setText(0, key)
                #item.setText(1, dict[key][0]['name'])
                #item1 = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()))
                #item1.setText(0, '1')
                #item1.setText(1, '11111')
                self.insertChilds(dict[key]['content'])

        #QHeaderView(self.treeWidget.header()).setSectionResizeMode(3)
        self.treeWidget.expandAll()

    def map(self, str):
        dict = {"seller":"开票方","registerNum":"纳税人识别号", "address":"地址","bank":"开户行账号", "purchaser":"收票方","invoiceDate":"开票日期","invoiceCode":"发票代码","invoiceNum":"发票号码","checkCode":"校验码","commodity":"开票内容","amounts":"开票金额","inWords":"大写","inFigures":"小写", "taxRate":"税率", "tax":"税额"}
        return dict[str]

    def insertFather(self, key, value):
        item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item.setForeground(0, QtGui.QColor(0, 125, 0))
        item.setFont(0, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Bold))
        item.setFont(1, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
        if key =="invoiceDate" and '2018' not in value:
            item.setForeground(0, QtGui.QColor(255, 0, 0))
            item.setForeground(1, QtGui.QColor(255, 0, 0))
        elif value == '':
            item.setForeground(0, QtGui.QColor(255, 0, 0))
        item.setText(0, self.map(key))
        item.setText(1, value)
        if(key == "commodity"):
            item.setText(2, '税率')
            item.setText(3, "税额")
            item.setFont(2, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
            item.setFont(3, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))

    def insertChilds(self, dict):
        #print('!!!')
        for key in dict:
            #print(key)
            item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()-1))
            item.setForeground(0, QtGui.QColor(0, 125, 0))
            item.setFont(0, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Bold))
            item.setFont(1, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
            if dict[key] =='':
                item.setForeground(0, QtGui.QColor(255, 0, 0))
            item.setText(0, self.map(key))
            item.setText(1, dict[key])
            item.setBackground(0, QtGui.QColor(233,233,233))
            item.setBackground(1, QtGui.QColor(233, 233, 233))
            item.setBackground(2, QtGui.QColor(233, 233, 233))
            item.setBackground(3, QtGui.QColor(233, 233, 233))
    def insertCommodity(self, list):
        #print(list)
        for i in range(len(list)):
            #print(i)
            #print(key)
            item = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(self.treeWidget.topLevelItemCount()-1))
            item.setText(0, list[i]['name'])
            item.setText(1, list[i]['amount'])
            item.setText(2, list[i]['taxRate'])
            item.setText(3, list[i]['tax'])
            item.setBackground(0, QtGui.QColor(233,233,233))
            item.setBackground(1, QtGui.QColor(233, 233, 233))
            item.setBackground(2, QtGui.QColor(233, 233, 233))
            item.setBackground(3, QtGui.QColor(233, 233, 233))
            item.setFont(0, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
            item.setFont(1, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
            item.setFont(2, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
            item.setFont(3, QtGui.QFont('微软雅黑', 14, QtGui.QFont.Normal))
            #print(list[i])
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    w.setWindowIcon(QtGui.QIcon("favicon.ico"))
    ui=window()
    ui.setupUi(w)
    #w.move(300, 300)
    w.setWindowTitle('2018年广联达暑期实习发票识别系统')
    #w.setCentralWidget(w)
    w.show()
    sys.exit(app.exec_())