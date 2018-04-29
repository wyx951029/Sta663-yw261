from setuptools import setup

setup(name = "sta663-yw261",
      version = "1.0",
      author='Yixuan Wang',
      author_email='yixuan.wang@duke.edu',
      url='https://stat.duke.edu/people/yixuan-wang',
      py_modules = ['sta663-yw261'],
      packages=setuptools.find_packages(),
      scripts = ['run_sta663_yw261.py'],
      python_requires='>=3',
      )