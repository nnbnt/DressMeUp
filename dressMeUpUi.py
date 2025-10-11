try: 
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 

ROOT_RESOURCE_DIR = 'C:/Users/Nennebi/Documents/MAYA/PROJECTS/2024/scripts/dressMeUp/resources'
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

		

		self.scene = QtWidgets.QGraphicsScene()
		self.view = QtWidgets.QGraphicsView(self.scene)

		self.mainLayout.addWidget(self.view)

		bg = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(f"image/room_test.png"))
		bg.setZValue(0)
		self.scene.addItem(bg)
		self.view.setStyleSheet(
			'''
				QLabel {
					
					min-width: 300px;
					min-height: 400px;
					
					
					
				}


			'''

		)

		

		# ++++++++++ ภาพตัวละคร +++++++++++
		
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image/model_test.png")
		scaled_pixmap = self.imagePixmap.scaled(
			
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation

			)


		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.imageLabel.setPixmap(self.imagePixmap)


		# ++++++++++ คำสั่งเอาภาพเข้ามาวาง +++++++++++


		
		self.charLayout = QtWidgets.QVBoxLayout(self.view)
		self.contentLayout.addWidget(self.view)

		
		self.charLayout.addWidget(self.imageLabel)








		# คอลัมน์ขวา (Panel)
	


		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('Reset')
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
		self.cancelButton = QtWidgets.QPushButton('')
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