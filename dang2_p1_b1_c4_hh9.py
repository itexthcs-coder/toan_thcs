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


def bt_dang2_p1_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tam_giac_list = [
            ('A', 'B', 'C', 'B', 'AC', 'AB', 'BC'),
            ('A', 'B', 'C', 'C', 'AB', 'AC', 'BC'),
            ('D', 'E', 'F', 'E', 'DF', 'DE', 'EF'),
            ('M', 'N', 'P', 'P', 'MN', 'MP', 'NP')
        ]
        A_v, B_v, C_v, goc_v, doi, ke, huyen = random.choice(tam_giac_list)

        ti_so_list = [
            ('\\dfrac{%s}{%s}' % (doi, huyen), '\\sin \\alpha', 'cạnh đối của góc $\\alpha$ và cạnh huyền'),
            ('\\dfrac{%s}{%s}' % (ke, huyen), '\\cos \\alpha', 'cạnh kề của góc $\\alpha$ và cạnh huyền'),
            ('\\dfrac{%s}{%s}' % (doi, ke), '\\tan \\alpha', 'cạnh đối và cạnh kề của góc $\\alpha$'),
            ('\\dfrac{%s}{%s}' % (ke, doi), '\\cot \\alpha', 'cạnh kề và cạnh đối của góc $\\alpha$')
        ]
        ti_so, dap_an_dung, mo_ta = random.choice(ti_so_list)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4,0);
\\coordinate (C) at (0,2.8);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);
\\fill (A) circle (1pt) node[below left] {$%s$};
\\fill (B) circle (1pt) node[below right] {$%s$};
\\fill (C) circle (1pt) node[above left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A_v, B_v, C_v))

        du = ['$%s$' % dap_an_dung]
        da = random.choice(du)
        tat_ca = ['$\\sin \\alpha$', '$\\cos \\alpha$', '$\\tan \\alpha$', '$\\cot \\alpha$']
        s = [item for item in tat_ca if item != da]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho $\\triangle %s%s%s$ vuông tại $%s$ có góc nhọn $%s = \\alpha$. Tỉ số $%s$ được gọi là
%s''' % (A_v, B_v, C_v, A_v, goc_v, ti_so, hinh_ve))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Xét $\\triangle %s%s%s$ vuông tại $%s$ có góc nhọn $%s = \\alpha$. \\\\
Ta có cạnh đối của góc $\\alpha$ là $%s$, cạnh kề của góc $\\alpha$ là $%s$ và cạnh huyền là $%s$. \\\\
Theo định nghĩa tỉ số lượng giác của góc nhọn, tỉ số giữa %s là $%s = %s$.'''
                   % (A_v, B_v, C_v, A_v, goc_v, doi, ke, huyen, mo_ta, dap_an_dung, ti_so))

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
