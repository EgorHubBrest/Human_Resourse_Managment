from setuptools import setup, find_packages


def require_pakages():
	with open("requirements.txt") as file_requirements:
		packages = [lib.replace('\n', '') for lib in file_requirements.readlines()]
	return packages


setup(name="department_app",
	  version="0.1",
	  description="HRM for Manager",
	  lond_description=open("README.md").read(),
	  packages=find_packages(),
	  url="https://github.com/EgorHubBrest/Human_Resourse_Managment.git",
	  install_requires=require_pakages()
	  )
