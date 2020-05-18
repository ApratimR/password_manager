import os

package_list = ("ZODB",
				"checksumdir")

for temp1 in package_list:
	instruction = ("python -m pip install "+temp1)
	os.system(instruction)