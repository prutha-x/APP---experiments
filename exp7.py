def read_and_write(input_file, output_file, in_mode="r", op_mode="a"):
	try:
		with open(input_file, in_mode) as file:
			lines = file.readlines()
		with open(output_file, op_mode) as op_file:
			count = 0
			for line in lines:
				count += 1
				if count <= 2:
					op_file.write(line)
	except FileNotFoundError as e:
		print(f"Unable to find file: {e}")


if __name__ == "__main__":
	print("reading files.....")
	print("writing files.....")
	read_and_write("test.txt", "output.txt")
	print("saved data in output.txt")
