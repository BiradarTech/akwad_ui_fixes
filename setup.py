from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in akwad_ui_fixes/__init__.py
from akwad_ui_fixes import __version__ as version

setup(
	name="akwad_ui_fixes",
	version=version,
	description="Akwad UI fixes for ERPNext",
	author="Akwad Programming",
	author_email="support@akwad.qa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
