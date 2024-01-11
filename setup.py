from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Girish Sawant',
    author_email='girishsawant9999@gmail.com',
    install_requires=["VertexAI","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)