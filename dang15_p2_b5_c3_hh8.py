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


def bt_dang15_p2_b5_c3_hh8(self):
    # Khai báo biến
    canh_hv = randint(5, 12)
    bo_dinh = random.choice([
        ('A', 'B', 'C', 'D', 'E', 'M', 'N', 'K'),
        ('A', 'B', 'C', 'D', 'E', 'P', 'Q', 'K')
    ])
    A, B, C, D, E, M, N, K = bo_dinh

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (2.6,2.6);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0,0);
\\coordinate (E) at (2.1,0);
\\coordinate (M) at (0.85,0);
\\coordinate (N) at (2.6,1.25);
\\coordinate (K) at (-1.35,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(E) (A)--(M) (M)--(N) (A)--(N);
\\draw[line width=1pt, dashed] (D)--(K) (A)--(K);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\draw[line width=1pt] (2.4,2.6)--(2.4,2.4)--(2.6,2.4);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below] {$%s$};
\\fill (E) circle (1pt) node[below] {$%s$};
\\fill (M) circle (1pt) node[below] {$%s$};
\\fill (N) circle (1pt) node[right] {$%s$};
\\fill (K) circle (1pt) node[left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, E, M, N, K))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình vuông $%s%s%s%s$ có cạnh bằng $%s\\text{ cm}$. Lấy điểm $%s$ nằm trên cạnh $%s%s$ ($%s$ khác $%s, %s$). Tia phân giác của $\\widehat{%s%s%s}$ cắt cạnh $%s%s$ tại $%s$. Đường thẳng qua $%s$ vuông góc với $%s%s$ cắt cạnh $%s%s$ tại $%s$. Trên tia đối của tia $%s%s$ lấy điểm $%s$ sao cho $%s%s = %s%s$. Xét tính đúng sai của các khẳng định sau:%s'''
                     % (A, B, C, D, canh_hv, E, C, D, E, C, D, D, A, E, D, C, M, M, A, E, B, C, N, D, C, K, D, K, B, N, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c)' % (A, D, K, A, B, N)
    nb_da_1_s = '$\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c)' % (A, D, K, A, D, M)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Xét hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có:\\\\
$%s%s = %s%s$ (cạnh hình vuông $%s%s%s%s$); $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$; $%s%s = %s%s$ (giả thiết).\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c).'''
                    % (A, D, K, A, B, N, A, D, A, B, A, B, C, D, A, D, K, A, B, N, D, K, B, N, A, D, K, A, B, N))

    # Ý b)
    th_da_1_d = '\\True $\\widehat{%s%s%s} = \\widehat{%s%s%s}$' % (K, M, A, N, M, A)
    th_da_1_s = '$\\widehat{%s%s%s} = 2\\widehat{%s%s%s}$' % (K, M, A, N, M, A)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Từ $\\Delta %s%s%s = \\Delta %s%s%s$ suy ra $%s%s = %s%s$ và $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\
Ta có $\\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ - \\widehat{%s%s%s} + \\widehat{%s%s%s}$.\\\\
Vì $%s%s$ là phân giác của $\\widehat{%s%s%s}$ nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$, từ đó suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ bằng nhau theo trường hợp c.h - c.g.v).'''
                    % (A, D, K, A, B, N, A, K, A, N, D, A, K, B, A, N,
                       K, A, M, K, A, D, D, A, M, B, A, N, D, A, M, B, A, N, D, A, M,
                       A, M, D, A, E, D, A, M, M, A, E, K, M, A, N, M, A, A, K, M, A, N, M))

    # Ý c)
    vd_da_1_d = '\\True $%s%s = %s%s + %s%s$' % (M, N, D, M, B, N)
    vd_da_1_s = '$%s%s = %s%s - %s%s$' % (M, N, D, M, B, N)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Từ $\\Delta %s%s%s = \\Delta %s%s%s$ suy ra $%s%s = %s%s$.\\\\
Vì điểm $%s$ nằm giữa hai điểm $%s$ và $%s$ nên $%s%s = %s%s + %s%s$.\\\\
Mà $%s%s = %s%s$ nên $%s%s = %s%s + %s%s$.'''
                    % (A, K, M, A, N, M, K, M, M, N,
                       D, K, M, K, M, D, M, D, K,
                       D, K, B, N, M, N, D, M, B, N))

    # Ý d)
    vdc_da_1_d = '\\True Chu vi của tam giác $%s%s%s$ luôn bằng $%s\\text{ cm}$' % (M, C, N, 2 * canh_hv)
    vdc_da_1_s = 'Chu vi của tam giác $%s%s%s$ luôn bằng $%s\\text{ cm}$' % (M, C, N, canh_hv)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Chu vi của tam giác $%s%s%s$ là: $%s%s + %s%s + %s%s = %s%s + %s%s + (%s%s + %s%s) = (%s%s + %s%s) + (%s%s + %s%s) = %s%s + %s%s = %s + %s = %s\\text{ (cm)}$.'''
                     % (M, C, N, M, C, C, N, M, N, M, C, C, N, D, M, B, N, D, M, M, C, B, N, C, N, D, C, B, C, canh_hv, canh_hv, 2 * canh_hv))

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
