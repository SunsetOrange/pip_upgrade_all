#!/usr/bin/env python3
import os
import subprocess


try:
	is_admin = os.getuid() == 0
except AttributeError:
	import ctypes
	is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
if is_admin:
	# Update pip, setuptools and wheels before importing pkg_resources.
	subprocess.call("python -m pip install --upgrade pip wheel")
	subprocess.call("python -m pip uninstall setuptools")  # setuptools install is often broken. Uninstall first..
	subprocess.call("python -m pip install setuptools")  # ..then reinstall to fix issues with pkg_resources.
	import pkg_resources
	for dist in pkg_resources.working_set:
		subprocess.call("python -m pip install --upgrade " + dist.project_name, shell=True)
else:
	print("Limited privileges detected!\nPlease rerun this script with admin level privileges.")
	input("\nPress Enter to exit.")
