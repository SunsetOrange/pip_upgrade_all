# pip_upgrade_all

This script upgrades all installed Python packages to their latest versions. It is intended Windows users who are not operating within virtual environments. It has been tested on Windows only and is unlikely to work with Linux or OSX in its current state.

The script must be run with administrative privileges or it will refuse to attempt to update packages. The script has been rewritten a few times over the years to circumvent several issues that have arisen, such as...
* pip not being upgraded
* the common broken setuptools installation
* wheels module being upgraded late due to alphabetical ordering
* deprecation issues related to retrieving a list of installed packages.
