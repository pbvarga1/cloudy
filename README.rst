======
cloudy
======

Parses the output files of the spectral synthesis code Cloudy into Pandas
DataFrames for analysis.

Example
+++++++

Here is a quick example. See sample_data for an ipythpn notebook example::

  >>> from cloudy import cloudy
  >>> sample = cloudy.Cloudy(
    'sample_data/sample.grd', 'sample_data/sample.ems')
  >>> sample.labels
  ['H  1  6563A',
   'N  2  6584A',
   'O  1  6300A',
   'S  2  6720A',
   'Temperature',
   'depth']


Todos
-----

* Write Docs

