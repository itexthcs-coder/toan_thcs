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


def bt_dang16_p1_b2_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_so = random.choice([
            ([28, 37, 30, 10, 15], 120, 2, 25),
            ([24, 36, 20, 12, 8], 100, 1, 36),
            ([30, 45, 36, 24, 15], 150, 2, 24)
        ])
        vals, tong, idx, kq = bo_so
        co_giay = [36, 37, 38, 39, 40]
        co_chon = co_giay[idx]
        m_chon = vals[idx]

        hinh_cot = f'''\\begin{{center}}
        \\begin{{tikzpicture}}[scale=0.8]
        \\draw[->] (0,0) -- (6.2,0) node[right] {{\\footnotesize Cỡ giày}};
        \\draw[->] (0,0) -- (0,4.8) node[above] {{\\footnotesize Số học sinh}};
        \\foreach \\y/\\lbl in {{1/10, 2/20, 3/30, 4/40}}
            \\draw[gray!40] (0,\\y) -- (5.8,\\y) node[left, black] at (0,\\y) {{\\footnotesize \\lbl}};
        \\foreach \\x/\\v/\\c in {{1/{vals[0]}/36, 2/{vals[1]}/37, 3/{vals[2]}/38, 4/{vals[3]}/39, 5/{vals[4]}/40}} {{
            \\fill[blue!60] (\\x-0.25, 0) rectangle (\\x+0.25, \\v/10);
            \\node[above] at (\\x, \\v/10) {{\\footnotesize \\v}};
            \\node[below] at (\\x, 0) {{\\footnotesize \\c}};
        }}
        \\node[above] at (3, 5.1) {{\\textbf{{Cỡ giày của các bạn nam khối lớp 9}}}};
        \\end{{tikzpicture}}
        \\end{{center}}'''

        # Các đáp án trắc nghiệm
        du = [f'${kq}\\%$']
        da = random.choice(du)
        s = list(set([f'${m_chon}\\%$', f'${kq + 5}\\%$', f'${kq - 5}\\%$', f'${100 - kq}\\%$']) - set(du))
        das1, das2, das3 = random.sample(s, 3)

        # Câu hỏi
        noidungcauhoi = f'''Biểu đồ cột dưới đây cho biết cỡ giày của các bạn nam khối lớp 9 trong một trường:{hinh_cot}Tần số tương đối của các bạn nam đi giày cỡ ${co_chon}$ là'''

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = f'''Từ biểu đồ cột, tổng số bạn nam khối 9 được khảo sát là:
        $$ n = {vals[0]} + {vals[1]} + {vals[2]} + {vals[3]} + {vals[4]} = {tong} \\text{{ (học sinh)}}. $$
        Số bạn nam đi giày cỡ ${co_chon}$ là $m = {m_chon}$. Vậy tần số tương đối tương ứng là:
        $$ f = \\frac{{{m_chon}}}{{{tong}}} \\cdot 100\\% = {kq}\\%. $$'''

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
