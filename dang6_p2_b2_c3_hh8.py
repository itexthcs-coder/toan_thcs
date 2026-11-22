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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang6_p2_b2_c3_hh8(self):
    bo_dinh = [('M', 'N', 'P', 'Q', 'O'), ('A', 'B', 'C', 'D', 'I'), ('E', 'F', 'G', 'H', 'K')]
    d1, d2, d3, d4, giao = random.choice(bo_dinh)
    ten_ht = d1 + d2 + d3 + d4
    day1, day2 = d1 + d2, d3 + d4
    dc1, dc2 = d1 + d3, d2 + d4
    do_dai = random.choice([8, 10, 12, 14])
    nua_str = str(do_dai // 2)

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (3.6,0);
    \\coordinate (A) at (0.8,1.8);
    \\coordinate (B) at (2.8,1.8);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
    \\fill (A) circle (1pt) node[above left] {$%s$};
    \\fill (B) circle (1pt) node[above right] {$%s$};
    \\fill (C) circle (1pt) node[below right] {$%s$};
    \\fill (D) circle (1pt) node[below left] {$%s$};
    \\fill (O) circle (1pt) node[above] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4, giao)

    noidungcauhoi = ('''Cho hình thang cân $%s$ ($%s // %s$, $%s < %s$) có hai đường chéo $%s$ và $%s$ cắt nhau tại $%s$, biết $%s = %s\\text{ cm}$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_ht, day1, day2, day1, day2, dc1, dc2, giao, dc1, do_dai, hinh_ve))

    nb_da_1_d = '\\True Đường chéo $%s$ có độ dài bằng $%s\\text{ cm}$' % (dc2, do_dai)
    nb_da_1_s = 'Đường chéo $%s$ có độ dài bằng $%s\\text{ cm}$' % (dc2, do_dai + 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Theo Định lí $2$, trong hình thang cân hai đường chéo bằng nhau nên $%s = %s = %s\\text{ cm}$.''' % (dc2, dc1, do_dai))

    th_da_1_d = '\\True Điểm $%s$ không phải là trung điểm của đoạn thẳng $%s$' % (giao, dc1)
    th_da_1_s = 'Điểm $%s$ luôn là trung điểm của đoạn thẳng $%s$' % (giao, dc1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $%s < %s$ nên $%s < %s$, do đó $%s$ không phải là trung điểm của $%s$.''' % (day1, day2, giao+d1, giao+d3, giao, dc1))

    vd_da_1_d = '\\True Hai tam giác $%s%s%s$ và $%s%s%s$ bằng nhau' % (d1, d3, d4, d2, d4, d3)
    vd_da_1_s = 'Hai tam giác $%s%s%s$ và $%s%s%s$ không bằng nhau' % (d1, d3, d4, d2, d4, d3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Hai tam giác $\\triangle %s%s%s$ và $\\triangle %s%s%s$ bằng nhau theo trường hợp cạnh – góc – cạnh (hoặc cạnh – cạnh – cạnh).''' % (d1, d3, d4, d2, d4, d3))

    vdc_da_1_d = '\\True Độ dài đoạn thẳng $%s$ không bằng $%s\\text{ cm}$' % (giao+d3, nua_str)
    vdc_da_1_s = 'Độ dài đoạn thẳng $%s$ luôn bằng $%s\\text{ cm}$' % (giao+d3, nua_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $%s$ không là trung điểm của $%s$ nên $%s \\neq %s\\text{ cm}$.''' % (giao, dc2, giao+d3, nua_str))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
