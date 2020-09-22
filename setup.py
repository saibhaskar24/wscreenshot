import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wscreenshot',
    version='0.0.3',
    packages=setuptools.find_packages(),
    url='https://github.com/saibhaskar24/wscreenshot',
    license='MIT License',
    author='saibhaskar',
    author_email='saibaaskar24091999@gmail.com',
    description='This package which helps you to take screenshot of specific running window',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Environment :: Win32 (MS Windows)"
    ],
)
