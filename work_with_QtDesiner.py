# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bama_test_aop.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import requests
from bs4 import BeautifulSoup
import re


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 472)
        self.brand = QtWidgets.QPushButton(Dialog)
        self.brand.setGeometry(QtCore.QRect(30, 20, 141, 32))
        self.brand.setObjectName("brand")

        self.brandlist = QtWidgets.QListWidget(Dialog)
        self.brandlist.setGeometry(QtCore.QRect(20, 60, 151, 181))
        self.brandlist.setObjectName("brandlist")

        self.model = QtWidgets.QPushButton(Dialog)
        self.model.setGeometry(QtCore.QRect(260, 30, 121, 21))
        self.model.setObjectName("model")

        self.modellist = QtWidgets.QListWidget(Dialog)
        self.modellist.setGeometry(QtCore.QRect(190, 60, 201, 181))
        self.modellist.setObjectName("modellist")

        self.result = QtWidgets.QTextBrowser(Dialog)
        self.result.setGeometry(QtCore.QRect(20, 250, 471, 201))
        self.result.setObjectName("result")

        self.munofresult = QtWidgets.QTextEdit(Dialog)
        self.munofresult.setGeometry(QtCore.QRect(400, 170, 91, 31))
        self.munofresult.setObjectName("munofresult")

        self.run = QtWidgets.QPushButton(Dialog)
        self.run.setGeometry(QtCore.QRect(390, 210, 113, 32))
        self.run.setObjectName("run")

        self.retranslateUi(Dialog)
        self.brand.clicked.connect(self.brandFunc)
        self.model.clicked.connect(self.modelFunc)
        self.run.clicked.connect(self.runFunc)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def brandFunc(self):
        app.processEvents()
        global url
        url = 'http://bama.ir/car/'
        global header
        header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
          'sec-fetch-user': '?1'}
        while True:
            try:
                response = requests.get(url, headers=header, timeout=3)
                break
            except:
                sleep(5)
                continue
        soup = BeautifulSoup(response.text, 'html.parser')
        brand_soup = soup.select('#selectedTopBrand')
        brand_soup = brand_soup[0]('option')
        global brand_list
        brand_list = []
        global brand_value
        brand_value = []
        for i in brand_soup:
            brand_list.append(i.get_text())
            brand_value.append(i['value'])
        brand_value = brand_value[1:]
        brand_list = brand_list[1:]
        for i in brand_list:
            self.brandlist.addItem(i)


    def modelFunc(self):
        app.processEvents()
        selected_brand = self.brandlist.selectedItems()
        selected_brand_text = selected_brand[0].text()
        global brand_value
        global brand_list
        conter = 0
        for i in brand_list:
            if i == selected_brand_text:
                i1 = conter
            conter += 1
        selected_brand_value = brand_value[i1]
        i2 = selected_brand_value.index(',')
        url_endpoint = selected_brand_value[i2+1:]
        global url
        global url_brand
        url_brand = url + url_endpoint
        global header
        while True:
            try:
                response = requests.get(url_brand, headers=header, timeout=3)
                break
            except:
                sleep(5)
                continue
        global models
        models = re.findall(r',([0-9a-zA-Z-]+)&quot;}', response.text)
        self.modellist.clear()
        for i in models:
            self.modellist.addItem(i)
        
        
        



    def runFunc(self):
        app.processEvents()
        selectec_models = self.modellist.selectedItems()
        selectec_models_text = selectec_models[0].text()
        global url_brand
        url_model = url_brand + '/' + selectec_models_text
        ads_num = self.munofresult.toPlainText()
        ads_num = int(ads_num)
        while True:
            try:
                response = requests.get(url_brand, headers=header, timeout=3)
                break
            except:
                sleep(5)
                continue
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.select('.persianOrder')
        counter = 0
        for i in title:
            if ads_num > counter:
                self.result.insertPlainText(i.get_text())





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.brand.setText(_translate("Dialog", "brand"))
        self.model.setText(_translate("Dialog", "model"))
        self.run.setText(_translate("Dialog", "run"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
