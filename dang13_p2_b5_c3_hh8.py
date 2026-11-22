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


def bt_dang13_p2_b5_c3_hh8(self):
    # Khai báo biến
    bo_dinh = random.choice([
        ('A', 'B', 'C', 'D', 'P'),
        ('M', 'N', 'P', 'Q', 'E')
    ])
    A, B, C, D, P = bo_dinh

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (2.2,0);
\\coordinate (P) at (4.4,0);
\\coordinate (D) at (0,2.2);
\\coordinate (C) at (2.2,2.2);
\\draw[line width=1pt] (A)--(P)--(C)--(D)--cycle (B)--(C) (B)--(D);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[below left] {$%s$};
\\fill (B) circle (1pt) node[below] {$%s$};
\\fill (P) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[above left] {$%s$};
\\fill (C) circle (1pt) node[above right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, P, D, C))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình bình hành $%s%s%s%s$. Lấy điểm $%s$ trên tia $%s%s$ sao cho $%s%s = 2%s%s$ ($%s$ nằm giữa $%s$ và $%s$). Xét tính đúng sai của các khẳng định sau:%s'''
                     % (A, B, C, D, P, A, B, A, P, A, B, B, A, P, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True $%s%s = %s%s$ và $%s%s // %s%s$' % (B, P, C, D, B, P, C, D)
    nb_da_1_s = '$%s%s = 2%s%s$ và $%s%s // %s%s$' % (B, P, C, D, B, P, C, D)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $%s$ nằm giữa $%s$ và $%s$ mà $%s%s = 2%s%s$ nên $%s%s = %s%s$.\\\\
Mặt khác $%s%s%s%s$ là hình bình hành nên $%s%s = %s%s$ và $%s%s // %s%s$.\\\\
Do đó $%s%s = %s%s$ và $%s%s // %s%s$.'''
                    % (B, A, P, A, P, A, B, B, P, A, B,
                       A, B, C, D, A, B, C, D, A, B, C, D,
                       B, P, C, D, B, P, C, D))

    # Ý b)
    th_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình bình hành' % (B, P, C, D)
    th_da_1_s = 'Tứ giác $%s%s%s%s$ là hình thang cân nhưng không phải hình bình hành' % (B, P, C, D)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tứ giác $%s%s%s%s$ có hai cạnh đối $%s%s // %s%s$ và $%s%s = %s%s$ nên là hình bình hành.'''
                    % (B, P, C, D, B, P, C, D, B, P, C, D))

    # Ý c)
    vd_da_1_d = '\\True Nếu tam giác $%s%s%s$ vuông cân tại $%s$ thì tứ giác $%s%s%s%s$ là hình chữ nhật' % (A, B, D, A, B, P, C, D)
    vd_da_1_s = 'Nếu tam giác $%s%s%s$ vuông cân tại $%s$ thì tứ giác $%s%s%s%s$ là hình thoi' % (A, B, D, A, B, P, C, D)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Khi tam giác $%s%s%s$ vuông cân tại $%s$ thì $\\widehat{%s} = 90^\\circ$ và $%s%s = %s%s$.\\\\
Hình bình hành $%s%s%s%s$ có $\\widehat{%s} = 90^\\circ$ và $%s%s = %s%s$ nên là hình vuông, suy ra $%s%s \\perp %s%s$ và $%s%s = %s%s$.\\\\
Vì $%s%s%s%s$ là hình bình hành nên $%s%s // %s%s$, kết hợp với $%s%s \\perp %s%s$ suy ra $\\widehat{%s%s%s} = 90^\\circ$.\\\\
Hình bình hành $%s%s%s%s$ có một góc vuông nên là hình chữ nhật (và hai cạnh kề $%s%s = %s%s$ nên $%s%s%s%s$ còn là hình vuông).'''
                    % (A, B, D, A, A, A, B, A, D,
                       A, B, C, D, A, A, B, A, D, B, D, A, C, B, D, A, C,
                       B, P, C, D, B, D, P, C, B, D, A, C, B, D, C,
                       B, P, C, D, B, D, C, D, B, P, C, D))

    # Ý d)
    vdc_da_1_d = '\\True Khi tam giác $%s%s%s$ vuông cân tại $%s$, số đo góc $\\widehat{%s%s%s}$ bằng $45^\\circ$' % (A, B, D, A, B, P, D)
    vdc_da_1_s = 'Khi tam giác $%s%s%s$ vuông cân tại $%s$, số đo góc $\\widehat{%s%s%s}$ bằng $60^\\circ$' % (A, B, D, A, B, P, D)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi tam giác $%s%s%s$ vuông cân tại $%s$ thì $\\widehat{%s%s%s} = 45^\\circ$.\\\\
Vì $%s%s%s%s$ là hình bình hành nên $%s%s // %s%s$, suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 45^\\circ$ (hai góc đồng vị).'''
                     % (A, B, D, A, A, B, D,
                        B, P, C, D, B, D, P, C, B, P, C, A, B, D))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
