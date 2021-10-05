import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bpmtoolbox',
    version='0.0.1',
    author='Richard Kastiak',
    author_email='kastiak.richard@gmail.com',
    description='BPM tool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Riqardos/BPMTool',
    project_urls={
        "Bug Tracker": "https://github.com/Riqardos/BPMTool/issues"
    },
    license='MIT',
    packages=['bpmtoolbox'],
    # install_requires=['AdminTask'],
)