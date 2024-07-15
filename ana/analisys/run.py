import sys
import os

sys.path.append(os.getcwd())

from ana.core.Nodes import Nodes
# from ana.core.Bars import Bars
# from ana.utils.Area import Area
# from ana.utils.Centroid import Centroid
from ana.parse.Parse import LoadFile

data = LoadFile(sys.argv[1]).toJson()