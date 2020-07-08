import json, pprint
import ruamel.yaml
yaml = ruamel.yaml.YAML()

def mergeFiles(originalFile, *args, **kargs):
	merged = open("merged.yaml", "w")

	with open(originalFile) as f:
		data = yaml.load(f)

	for arg in args:
		with open(arg) as g:
			data1 = yaml.load(g)

	 	# key = data
	 	# value = data1

		for item1 in data1:
			print("item1: ", item1)
			if item1 in data:
				# If item is paths
				print("data[item1]: ", data[item1])
				for item2 in data1[item1]:
					print("item2: ", item2)
					if item2 in data[item1]:
						# print("data[item1][item2]: ", data[item1][item2])
						# print("")
						# print("data1[item1][item2]: ", data1[item1][item2])
						data[item1][item2].update(data1[item1][item2])
						data1[item1][item2].update(data[item1][item2])
						# print("if updated", data[item1][item2])
					else:
						data[item1].update(data1[item1])
						print("else updated", data1[item1])
			else:
				data[item1].update(data1[item1])
				print("bahaar waal else updated")


		


	print(data)
	json_formatted_str = yaml.dump(data, merged)
	merged.close()




if __name__ == '__main__':
	mergeFiles("original.yaml", "add.yaml")

