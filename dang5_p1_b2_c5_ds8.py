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


def bt_dang5_p1_b2_c5_ds8(self):
    # Dạng 5 (Nhận biết): Đọc quy ước đơn vị trong biểu đồ tranh có hình vẽ minh họa
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        unit = random.choice([5, 10, 15, 20])
        c_t6 = random.randint(2, 4)
        c_t7 = random.randint(3, 5)
        c_cn = random.randint(4, 6)
        while c_cn == c_t6 or c_cn == c_t7:
            c_cn = random.randint(4, 6)
            
        ans = c_cn * unit
        
        icons_t6 = "".join([f"\\draw[line width=1pt] ({1.2 + i*0.65}, 2.2) circle (0.22);" for i in range(c_t6)])
        icons_t7 = "".join([f"\\draw[line width=1pt] ({1.2 + i*0.65}, 1.4) circle (0.22);" for i in range(c_t7)])
        icons_cn = "".join([f"\\draw[line width=1pt] ({1.2 + i*0.65}, 0.6) circle (0.22);" for i in range(c_cn)])
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (-1.5, 0.1) rectangle (5.6, 2.7);
        \\draw[line width=1pt] (0.6, 0.1) -- (0.6, 2.7);
        \\draw[line width=1pt] (-1.5, 1.8) -- (5.6, 1.8);
        \\draw[line width=1pt] (-1.5, 1.0) -- (5.6, 1.0);
        \\node at (-0.45, 2.2) {Thứ Sáu};
        \\node at (-0.45, 1.4) {Thứ Bảy};
        \\node at (-0.45, 0.6) {Chủ nhật};
        %s
        %s
        %s
        \\draw[line width=1pt] (0.5, -0.35) circle (0.18);
        \\node[right] at (0.8, -0.35) {ứng với $%s$ chiếc xe đạp};
        \\end{tikzpicture}
        \\end{center}""" % (icons_t6, icons_t7, icons_cn, unit))
        
        du = ['$%s$ chiếc' % ans]
        da = random.choice(du)
        s = [
            '$%s$ chiếc' % (c_cn + unit),
            '$%s$ chiếc' % c_cn,
            '$%s$ chiếc' % ((c_cn + 1) * unit),
            '$%s$ chiếc' % ((c_cn - 1) * unit)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Biểu đồ tranh dưới đây thống kê số lượng xe đạp bán được của một cửa hàng trong ba ngày cuối tuần (mỗi hình tròn ứng với $%s$ chiếc xe đạp). Nếu ngày Chủ nhật có $%s$ biểu tượng thì số xe đạp bán được trong ngày Chủ nhật là bao nhiêu?%s"""
                         % (unit, c_cn, tikz_code))
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Quan sát biểu đồ tranh, ta thấy:\\\\
    - Mỗi biểu tượng hình tròn ứng với $%s$ chiếc xe đạp.\\\\
    - Ngày Chủ nhật có $%s$ biểu tượng nên số xe đạp bán được trong ngày Chủ nhật là: $%s \\cdot %s = %s$ (chiếc)."""
                   % (unit, c_cn, c_cn, unit, ans))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
