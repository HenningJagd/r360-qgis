# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GG\2015-10-05_bitbucket_api_plugin\qgisgroup\ggapi\ui\dist_matrix.ui'
#
# Created: Mon Sep 12 11:29:12 2016
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DistM_Dialog(object):
    def setupUi(self, DistM_Dialog):
        DistM_Dialog.setObjectName(_fromUtf8("DistM_Dialog"))
        DistM_Dialog.setWindowModality(QtCore.Qt.NonModal)
        DistM_Dialog.resize(392, 755)
        DistM_Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(DistM_Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.inPoint1label = QtGui.QLabel(DistM_Dialog)
        self.inPoint1label.setObjectName(_fromUtf8("inPoint1label"))
        self.verticalLayout.addWidget(self.inPoint1label)
        self.inPoint1 = QtGui.QComboBox(DistM_Dialog)
        self.inPoint1.setObjectName(_fromUtf8("inPoint1"))
        self.verticalLayout.addWidget(self.inPoint1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 3)
        self.progressBar = QtGui.QProgressBar(DistM_Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DistM_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 2)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.inField1label = QtGui.QLabel(DistM_Dialog)
        self.inField1label.setObjectName(_fromUtf8("inField1label"))
        self.vboxlayout.addWidget(self.inField1label)
        self.inField1 = QtGui.QComboBox(DistM_Dialog)
        self.inField1.setObjectName(_fromUtf8("inField1"))
        self.vboxlayout.addWidget(self.inField1)
        self.gridLayout.addLayout(self.vboxlayout, 1, 0, 1, 3)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.inField2label = QtGui.QLabel(DistM_Dialog)
        self.inField2label.setObjectName(_fromUtf8("inField2label"))
        self.vboxlayout1.addWidget(self.inField2label)
        self.inField2 = QtGui.QComboBox(DistM_Dialog)
        self.inField2.setObjectName(_fromUtf8("inField2"))
        self.vboxlayout1.addWidget(self.inField2)
        self.gridLayout.addLayout(self.vboxlayout1, 3, 0, 1, 3)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.label_2 = QtGui.QLabel(DistM_Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout2.addWidget(self.label_2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.outFile = QtGui.QLineEdit(DistM_Dialog)
        self.outFile.setReadOnly(True)
        self.outFile.setObjectName(_fromUtf8("outFile"))
        self.hboxlayout.addWidget(self.outFile)
        self.btnFile = QtGui.QPushButton(DistM_Dialog)
        self.btnFile.setObjectName(_fromUtf8("btnFile"))
        self.hboxlayout.addWidget(self.btnFile)
        self.vboxlayout2.addLayout(self.hboxlayout)
        self.addToMap_checkBox = QtGui.QCheckBox(DistM_Dialog)
        self.addToMap_checkBox.setChecked(True)
        self.addToMap_checkBox.setObjectName(_fromUtf8("addToMap_checkBox"))
        self.vboxlayout2.addWidget(self.addToMap_checkBox)
        self.gridLayout.addLayout(self.vboxlayout2, 8, 0, 1, 3)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.inPoint2label = QtGui.QLabel(DistM_Dialog)
        self.inPoint2label.setObjectName(_fromUtf8("inPoint2label"))
        self.vboxlayout3.addWidget(self.inPoint2label)
        self.inPoint2 = QtGui.QComboBox(DistM_Dialog)
        self.inPoint2.setObjectName(_fromUtf8("inPoint2"))
        self.vboxlayout3.addWidget(self.inPoint2)
        self.gridLayout.addLayout(self.vboxlayout3, 2, 0, 1, 3)
        self.groupBox_3 = QtGui.QGroupBox(DistM_Dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rdoLinear = QtGui.QRadioButton(self.groupBox_3)
        self.rdoLinear.setChecked(True)
        self.rdoLinear.setObjectName(_fromUtf8("rdoLinear"))
        self.verticalLayout_2.addWidget(self.rdoLinear)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(35, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.chkNearest = QtGui.QCheckBox(self.groupBox_3)
        self.chkNearest.setObjectName(_fromUtf8("chkNearest"))
        self.horizontalLayout_2.addWidget(self.chkNearest)
        self.spnNearest = QtGui.QSpinBox(self.groupBox_3)
        self.spnNearest.setEnabled(False)
        self.spnNearest.setMinimum(1)
        self.spnNearest.setMaximum(9999)
        self.spnNearest.setObjectName(_fromUtf8("spnNearest"))
        self.horizontalLayout_2.addWidget(self.spnNearest)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.rdoStandard = QtGui.QRadioButton(self.groupBox_3)
        self.rdoStandard.setEnabled(True)
        self.rdoStandard.setObjectName(_fromUtf8("rdoStandard"))
        self.verticalLayout_2.addWidget(self.rdoStandard)
        self.rdoRoute = QtGui.QRadioButton(self.groupBox_3)
        self.rdoRoute.setObjectName(_fromUtf8("rdoRoute"))
        self.verticalLayout_2.addWidget(self.rdoRoute)
        self.rdoLines = QtGui.QRadioButton(self.groupBox_3)
        self.rdoLines.setObjectName(_fromUtf8("rdoLines"))
        self.verticalLayout_2.addWidget(self.rdoLines)
        self.gridLayout.addWidget(self.groupBox_3, 6, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(DistM_Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.rdoCar = QtGui.QRadioButton(self.groupBox_2)
        self.rdoCar.setChecked(True)
        self.rdoCar.setObjectName(_fromUtf8("rdoCar"))
        self.mot = QtGui.QButtonGroup(DistM_Dialog)
        self.mot.setObjectName(_fromUtf8("mot"))
        self.mot.addButton(self.rdoCar)
        self.gridlayout.addWidget(self.rdoCar, 0, 0, 1, 1)
        self.rdoPublic = QtGui.QRadioButton(self.groupBox_2)
        self.rdoPublic.setObjectName(_fromUtf8("rdoPublic"))
        self.mot.addButton(self.rdoPublic)
        self.gridlayout.addWidget(self.rdoPublic, 3, 0, 1, 1)
        self.rdoBike = QtGui.QRadioButton(self.groupBox_2)
        self.rdoBike.setEnabled(True)
        self.rdoBike.setObjectName(_fromUtf8("rdoBike"))
        self.mot.addButton(self.rdoBike)
        self.gridlayout.addWidget(self.rdoBike, 1, 0, 1, 1)
        self.rdoWalk = QtGui.QRadioButton(self.groupBox_2)
        self.rdoWalk.setEnabled(True)
        self.rdoWalk.setObjectName(_fromUtf8("rdoWalk"))
        self.mot.addButton(self.rdoWalk)
        self.gridlayout.addWidget(self.rdoWalk, 2, 0, 1, 1)
        self.time_control = QtGui.QHBoxLayout()
        self.time_control.setObjectName(_fromUtf8("time_control"))
        self.pub_dateTimeEdit = QtGui.QDateTimeEdit(self.groupBox_2)
        self.pub_dateTimeEdit.setEnabled(False)
        self.pub_dateTimeEdit.setTime(QtCore.QTime(8, 0, 0))
        self.pub_dateTimeEdit.setObjectName(_fromUtf8("pub_dateTimeEdit"))
        self.time_control.addWidget(self.pub_dateTimeEdit)
        self.pub_deptRdo = QtGui.QRadioButton(self.groupBox_2)
        self.pub_deptRdo.setEnabled(False)
        self.pub_deptRdo.setChecked(True)
        self.pub_deptRdo.setObjectName(_fromUtf8("pub_deptRdo"))
        self.pub_mode = QtGui.QButtonGroup(DistM_Dialog)
        self.pub_mode.setObjectName(_fromUtf8("pub_mode"))
        self.pub_mode.addButton(self.pub_deptRdo)
        self.time_control.addWidget(self.pub_deptRdo)
        self.pub_arrRdo = QtGui.QRadioButton(self.groupBox_2)
        self.pub_arrRdo.setEnabled(False)
        self.pub_arrRdo.setObjectName(_fromUtf8("pub_arrRdo"))
        self.pub_mode.addButton(self.pub_arrRdo)
        self.time_control.addWidget(self.pub_arrRdo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.time_control.addItem(spacerItem1)
        self.gridlayout.addLayout(self.time_control, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 4, 0, 1, 3)
        self.groupBox_4 = QtGui.QGroupBox(DistM_Dialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self._6 = QtGui.QGridLayout(self.groupBox_4)
        self._6.setObjectName(_fromUtf8("_6"))
        self.rdoMinutes = QtGui.QRadioButton(self.groupBox_4)
        self.rdoMinutes.setEnabled(True)
        self.rdoMinutes.setObjectName(_fromUtf8("rdoMinutes"))
        self._6.addWidget(self.rdoMinutes, 1, 0, 1, 1)
        self.rdoMeter = QtGui.QRadioButton(self.groupBox_4)
        self.rdoMeter.setChecked(True)
        self.rdoMeter.setObjectName(_fromUtf8("rdoMeter"))
        self._6.addWidget(self.rdoMeter, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 5, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)

        self.retranslateUi(DistM_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DistM_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(DistM_Dialog)

    def retranslateUi(self, DistM_Dialog):
        DistM_Dialog.setWindowTitle(_translate("DistM_Dialog", "Road Distance Matrix", None))
        self.inPoint1label.setText(_translate("DistM_Dialog", "Input layer", None))
        self.inField1label.setText(_translate("DistM_Dialog", "Input unique ID field", None))
        self.inField2label.setText(_translate("DistM_Dialog", "Target unique ID field", None))
        self.label_2.setText(_translate("DistM_Dialog", "Output matrix", None))
        self.btnFile.setText(_translate("DistM_Dialog", "Browse", None))
        self.addToMap_checkBox.setText(_translate("DistM_Dialog", "Add to to map", None))
        self.inPoint2label.setText(_translate("DistM_Dialog", "Target layer", None))
        self.groupBox_3.setTitle(_translate("DistM_Dialog", "Output type", None))
        self.rdoLinear.setText(_translate("DistM_Dialog", "Linear (CSV file)", None))
        self.chkNearest.setText(_translate("DistM_Dialog", " Use only the nearest (k) target points", None))
        self.rdoStandard.setText(_translate("DistM_Dialog", "Standard (CSV fil)", None))
        self.rdoRoute.setText(_translate("DistM_Dialog", "Routes (SHP fil)", None))
        self.rdoLines.setText(_translate("DistM_Dialog", "Straight lines (SHP fil)", None))
        self.groupBox_2.setTitle(_translate("DistM_Dialog", "Mode of transport", None))
        self.rdoCar.setText(_translate("DistM_Dialog", "Car", None))
        self.rdoPublic.setText(_translate("DistM_Dialog", "Public transport", None))
        self.rdoBike.setText(_translate("DistM_Dialog", "Bicycle", None))
        self.rdoWalk.setText(_translate("DistM_Dialog", "Walk", None))
        self.pub_dateTimeEdit.setDisplayFormat(_translate("DistM_Dialog", "dd-MM-yyyy HH:mm", None))
        self.pub_deptRdo.setText(_translate("DistM_Dialog", "Afgang", None))
        self.pub_arrRdo.setText(_translate("DistM_Dialog", "Ankomst", None))
        self.groupBox_4.setTitle(_translate("DistM_Dialog", "Unit", None))
        self.rdoMinutes.setText(_translate("DistM_Dialog", "Minutes", None))
        self.rdoMeter.setText(_translate("DistM_Dialog", "Meters", None))

