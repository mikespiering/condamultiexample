# cf-mbp-java-python-dependencies
A simple demo app for Multi-Buildpack (Java &amp; Python) with Python having additional dependencies.

Reproducing module not found error

Changes:
1. Manfiest should have buildpacks: with the buildpacks in order, run buildpack last
2. If no command is set in manifest, it can default to the first buildback (python in this case) and try and run that command. For java that needs to be empty.
3. Pom.xml needs to bring in the environment.yml as well as the vendor folder for conda
4. CF commandline must be newer than v6.38.0 - released aug 8, 2018
5. PCF instance must support multibuildpacks- supported since at least pcf 2.2

May still need to set LD_LIBRARY_PATH and PYTHONPATH 