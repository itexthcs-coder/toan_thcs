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


def bt_dang12_p1_b2_c5_ds8(self):
    # Dạng 12 (Thông hiểu): Chuyển đổi biểu đồ tranh sang bảng thống kê và tính tổng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        unit = random.choice([3, 4, 5, 6])
        c1 = random.randint(3, 5)
        c2 = random.randint(4, 6)
        c3 = random.randint(2, 4)
        
        v1, v2, v3 = c1 * unit, c2 * unit, c3 * unit
        tong_vo = v1 + v2 + v3
        tong_bt = c1 + c2 + c3
        
        icons_1 = "".join([f"\\draw[line width=1pt] ({1.0 + i*0.55}, 2.2) rectangle ({1.32 + i*0.55}, 2.55);" for i in range(c1)])
        icons_2 = "".join([f"\\draw[line width=1pt] ({1.0 + i*0.55}, 1.4) rectangle ({1.32 + i*0.55}, 1.75);" for i in range(c2)])
        icons_3 = "".join([f"\\draw[line width=1pt] ({1.0 + i*0.55}, 0.6) rectangle ({1.32 + i*0.55}, 0.95);" for i in range(c3)])
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (-1.2, 0.2) rectangle (5.2, 2.8);
        \\draw[line width=1pt] (0.5, 0.2) -- (0.5, 2.8);
        \\draw[line width=1pt] (-1.2, 1.95) -- (5.2, 1.95);
        \\draw[line width=1pt] (-1.2, 1.15) -- (5.2, 1.15);
        \\node at (-0.35, 2.37) {Tổ 1};
        \\node at (-0.35, 1.57) {Tổ 2};
        \\node at (-0.35, 0.77) {Tổ 3};
        %s
        %s
        %s
        \\draw[line width=1pt] (0.5, -0.45) rectangle (0.82, -0.1);
        \\node[right] at (1.0, -0.28) {ứng với $%s$ quyển vở};
        \\end{tikzpicture}
        \\end{center}""" % (icons_1, icons_2, icons_3, unit))
        
        du = ['$%s$ quyển' % tong_vo]
        da = random.choice(du)
        s = [
            '$%s$ quyển' % tong_bt,
            '$%s$ quyển' % ((tong_bt + 1) * unit),
            '$%s$ quyển' % ((tong_bt - 1) * unit),
            '$%s$ quyển' % (tong_bt + unit)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Biểu đồ tranh dưới đây thống kê số quyển vở quyên góp của các tổ lớp 8B (mỗi biểu tượng quyển vở ứng với $%s$ quyển vở thực tế):%sTổng số quyển vở cả ba tổ quyên góp được là bao nhiêu?"""
                         % (unit, tikz_code))
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Từ biểu đồ tranh, ta lập được số quyển vở quyên góp của từng tổ như sau:\\\\
    - Tổ 1 có $%s$ biểu tượng nên quyên góp được: $%s \\cdot %s = %s$ (quyển).\\\\
    - Tổ 2 có $%s$ biểu tượng nên quyên góp được: $%s \\cdot %s = %s$ (quyển).\\\\
    - Tổ 3 có $%s$ biểu tượng nên quyên góp được: $%s \\cdot %s = %s$ (quyển).\\\\
    Tổng số quyển vở cả ba tổ quyên góp được là: $%s + %s + %s = %s$ (quyển)."""
                   % (c1, c1, unit, v1, c2, c2, unit, v2, c3, c3, unit, v3, v1, v2, v3, tong_vo))

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
