try: 
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

from . import dressMeUpUtil as dutil


ROOT_RESOURCE_DIR = 'C:/Users/Nennebi/Documents/MAYA/PROJECTS/2024/scripts/dressMeUp/resources/'
class DressMeUPDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Dress Me Up')
		self.resize(800,500)
		self.setFixedSize(self.width(), self.height())

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
					min-width: 380px;
					min-height: 50px;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					font-family: Papyrus;
					font-weight: bold;
					text-align: center;
					padding: 5px;
					margin: 5px
				}


			'''

		)
		


		self.nameLayout.addWidget(self.nameLabel)
	
		self.contentLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.contentLayout)
		self.setLayout(self.mainLayout)

		

		self.scene = QtWidgets.QGraphicsScene()
		self.view = QtWidgets.QGraphicsView(self.scene)

		self.mainLayout.addWidget(self.view)

		bg = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}image/room_test.png"))
		bg.setZValue(0)
		self.scene.addItem(bg)
		
		# ++++++++++ ภาพตัวละคร +++++++++++
		
		model = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}image/model_test.png"))
		model.setZValue(1)
		self.scene.addItem(model)
		self.layers = {cat: None for cat in dutil.CATEGORIES.keys()}


		# ++++++++++ คำสั่งเอาภาพเข้ามาวาง +++++++++++


		
		self.charLayout = QtWidgets.QVBoxLayout(self.view)
		self.contentLayout.addWidget(self.view)

		self.rightFrame = QtWidgets.QFrame()
		self.rightFrame.setStyleSheet("""
			QFrame {
				background-color: #FFEFF2;
				border-radius: 10px;
				min-width: 380px;
				min-height: 5px;
			}
		""")

		self.rightLayout = QtWidgets.QVBoxLayout(self.rightFrame)
		self.contentLayout.addWidget(self.rightFrame)

		# Label ฝั่งขวา
		self.infoLabel = QtWidgets.QLabel("✨ Dress Option ✨")
		self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.infoLabel.setStyleSheet("""
			QLabel {
				background-color: #FCD4E4;
				color: #86445A;
				border-radius: 2px;
				font-size: 16px;
				font-family: Papyrus;
				font-weight: bold;
				padding: 2px;
			}
		""")
		self.rightLayout.addWidget(self.infoLabel)
				


		# ===== เพิ่มปุ่ม option =====
		self.scrollArea = QtWidgets.QScrollArea()
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setStyleSheet("""
			QScrollArea {
				background-color: transparent;
				border-radius: 5px;
		""")

		self.scrollContent = QtWidgets.QWidget()
		self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollContent)

		

		for category, items in dutil.CATEGORIES.items():
			catLabel = QtWidgets.QLabel(f" {category}")
			catLabel.setStyleSheet("""
				QLabel {
					font-weight: bold;
					font-family: Papyrus;
					font-size: 16px;
					border-radius: 5px;
					color: #86445A;
					padding: 4px;
					margin-top: 2px;
				}
			""")
			self.scrollLayout.addWidget(catLabel)

			for itemName, imagePath in items.items():
				btn = QtWidgets.QPushButton(itemName)
				btn.setStyleSheet("""
					QPushButton {
						background-color: #FDE4EB;
						border-radius:10px;
						padding: 4px;
						font-weight: bold;
						font-size: 14px;
						font-family: Papyrus;
						color: #6A4050;
					}
					QPushButton:hover {
						background-color: #FACFE2;
					}
					QPushButton:pressed {
						background-color: #F8BBD0;
					}
				""")
				# ส่ง category และ path ไปยังฟังก์ชัน
				btn.clicked.connect(lambda checked=False, c=category, p=imagePath: self.changeOutfit(c, p))

				self.scrollLayout.addWidget(btn)


		self.scrollLayout.addStretch()
		self.scrollContent.setLayout(self.scrollLayout)
		self.scrollArea.setWidget(self.scrollContent)

		self.rightLayout.addWidget(self.scrollArea)



			# ===== Reset Button =====





		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)



		self.cancelButton = QtWidgets.QPushButton('')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FFF9DD;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 4px;
					font-family: Papyrus;
					font-weight: bold;
				}

				QPushButton:hover {
					background-color: #FFF9DD;

				}

				QPushButton:pressed {
					background-color: #FFF9DD;
				}
			'''

		)
		
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()
		self.charLayout.addStretch()


		self.resetButton = QtWidgets.QPushButton('RESET')

		self.resetButton.setStyleSheet("""
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
		""")
		self.resetButton.clicked.connect(self.resetOutfit)
		self.buttonLayout.addWidget(self.resetButton)


		self.mainLayout.addStretch()
		self.charLayout.addStretch()







	def changeOutfit(self, category, imagePath):
		fullPath = f"{ROOT_RESOURCE_DIR}{imagePath}"

		#  ++++++++++ ลบภาพเดิม  ++++++++++ 
		if self.layers[category]:
			self.scene.removeItem(self.layers[category])
			self.layers[category] = None

		#  ++++++++++ โหลดภาพใหม่  ++++++++++ 
		newItem = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(fullPath))

		z_value = dutil.Z_ORDER.get(category, 1)  
		newItem.setZValue(z_value)

		self.scene.addItem(newItem)
		self.layers[category] = newItem	

	def resetOutfit(self):
		for cat, item in self.layers.items():
			if item:
				self.scene.removeItem(item)
				self.layers[cat] = None


def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = DressMeUPDialog(parent=ptr)
	ui.show()