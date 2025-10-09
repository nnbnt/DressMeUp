try: 
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 


class DressMeUPDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Dress Me Up')
		self.resize(1000,500)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: #FFF9DD;')

	

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel(' Dree Me Up !! 彡☆ ')
		self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.nameLabel.setStyleSheet(
			'''
				QLabel {
					background-color: #9FE3E2;
					min-width: 5px;
					min-height: 40px;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					font-family: Papyrus;
					font-weight: bold;
					text-align: center;
					
				}


			'''

		)
		


		self.nameLayout.addWidget(self.nameLabel)
		
		self.contentLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.contentLayout)

# ✅ คอลัมน์ซ้าย (Character Area)
		self.charFrame = QtWidgets.QFrame()
		self.charFrame.setStyleSheet(

			'''
				QFrame {
					background-color: #FFFDf6;
					min-width: 300px;
					min-height: 400px;
				}
		
			'''
		)
		

		self.charLayout = QtWidgets.QVBoxLayout(self.charFrame)
		#self.charLabel = QtWidgets.QLabel("Character Area")
		#self.charLabel.setAlignment(QtCore.Qt.AlignCenter)
		#self.charLayout.addWidget(self.charLabel)

		self.contentLayout.addWidget(self.charFrame)

		# ✅ คอลัมน์ขวา (Panel)
		self.panelFrame = QtWidgets.QFrame()
		self.panelFrame.setStyleSheet("""
				QFrame {
					background-color: #FFEFF2;
					min-width: 300px;
					min-height: 400px;
			}
			"""

		)

		self.panelLayout = QtWidgets.QVBoxLayout(self.panelFrame)
		#self.panelLabel = QtWidgets.QLabel("Panel")
		#self.panelLabel.setAlignment(QtCore.Qt.AlignCenter)
		#self.panelLayout.addWidget(self.panelLabel)

		self.contentLayout.addWidget(self.panelFrame)



		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('Create')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FFCBCA;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 4px;
					font-family: Papyrus;
					font-weight: bold;
				}

				QPushButton:hover {
					background-color: #F2A2AD;

				}

				QPushButton:pressed {
					background-color: #F2668B;
				}


			'''

		)
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FFCBCA;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 4px;
					font-family: Papyrus;
					font-weight: bold;
				}

				QPushButton:hover {
					background-color: #F2A2AD;

				}

				QPushButton:pressed {
					background-color: #F2668B;
				}
			'''

		)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()
		self.charLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = DressMeUPDialog(parent=ptr)
	ui.show()