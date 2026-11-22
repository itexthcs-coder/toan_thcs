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


def bt_dang16_p2_b5_c3_hh8(self):
    # Khai báo biến
    bo_dinh = random.choice([
        ('A', 'B', 'C', 'M', 'E', 'K', 'N', 'D'),
        ('A', 'B', 'C', 'M', 'P', 'H', 'Q', 'I')
    ])
    A, B, C, M, E, K, N, D = bo_dinh

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2.5,2.8);
\\coordinate (B) at (1.3,0);
\\coordinate (C) at (3.7,0);
\\coordinate (M) at (-0.2,0);
\\coordinate (E) at (3.12,1.35);
\\coordinate (K) at (3.32,0.88);
\\coordinate (N) at (1.13,0.54);
\\coordinate (D) at (1.07,-0.54);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(C) (M)--(E) (B)--(K) (B)--(N) (M)--(D) (B)--(D);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (M) circle (1pt) node[left] {$%s$};
\\fill (E) circle (1pt) node[right] {$%s$};
\\fill (K) circle (1pt) node[right] {$%s$};
\\fill (N) circle (1pt) node[above left] {$%s$};
\\fill (D) circle (1pt) node[below] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, M, E, K, N, D))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $%s%s%s$ cân tại $%s$; $%s$ là một điểm thuộc đường thẳng $%s%s$ sao cho $%s$ nằm giữa $%s$ và $%s$. Gọi $%s, %s$ lần lượt là chân đường vuông góc hạ từ $%s$ và $%s$ xuống $%s%s$; $%s, %s$ lần lượt là chân đường vuông góc hạ từ $%s$ xuống $%s%s$ và từ $%s$ xuống $%s%s$. Xét tính đúng sai của các khẳng định sau:%s'''
                     % (A, B, C, A, M, B, C, B, M, C, E, K, M, B, A, C, N, D, B, M, E, M, A, B, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình chữ nhật' % (B, K, E, N)
    nb_da_1_s = 'Tứ giác $%s%s%s%s$ là hình thoi nhưng không phải hình chữ nhật' % (B, K, E, N)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta có $\\widehat{%s%s%s} = 90^\\circ$ ($%s%s \\perp %s%s$), $\\widehat{%s%s%s} = 90^\\circ$ ($%s%s \\perp %s%s$) và $\\widehat{%s%s%s} = 90^\\circ$ ($%s%s \\perp %s%s$).\\\\
Tứ giác $%s%s%s%s$ có ba góc vuông nên là hình chữ nhật.'''
                    % (B, K, E, B, K, A, C, K, E, N, M, E, A, C, E, N, B, B, N, M, E, B, K, E, N))

    # Ý b)
    th_da_1_d = '\\True $\\widehat{%s%s%s} = \\widehat{%s%s%s}$' % (N, B, M, D, B, M)
    th_da_1_s = '$\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$' % (N, B, M, D, B, M)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $%s%s%s%s$ là hình chữ nhật nên $%s%s // %s%s$, suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc đồng vị).\\\\
Mặt khác tam giác $%s%s%s$ cân tại $%s$ nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$, và $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc đối đỉnh).\\\\
Do đó $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.'''
                    % (B, K, E, N, B, N, A, C, N, B, M, A, C, B,
                       A, B, C, A, A, C, B, A, B, C, A, B, C, D, B, M,
                       N, B, M, D, B, M))

    # Ý c)
    vd_da_1_d = '\\True $%s%s = %s%s$' % (M, N, M, D)
    vd_da_1_s = '$%s%s = 2%s%s$' % (M, N, M, D)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Xét hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có cạnh huyền $%s%s$ chung và $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.h - g.n), do đó $%s%s = %s%s$.'''
                    % (M, N, B, M, D, B, B, M, N, B, M, D, B, M,
                       M, N, B, M, D, B, M, N, M, D))

    # Ý d)
    vdc_da_1_d = '\\True Khi điểm $%s$ di chuyển trên tia đối của tia $%s%s$ thì hiệu khoảng cách $%s%s - %s%s$ luôn không đổi và bằng $%s%s$' % (M, B, C, M, E, M, D, B, K)
    vdc_da_1_s = 'Khi điểm $%s$ di chuyển trên tia đối của tia $%s%s$ thì hiệu khoảng cách $%s%s - %s%s$ thay đổi tỉ lệ thuận với độ dài $%s%s$' % (M, B, C, M, E, M, D, M, B)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $%s%s - %s%s = %s%s - %s%s = %s%s$.\\\\
Vì $%s%s%s%s$ là hình chữ nhật nên $%s%s = %s%s$.\\\\
Do tam giác $%s%s%s$ cố định nên đường cao $%s%s$ không đổi, vậy $%s%s - %s%s = %s%s$ luôn không đổi.'''
                     % (M, E, M, D, M, E, M, N, E, N,
                        B, K, E, N, E, N, B, K,
                        A, B, C, B, K, M, E, M, D, B, K))

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
