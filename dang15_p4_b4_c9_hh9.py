# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang15_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (105:1.8);
\\coordinate (B) at (215:1.8);
\\coordinate (C) at (-35:1.8);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (N) at ($(C)!0.5!(A)$);
\\coordinate (P) at ($(A)!0.5!(B)$);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt, dashed] (O)--(M) (O)--(N) (O)--(P);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[above right] {$N$};
\\fill (P) circle (1pt) node[above left] {$P$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho tam giác nhọn $ABC$ nội tiếp đường tròn tâm $O$ (như hình vẽ). Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $BC, CA, AB$. Chứng minh rằng ba tứ giác $ANOP, BPOM, CMON$ đều là các tứ giác nội tiếp và xác định tâm của các đường tròn ngoại tiếp ba tứ giác đó. %s'''
                         % (hinh_tikz))

        loigiai = ('''Xét đường tròn $(O)$ có các dây cung $BC, CA, AB$ không đi qua tâm $O$. \\\\
Vì $M, N, P$ lần lượt là trung điểm của các dây cung $BC, CA, AB$ nên theo quan hệ vuông góc giữa đường kính và dây cung, ta có:
$$OM \\perp BC, \\qquad ON \\perp CA, \\qquad OP \\perp AB.$$
Suy ra $\\widehat{OMC} = \\widehat{OMB} = 90^\\circ$, $\\widehat{ONA} = \\widehat{ONC} = 90^\\circ$, $\\widehat{OPA} = \\widehat{OPB} = 90^\\circ$. \\\\
- Xét tứ giác $ANOP$ có $\\widehat{OPA} + \\widehat{ONA} = 90^\\circ + 90^\\circ = 180^\\circ$, nên $ANOP$ là tứ giác nội tiếp đường tròn đường kính $OA$ (tâm là trung điểm của $OA$). \\\\
- Xét tứ giác $BPOM$ có $\\widehat{OPB} + \\widehat{OMB} = 90^\\circ + 90^\\circ = 180^\\circ$, nên $BPOM$ là tứ giác nội tiếp đường tròn đường kính $OB$ (tâm là trung điểm của $OB$). \\\\
- Xét tứ giác $CMON$ có $\\widehat{OMC} + \\widehat{ONC} = 90^\\circ + 90^\\circ = 180^\\circ$, nên $CMON$ là tứ giác nội tiếp đường tròn đường kính $OC$ (tâm là trung điểm của $OC$).''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
