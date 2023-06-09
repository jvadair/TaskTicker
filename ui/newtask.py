# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtask.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTask(object):
    def setupUi(self, NewTask):
        NewTask.setObjectName("NewTask")
        NewTask.resize(495, 280)
        NewTask.setMaximumSize(QtCore.QSize(495, 280))
        self.label = QtWidgets.QLabel(NewTask)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 51))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.cbxTags = QtWidgets.QComboBox(NewTask)
        self.cbxTags.setGeometry(QtCore.QRect(320, 20, 161, 26))
        self.cbxTags.setObjectName("cbxTags")
        self.txtTitle = QtWidgets.QLineEdit(NewTask)
        self.txtTitle.setGeometry(QtCore.QRect(130, 70, 351, 32))
        self.txtTitle.setObjectName("txtTitle")
        self.label_2 = QtWidgets.QLabel(NewTask)
        self.label_2.setGeometry(QtCore.QRect(20, 76, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(NewTask)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtDescription = QtWidgets.QPlainTextEdit(NewTask)
        self.txtDescription.setGeometry(QtCore.QRect(130, 150, 351, 71))
        self.txtDescription.setObjectName("txtDescription")
        self.btnCreate = QtWidgets.QPushButton(NewTask)
        self.btnCreate.setGeometry(QtCore.QRect(390, 240, 94, 32))
        self.btnCreate.setObjectName("btnCreate")
        self.btnCancel = QtWidgets.QPushButton(NewTask)
        self.btnCancel.setGeometry(QtCore.QRect(290, 240, 94, 32))
        self.btnCancel.setObjectName("btnCancel")
        self.label_4 = QtWidgets.QLabel(NewTask)
        self.label_4.setGeometry(QtCore.QRect(20, 109, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.dteDate = QtWidgets.QDateTimeEdit(NewTask)
        self.dteDate.setGeometry(QtCore.QRect(130, 110, 351, 26))
        self.dteDate.setDate(QtCore.QDate(2000, 1, 1))
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName("dteDate")

        self.retranslateUi(NewTask)
        QtCore.QMetaObject.connectSlotsByName(NewTask)

    def retranslateUi(self, NewTask):
        _translate = QtCore.QCoreApplication.translate
        NewTask.setWindowTitle(_translate("NewTask", "Form"))
        self.label.setText(_translate("NewTask", "New Task"))
        self.cbxTags.setPlaceholderText(_translate("NewTask", "Tags"))
        self.label_2.setText(_translate("NewTask", "Title"))
        self.label_3.setText(_translate("NewTask", "Description"))
        self.btnCreate.setText(_translate("NewTask", "Create"))
        self.btnCancel.setText(_translate("NewTask", "Cancel"))
        self.label_4.setText(_translate("NewTask", "Due date"))
        self.dteDate.setDisplayFormat(_translate("NewTask", "mm/dd/yy h:mm AP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTask = QtWidgets.QWidget()
    ui = Ui_NewTask()
    ui.setupUi(NewTask)
    NewTask.show()
    sys.exit(app.exec_())
