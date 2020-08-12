import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='flask-creator',  

     version='0.1',

     scripts=['flask-creator'] ,

     author="Lucas SCHUTZ",

     author_email="lucas.schutz0954@gmail.com",

     description="A flask tool to quickly create and launch flask app",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )