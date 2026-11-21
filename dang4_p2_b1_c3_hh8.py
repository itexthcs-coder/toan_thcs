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


def bt_dang4_p2_b1_c3_hh8(self):
    bo_dinh = [
        ('A', 'B', 'C', 'D', 'An', 'Bình'),
        ('M', 'N', 'P', 'Q', 'Minh', 'Lan'),
        ('E', 'F', 'G', 'H', 'Hoa', 'Nam')
    ]
    d1, d2, d3, d4, ten1, ten2 = random.choice(bo_dinh)
    ten_tg = d1 + d2 + d3 + d4
    dc1, dc2 = d1 + d3, d2 + d4

    hinh_ve = '''
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3.2,0);
    \\coordinate (C) at (2.7,2.1);
    \\coordinate (D) at (0.4,1.9);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
    \\draw[line width=1pt, dashed] (A)--(C);
    \\fill (A) circle (1pt) node[below left] {$%s$};
    \\fill (B) circle (1pt) node[below right] {$%s$};
    \\fill (C) circle (1pt) node[above right] {$%s$};
    \\fill (D) circle (1pt) node[above left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (d1, d2, d3, d4)

    noidungcauhoi = ('''Để tính tổng số đo bốn góc $\\widehat{%s} + \\widehat{%s} + \\widehat{%s} + \\widehat{%s}$ của tứ giác $%s$, bạn %s kẻ đường chéo $%s$ chia tứ giác thành hai tam giác $%s%s%s$ và $%s%s%s$ (như hình vẽ). Xét tính đúng, sai của các khẳng định sau: %s'''
                     % (d1, d2, d3, d4, ten_tg, ten1, dc1, d1, d2, d3, d1, d4, d3, hinh_ve))

    nb_da_1_d = '\\True Tổng các góc trong tam giác $%s%s%s$ là $\\widehat{%s%s%s} + \\widehat{%s} + \\widehat{%s%s%s} = 180^\\circ$' % (d1, d2, d3, d2, d1, d3, d2, d2, d3, d1)
    nb_da_1_s = 'Tổng các góc trong tam giác $%s%s%s$ là $\\widehat{%s%s%s} + \\widehat{%s} + \\widehat{%s%s%s} = 360^\\circ$' % (d1, d2, d3, d2, d1, d3, d2, d2, d3, d1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Áp dụng định lí về tổng ba góc trong một tam giác đối với tam giác $%s%s%s$, ta có $\\widehat{%s%s%s} + \\widehat{%s} + \\widehat{%s%s%s} = 180^\\circ$.'''
                    % (d1, d2, d3, d2, d1, d3, d2, d2, d3, d1))

    th_da_1_d = '\\True Góc $\\widehat{%s%s%s}$ của tứ giác bằng tổng hai góc $\\widehat{%s%s%s} + \\widehat{%s%s%s}$' % (d2, d1, d4, d2, d1, d3, d3, d1, d4)
    th_da_1_s = 'Góc $\\widehat{%s%s%s}$ của tứ giác bằng hiệu hai góc $\\widehat{%s%s%s} - \\widehat{%s%s%s}$' % (d2, d1, d4, d2, d1, d3, d3, d1, d4)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì tia $%s%s$ nằm giữa hai tia $%s%s$ và $%s%s$ trong tứ giác lồi $%s$ nên $\\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s}$.'''
                    % (d1, d3, d1, d2, d1, d4, ten_tg, d2, d1, d4, d2, d1, d3, d3, d1, d4))

    vd_da_1_d = '\\True Tổng bốn góc của tứ giác $%s$ bằng tổng các góc của hai tam giác $%s%s%s$ và $%s%s%s$ nên bằng $360^\\circ$' % (ten_tg, d1, d2, d3, d1, d4, d3)
    vd_da_1_s = 'Tổng bốn góc của tứ giác $%s$ bằng tổng các góc của hai tam giác $%s%s%s$ và $%s%s%s$ nên bằng $180^\\circ$' % (ten_tg, d1, d2, d3, d1, d4, d3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Cộng tổng ba góc của tam giác $%s%s%s$ ($180^\\circ$) và tổng ba góc của tam giác $%s%s%s$ ($180^\\circ$), ta được tổng bốn góc của tứ giác $%s$ bằng $180^\\circ + 180^\\circ = 360^\\circ$.'''
                    % (d1, d2, d3, d1, d4, d3, ten_tg))

    vdc_da_1_d = '\\True Nếu bạn %s kẻ đường chéo $%s$ thay vì đường chéo $%s$ thì tổng bốn góc thu được của tứ giác $%s$ vẫn bằng $360^\\circ$' % (ten2, dc2, dc1, ten_tg)
    vdc_da_1_s = 'Nếu bạn %s kẻ đường chéo $%s$ thay vì đường chéo $%s$ thì tổng bốn góc thu được của tứ giác $%s$ sẽ thay đổi' % (ten2, dc2, dc1, ten_tg)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Dù kẻ đường chéo $%s$ hay đường chéo $%s$, tứ giác lồi $%s$ đều được chia thành hai tam giác nên tổng các góc của tứ giác luôn không đổi và bằng $360^\\circ$.'''
                     % (dc1, dc2, ten_tg))

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
