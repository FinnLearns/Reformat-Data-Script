import os

current_dir = os.getcwd()

def padZeros(path):
	new_lines = []

	with open(path, 'r') as file:
		lines = file.readlines()

	for line in lines:
		line = line.rstrip() + " 0.0 0.0 0 0.0 0.0 0 0.0 0.0 0 0.0 0.0 0 0.0 0.0 0\n"
		new_lines.append(line)

	with open(path, 'w') as file:
		file.writelines(new_lines)

def rename_img(num):	
	img_folder = f"{current_dir}/images"

	# sorted so that images and labels match up with each other
	imgs = sorted(os.listdir((img_folder)))

	for img in imgs:
		new_name = f"circuit_0{num}.jpg"
		os.rename(f"{img_folder}/{img}",f"{img_folder}/{new_name}")
		num +=1

def rename_lbl(num):
	lbl_folder = f"{current_dir}/labels"
	
	# sorted so that images and labels match up with each other
	lbls = sorted(os.listdir((lbl_folder)))

	for lbl in lbls:
		new_name = f"circuit_0{num}.txt"
		os.rename(f"{lbl_folder}/{lbl}",f"{lbl_folder}/{new_name}")
		num +=1

		padZeros(f"{lbl_folder}/{new_name}")

def main():
	user_num = int(input("Enter a starting number: "))
	rename_img(user_num)
	rename_lbl(user_num)

if __name__ == '__main__':
	main()