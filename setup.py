from setuptools import setup
setup(
  name = 'Topsis-Ajaipaul-101917033',         # How you named your package folder (MyLib)
  packages = ['Topsis-Ajaipaul-101917033'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Topsis package python',   # Give a short description about your library
  author = 'Ajaipaul Singh Bajwa',                   # Type in your name
  author_email = 'ajayrko2001@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Bajwa-Ajai/Topsis.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Bajwa-Ajai/Topsis/archive/refs/heads/main.zip',    # I explain this later on
  keywords = ['Python', 'Topsis','UCS654'],   # Keywords that define your package best

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)