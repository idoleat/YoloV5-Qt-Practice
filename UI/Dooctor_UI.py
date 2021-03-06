# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dooctor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Labe_type = QtWidgets.QLabel(self.centralwidget)
        self.Labe_type.setGeometry(QtCore.QRect(610, 100, 111, 19))
        self.Labe_type.setObjectName("Labe_type")
        self.label_CurrentImageEva = QtWidgets.QLabel(self.centralwidget)
        self.label_CurrentImageEva.setGeometry(QtCore.QRect(560, 210, 111, 19))
        self.label_CurrentImageEva.setObjectName("label_CurrentImageEva")
        self.ImageSwitcher = QtWidgets.QSlider(self.centralwidget)
        self.ImageSwitcher.setGeometry(QtCore.QRect(40, 530, 481, 16))
        self.ImageSwitcher.setOrientation(QtCore.Qt.Horizontal)
        self.ImageSwitcher.setObjectName("ImageSwitcher")
        self.ResultImage_heatmap = QtWidgets.QGraphicsView(self.centralwidget)
        self.ResultImage_heatmap.setGeometry(QtCore.QRect(380, 340, 151, 101))
        self.ResultImage_heatmap.setObjectName("ResultImage_heatmap")
        self.OpenImageFolder = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImageFolder.setGeometry(QtCore.QRect(60, 40, 136, 27))
        self.OpenImageFolder.setAutoDefault(False)
        self.OpenImageFolder.setObjectName("OpenImageFolder")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(360, 480, 66, 19))
        self.label_result.setObjectName("label_result")
        self.label_predict = QtWidgets.QLabel(self.centralwidget)
        self.label_predict.setGeometry(QtCore.QRect(560, 130, 66, 16))
        self.label_predict.setObjectName("label_predict")
        self.ResultImage_cropped = QtWidgets.QGraphicsView(self.centralwidget)
        self.ResultImage_cropped.setGeometry(QtCore.QRect(250, 350, 121, 101))
        self.ResultImage_cropped.setObjectName("ResultImage_cropped")
        self.Predict = QtWidgets.QPushButton(self.centralwidget)
        self.Predict.setGeometry(QtCore.QRect(620, 130, 87, 27))
        self.Predict.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Predict.setAutoDefault(False)
        self.Predict.setDefault(False)
        self.Predict.setFlat(False)
        self.Predict.setObjectName("Predict")
        self.label_FolderImageEva = QtWidgets.QLabel(self.centralwidget)
        self.label_FolderImageEva.setGeometry(QtCore.QRect(560, 350, 101, 19))
        self.label_FolderImageEva.setObjectName("label_FolderImageEva")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(150, 470, 66, 19))
        self.label_image.setObjectName("label_image")
        self.DetectScaphoid = QtWidgets.QPushButton(self.centralwidget)
        self.DetectScaphoid.setGeometry(QtCore.QRect(290, 50, 117, 27))
        self.DetectScaphoid.setObjectName("DetectScaphoid")
        self.ClassifyNDetectFracture = QtWidgets.QPushButton(self.centralwidget)
        self.ClassifyNDetectFracture.setGeometry(QtCore.QRect(500, 30, 201, 27))
        self.ClassifyNDetectFracture.setObjectName("ClassifyNDetectFracture")
        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.OriginalImage.setEnabled(True)
        self.OriginalImage.setGeometry(QtCore.QRect(50, 110, 181, 201))
        self.OriginalImage.setFrameShape(QtWidgets.QFrame.Box)
        self.OriginalImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OriginalImage.setText("")
        self.OriginalImage.setScaledContents(True)
        self.OriginalImage.setObjectName("OriginalImage")
        self.ResultImage = QtWidgets.QLabel(self.centralwidget)
        self.ResultImage.setGeometry(QtCore.QRect(280, 110, 181, 201))
        self.ResultImage.setFrameShape(QtWidgets.QFrame.Box)
        self.ResultImage.setText("")
        self.ResultImage.setScaledContents(True)
        self.ResultImage.setObjectName("ResultImage")
        self.ResultImage_scaphoid = QtWidgets.QLabel(self.centralwidget)
        self.ResultImage_scaphoid.setGeometry(QtCore.QRect(80, 340, 101, 111))
        self.ResultImage_scaphoid.setFrameShape(QtWidgets.QFrame.Box)
        self.ResultImage_scaphoid.setText("")
        self.ResultImage_scaphoid.setScaledContents(True)
        self.ResultImage_scaphoid.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultImage_scaphoid.setObjectName("ResultImage_scaphoid")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 180, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 530, 31, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 530, 61, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 530, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 240, 66, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 270, 66, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 300, 66, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 320, 66, 19))
        self.label_8.setObjectName("label_8")
        self.Recall_c = QtWidgets.QLabel(self.centralwidget)
        self.Recall_c.setGeometry(QtCore.QRect(630, 240, 66, 19))
        self.Recall_c.setObjectName("Recall_c")
        self.IOU_c = QtWidgets.QLabel(self.centralwidget)
        self.IOU_c.setGeometry(QtCore.QRect(630, 270, 66, 19))
        self.IOU_c.setObjectName("IOU_c")
        self.F1_c = QtWidgets.QLabel(self.centralwidget)
        self.F1_c.setGeometry(QtCore.QRect(630, 300, 66, 19))
        self.F1_c.setObjectName("F1_c")
        self.Precision_c = QtWidgets.QLabel(self.centralwidget)
        self.Precision_c.setGeometry(QtCore.QRect(630, 320, 66, 19))
        self.Precision_c.setObjectName("Precision_c")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 410, 66, 19))
        self.label_13.setObjectName("label_13")
        self.Recall_f = QtWidgets.QLabel(self.centralwidget)
        self.Recall_f.setGeometry(QtCore.QRect(630, 380, 66, 19))
        self.Recall_f.setObjectName("Recall_f")
        self.F1_f = QtWidgets.QLabel(self.centralwidget)
        self.F1_f.setGeometry(QtCore.QRect(630, 440, 66, 19))
        self.F1_f.setObjectName("F1_f")
        self.Precision_f = QtWidgets.QLabel(self.centralwidget)
        self.Precision_f.setGeometry(QtCore.QRect(630, 460, 66, 19))
        self.Precision_f.setObjectName("Precision_f")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(560, 380, 66, 19))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(560, 440, 66, 19))
        self.label_18.setObjectName("label_18")
        self.IOU_f = QtWidgets.QLabel(self.centralwidget)
        self.IOU_f.setGeometry(QtCore.QRect(630, 410, 66, 19))
        self.IOU_f.setObjectName("IOU_f")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(560, 460, 66, 19))
        self.label_20.setObjectName("label_20")
        self.Number_now = QtWidgets.QLabel(self.centralwidget)
        self.Number_now.setGeometry(QtCore.QRect(570, 530, 66, 19))
        self.Number_now.setObjectName("Number_now")
        self.Number_total = QtWidgets.QLabel(self.centralwidget)
        self.Number_total.setGeometry(QtCore.QRect(670, 530, 66, 19))
        self.Number_total.setObjectName("Number_total")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 100, 66, 19))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Labe_type.setText(_translate("MainWindow", "frac?"))
        self.label_CurrentImageEva.setText(_translate("MainWindow", "Current Image:"))
        self.OpenImageFolder.setText(_translate("MainWindow", "Open Image Folder"))
        self.label_result.setText(_translate("MainWindow", "Result"))
        self.label_predict.setText(_translate("MainWindow", "Predict:"))
        self.Predict.setText(_translate("MainWindow", "Fracture"))
        self.label_FolderImageEva.setText(_translate("MainWindow", "Folder (mean):"))
        self.label_image.setText(_translate("MainWindow", "Image"))
        self.DetectScaphoid.setText(_translate("MainWindow", "Detect Scaphoid"))
        self.ClassifyNDetectFracture.setText(_translate("MainWindow", "Classify and Detect Fracture"))
        self.label.setText(_translate("MainWindow", "Evaluation"))
        self.label_2.setText(_translate("MainWindow", "No."))
        self.label_3.setText(_translate("MainWindow", "image of"))
        self.label_4.setText(_translate("MainWindow", "Total Images"))
        self.label_5.setText(_translate("MainWindow", "Recall"))
        self.label_6.setText(_translate("MainWindow", "IOU"))
        self.label_7.setText(_translate("MainWindow", "F1-score"))
        self.label_8.setText(_translate("MainWindow", "Precision"))
        self.Recall_c.setText(_translate("MainWindow", "0.0"))
        self.IOU_c.setText(_translate("MainWindow", "0.0"))
        self.F1_c.setText(_translate("MainWindow", "0.0"))
        self.Precision_c.setText(_translate("MainWindow", "0.0"))
        self.label_13.setText(_translate("MainWindow", "IOU"))
        self.Recall_f.setText(_translate("MainWindow", "0.0"))
        self.F1_f.setText(_translate("MainWindow", "0.0"))
        self.Precision_f.setText(_translate("MainWindow", "0.0"))
        self.label_17.setText(_translate("MainWindow", "Recall"))
        self.label_18.setText(_translate("MainWindow", "F1-score"))
        self.IOU_f.setText(_translate("MainWindow", "0.0"))
        self.label_20.setText(_translate("MainWindow", "Precision"))
        self.Number_now.setText(_translate("MainWindow", "77"))
        self.Number_total.setText(_translate("MainWindow", "777"))
        self.label_9.setText(_translate("MainWindow", "Type:"))
