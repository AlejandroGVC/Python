"""
Esta función nos permite transformar un path en una uri.
Ejemplos de path que puede transformar:

'~/examples/file.txt' --> 'file:///home/<user>/examples/file.txt'
'$HADOOP_HOME/sbin' --> 'file:///usr/local/hadoop.3.2.0/sbin'
'./file.txt' --> 'file:///<actual path>/file.txt'
"""

import os
import pathlib
def toUri(path):
    """Return file:// URL from a filename."""
    path = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
    return pathlib.Path(path).as_uri()