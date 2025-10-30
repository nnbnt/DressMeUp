import os
import maya.cmds as cmds


ROOT_RESOURCE_DIR = 'C:/Users/Nennebi/Documents/MAYA/PROJECTS/2024/scripts/dressMeUp/resources/'


CATEGORIES = {
	"Face": {
		"Face 01": "image/face/face_01.png",
		"Face 02": "image/face/face_02.png",
		"Face 03": "image/face/face_03.png",
		"Face 04": "image/face/face_04.png",
		"Face 05": "image/face/face_05.png",
		"Face 06": "image/face/face_06.png",
	},
	"Hair": {
		"Hair 01": "image/hair/hair_01.png",
		"Hair 02": "image/hair/hair_02.png",
		"Hair 03": "image/hair/hair_03.png",
		"Hair 04": "image/hair/hair_04.png",
		"Hair 05": "image/hair/hair_05.png",
		"Hair 06": "image/hair/hair_06.png",
	},
	"Upper": {
		"Shirt 01": "image/upper_p/shirt_01.png",
		"Shirt 02": "image/upper_p/shirt_02.png",
		"Shirt 03": "image/upper_p/shirt_03.png",
		"Shirt 04": "image/upper_p/shirt_04.png",
		"Shirt 05": "image/upper_p/shirt_05.png",
		"Shirt 06": "image/upper_p/shirt_06.png",
	},
	"Lower": {
		"Skirt 01": "image/lower_p/skirt_01.png",
		"Skirt 02": "image/lower_p/skirt_02.png",
		"Skirt 03": "image/lower_p/skirt_03.png",
		"Skirt 04": "image/lower_p/skirt_04.png",
		"Skirt 05": "image/lower_p/skirt_05.png",
		"Skirt 06": "image/lower_p/skirt_06.png",


	},
	"Shoes": {
		"Shoes 01": "image/shoes/shoes_01.png",
		"Shoes 02": "image/shoes/shoes_02.png",
		"Shoes 03": "image/shoes/shoes_03.png",
		"Shoes 04": "image/shoes/shoes_04.png",
		"Shoes 05": "image/shoes/shoes_05.png",

	},
	"Accessory": {
		"acces 01": "image/acces/acces_01.png",
		"acces 02": "image/acces/acces_02.png",
		"acces 03": "image/acces/acces_03.png",
		"acces 04": "image/acces/acces_04.png",
		"acces 05": "image/acces/acces_05.png",


	},
	"Accessory 1 ": {
		"acces 01": "image/acces_2/acces_01.png",
		"acces 02": "image/acces_2/acces_02.png",
		"acces 03": "image/acces_2/acces_03.png",
		"acces 04": "image/acces_2/acces_04.png",
		"acces 05": "image/acces_2/acces_05.png",


	},
}

Z_ORDER = {
	"Model": 0,
	"Face": 1,
	"Hair": 2,
	"Upper": 3,
	"Lower": 4,
	"Shoes": 2,
	"Accessory": 5,
	"Accessory 1 ": 6,
	
}
# (ถ้าอยากเพิ่มระบบเสริมทีหลัง เช่น random หรือ save outfit ก็เพิ่ม function ที่นี่ได้)
def get_full_path(image_path):
	"""แปลง path สั้นให้เป็น path เต็มพร้อม ROOT"""
	return os.path.join(ROOT_RESOURCE_DIR, image_path)
