# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'done.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Done(object):
    def setupUi(self, Done):
        Done.setObjectName("Done")
        Done.resize(283, 120)
        self.label = QtWidgets.QLabel(Done)
        self.label.setGeometry(QtCore.QRect(120, 0, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Done)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.clbReturn = QtWidgets.QCommandLinkButton(Done)
        self.clbReturn.setGeometry(QtCore.QRect(160, 60, 81, 31))
        self.clbReturn.setObjectName("clbReturn")

        self.retranslateUi(Done)
        QtCore.QMetaObject.connectSlotsByName(Done)

    def retranslateUi(self, Done):
        _translate = QtCore.QCoreApplication.translate
        Done.setWindowTitle(_translate("Done", "You did it!"))
        self.label.setText(_translate("Done", "You did it!"))
        self.label_2.setText(_translate("Done", "🎉"))
        self.clbReturn.setText(_translate("Done", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Done = QtWidgets.QWidget()
    ui = Ui_Done()
    ui.setupUi(Done)
    Done.show()
    sys.exit(app.exec_())
