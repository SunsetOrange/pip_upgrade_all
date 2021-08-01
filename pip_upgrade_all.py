#!/usr/bin/env python3
import os
import sys
import subprocess


def run(is_admin: bool):
	subprocess.call(["python3", "-m", "pip", "install", "--upgrade", "pip", "wheel"])
	if is_admin:
		subprocess.call(["python3", "-m", "pip", "uninstall", "-y", "setuptools"])  # setuptools install is often broken. Uninstall first..
	subprocess.call(["python3", "-m", "pip", "install", "setuptools"])  # ..then reinstall to fix issues with pkg_resources.

	# Update pip, setuptools and wheels before importing pkg_resources.
	import pkg_resources
	for dist in pkg_resources.working_set:  # pylint: disable=not-an-iterable
		project_name = dist.project_name
		subprocess.call(["pip", "install", "--upgrade", project_name])


if __name__ == "__main__":
	is_admin = False
	if "admin" in sys.argv:
		try:
			is_admin = os.getuid() == 0
		except AttributeError:
			import ctypes
			is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

	if is_admin:
		print("Running script in admin mode.")
	else:
		print("Running script in local mode.")

	run(is_admin)
	print("\nPackages have been updated.")
	input("\nPress Enter to exit.")
