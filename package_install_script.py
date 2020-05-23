import os

package_list = ("checksumdir")

for temp1 in package_list:
	instruction = ("python -m pip install "+temp1)
	os.system(instruction)