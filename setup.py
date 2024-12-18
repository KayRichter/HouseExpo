from setuptools import setup

setup(name='pseudoslam',
      version='0.0.1',
      description='A reinforcement learning environment for robot autonomous exploration',
      install_requires=['gymnasium', 'numpy', 'pyyaml', 'matplotlib', 'opencv-python'],
      packages=["pseudoslam"],
      )
