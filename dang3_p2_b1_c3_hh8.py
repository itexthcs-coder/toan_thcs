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


def bt_dang3_p2_b1_c3_hh8(self):
    bo_dinh = [
        ('E', 'F', 'G', 'H'),
        ('A', 'B', 'C', 'D'),
        ('M', 'N', 'P', 'Q'),
        ('K', 'L', 'M', 'N')
    ]
    d1, d2, d3, d4 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4
    ten_nguoc = d4 + d3 + d2 + d1
    dc1, dc2 = d1 + d3, d2 + d4

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3.4,0);
    \\coordinate (C) at (2.8,2.2);
    \\coordinate (D) at (0.4,1.9);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
    \\fill (A) circle (1pt) node[below left] {$%s$};
    \\fill (B) circle (1pt) node[below right] {$%s$};
    \\fill (C) circle (1pt) node[above right] {$%s$};
    \\fill (D) circle (1pt) node[above left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4)

    noidungcauhoi = ('''Cho tứ giác lồi $%s$ như hình vẽ dưới đây. Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (ten_tg, hinh_ve))

    nb_da_1_d = '\\True Tứ giác $%s$ cũng có thể đọc tên là tứ giác $%s$' % (ten_tg, ten_nguoc)
    nb_da_1_s = 'Tứ giác $%s$ không thể đọc tên là tứ giác $%s$' % (ten_tg, ten_nguoc)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Khi đọc tên tứ giác $%s$ theo chiều ngược lại xuất phát từ đỉnh $%s$, ta được thứ tự các đỉnh liên tiếp quanh tứ giác là $%s$ nên tứ giác $%s$ còn gọi là tứ giác $%s$.'''
                    % (ten_tg, d4, ten_nguoc, ten_tg, ten_nguoc))

    th_da_1_d = '\\True Trong tứ giác $%s$, đoạn thẳng $%s$ và đoạn thẳng $%s$ là hai đường chéo của tứ giác' % (ten_tg, dc1, dc2)
    th_da_1_s = 'Trong tứ giác $%s$, đoạn thẳng $%s$ và đoạn thẳng $%s$ là hai cạnh đối của tứ giác' % (ten_tg, dc1, dc2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Hai đoạn thẳng $%s$ và $%s$ nối các cặp đỉnh đối nhau của tứ giác nên chúng là hai đường chéo của tứ giác $%s$, không phải là hai cạnh đối.'''
                    % (dc1, dc2, ten_tg))

    vd_da_1_d = '\\True Hai góc $\\widehat{%s}$ và $\\widehat{%s}$ là cặp góc đối, đồng thời hai góc $\\widehat{%s}$ và $\\widehat{%s}$ cũng là cặp góc đối' % (d1, d3, d2, d4)
    vd_da_1_s = 'Hai góc $\\widehat{%s}$ và $\\widehat{%s}$ là cặp góc đối, còn hai góc $\\widehat{%s}$ và $\\widehat{%s}$ là cặp góc kề nhau' % (d1, d3, d2, d4)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong tứ giác $%s$, hai đỉnh $%s$ và $%s$ đối nhau nên $\\widehat{%s}$ và $\\widehat{%s}$ là cặp góc đối; hai đỉnh $%s$ và $%s$ đối nhau nên $\\widehat{%s}$ và $\\widehat{%s}$ cũng là cặp góc đối.'''
                    % (ten_tg, d1, d3, d1, d3, d2, d4, d2, d4))

    vdc_da_1_d = '\\True Hai đường chéo $%s$ và $%s$ cắt nhau tại một điểm nằm giữa mỗi đường' % (dc1, dc2)
    vdc_da_1_s = 'Hai đường chéo $%s$ và $%s$ luôn cắt nhau tại trung điểm của mỗi đường' % (dc1, dc2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Theo nhận xét trong bài học: Trong tứ giác lồi, hai đường chéo $%s$ và $%s$ cắt nhau tại một điểm nằm giữa mỗi đường (chỉ các tứ giác đặc biệt như hình bình hành mới cắt nhau tại trung điểm mỗi đường).'''
                     % (dc1, dc2))

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
