from setuptools import setup, find_packages

setup(name='OpcDa',
      version='0.1',
      description='Package to OPC',
      long_description='realize DCOM Interfaces of OPC DA 2.0',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='opc da',
      url='http://github.com/storborg/funniest',
      author='Pockusaev Andrey',
      author_email='pockusaevandrey@yandex.ru',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'pypiwin32',
      ],
      include_package_data=True,
      zip_safe=False)