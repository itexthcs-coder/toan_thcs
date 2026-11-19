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


def bt_dang1_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ten_hv = random.choice(["ABCD", "MNPQ"])
        a, b, c, d = ten_hv[0], ten_hv[1], ten_hv[2], ten_hv[3]
        anh_hv = "EFGH" if ten_hv == "ABCD" else "RSTU"
        e, f, g, h = anh_hv[0], anh_hv[1], anh_hv[2], anh_hv[3]
        ten_bg = "%s%s%s%s%s%s%s%s" % (e, a, f, b, g, c, h, d)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (E) at (45:1.7);
\\coordinate (D) at (0:1.7);
\\coordinate (H) at (-45:1.7);
\\coordinate (C) at (-90:1.7);
\\coordinate (G) at (-135:1.7);
\\coordinate (B) at (180:1.7);
\\coordinate (F) at (135:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (E)--(A)--(F)--(B)--(G)--(C)--(H)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(B)--(C)--(D)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (E) circle (1pt) node[above right] {$%s$};
\\fill (D) circle (1pt) node[right] {$%s$};
\\fill (H) circle (1pt) node[below right] {$%s$};
\\fill (C) circle (1pt) node[below] {$%s$};
\\fill (G) circle (1pt) node[below left] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (F) circle (1pt) node[above left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (a, e, d, h, c, g, b, f)

        noidungcauhoi = ('''Biết rằng bốn đỉnh $%s, %s, %s, %s$ của một hình vuông cùng nằm trên một đường tròn tâm $O$ theo thứ tự ngược chiều quay của kim đồng hồ. Phép quay thuận chiều $45^\\circ$ tâm $O$ biến các điểm $%s, %s, %s, %s$ lần lượt thành các điểm $%s, %s, %s, %s$ (như hình vẽ). Chứng minh rằng đa giác $%s$ là một bát giác đều. %s'''
                         % (a, b, c, d, a, b, c, d, e, f, g, h, ten_bg, hinh_tikz))

        loigiai = ('''Vì $%s%s%s%s$ là hình vuông nội tiếp đường tròn $(O)$ theo thứ tự ngược chiều kim đồng hồ nên các đỉnh $%s, %s, %s, %s$ nằm trên $(O)$ theo thứ tự thuận chiều kim đồng hồ và bốn cung nhỏ $%s%s, %s%s, %s%s, %s%s$ đều có số đo bằng $\\frac{360^\\circ}{4} = 90^\\circ$. \\
Phép quay thuận chiều $45^\\circ$ tâm $O$ biến các điểm $%s, %s, %s, %s$ lần lượt thành $%s, %s, %s, %s$ nên các điểm $%s, %s, %s, %s$ cũng thuộc đường tròn $(O)$ và lần lượt là điểm chính giữa của các cung nhỏ $%s%s, %s%s, %s%s, %s%s$. \\
Do đó, tám điểm $%s, %s, %s, %s, %s, %s, %s, %s$ chia đường tròn $(O)$ thành $8$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $45^\\circ$. \\
Suy ra tám cạnh của đa giác lồi $%s$ là các dây căng các cung bằng nhau nên bằng nhau:
$$%s%s = %s%s = %s%s = %s%s = %s%s = %s%s = %s%s = %s%s.$$
Mặt khác, mỗi góc trong của đa giác $%s$ là góc nội tiếp chắn $6$ cung nhỏ liên tiếp của $(O)$ nên đều có số đo bằng $\\frac{6 \\cdot 45^\\circ}{2} = 135^\\circ$. \\
Vậy đa giác $%s$ có tất cả các cạnh bằng nhau và các góc bằng nhau nên $%s$ là một bát giác đều.'''
                   % (a, b, c, d, a, d, c, b, a, d, d, c, c, b, b, a,
                      a, b, c, d, e, f, g, h, e, f, g, h, a, d, b, a, c, b, d, c,
                      e, a, f, b, g, c, h, d, ten_bg,
                      e, a, a, f, f, b, b, g, g, c, c, h, h, d, d, e,
                      ten_bg, ten_bg, ten_bg))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
