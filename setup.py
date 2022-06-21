from setuptools import setup, find_packages

setup(name='OpcDa',
      version='1.2.1',
      description='Package to OPC',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      keywords='OPCDA',
      url='https://github.com/PockusaevAndrey/pyOpcDa',
      author='Pockusaev Andrey',
      author_email='pockusaevandrey@yandex.ru',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'pypiwin32',
      ],
      include_package_data=True,
      zip_safe=False)
