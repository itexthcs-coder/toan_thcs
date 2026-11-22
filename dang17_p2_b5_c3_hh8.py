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


def bt_dang17_p2_b5_c3_hh8(self):
    # Khai báo biến
    canh_a = random.choice([4, 6, 8, 10])
    dien_tich_hv = canh_a ** 2
    dien_tich_nua = dien_tich_hv // 2
    dien_tich_tu = dien_tich_hv // 4

    bo_dinh = random.choice([
        ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
        ('M', 'N', 'P', 'Q', 'E', 'F', 'G', 'H')
    ])
    A, B, C, D, E, F, G, H = bo_dinh

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (2.6,2.6);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0,0);
\\coordinate (E) at (0.8,2.6);
\\coordinate (F) at (2.6,1.8);
\\coordinate (G) at (1.8,0);
\\coordinate (H) at (0,0.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (E)--(F)--(G)--(H)--cycle;
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below left] {$%s$};
\\fill (E) circle (1pt) node[above] {$%s$};
\\fill (F) circle (1pt) node[right] {$%s$};
\\fill (G) circle (1pt) node[below] {$%s$};
\\fill (H) circle (1pt) node[left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, E, F, G, H))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình vuông $%s%s%s%s$ có cạnh bằng $%s\\text{ cm}$. Trên các cạnh $%s%s, %s%s, %s%s, %s%s$ lần lượt lấy các điểm $%s, %s, %s, %s$ sao cho $%s%s = %s%s = %s%s = %s%s = x$ ($0 < x < %s$). Xét tính đúng sai của các khẳng định sau:%s'''
                     % (A, B, C, D, canh_a, A, B, B, C, C, D, D, A, E, F, G, H, A, E, B, F, C, G, D, H, canh_a, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True $\\Delta %s%s%s = \\Delta %s%s%s = \\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c)' % (A, E, H, B, F, E, C, G, F, D, H, G)
    nb_da_1_s = '$\\Delta %s%s%s$ và $\\Delta %s%s%s$ là hai tam giác cân bằng nhau với mọi $x$' % (A, E, H, B, F, E)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta có $%s%s = %s%s = %s%s = %s%s = %s - x$ và $%s%s = %s%s = %s%s = %s%s = x$.\\\\
Bốn tam giác vuông $\\Delta %s%s%s, \\Delta %s%s%s, \\Delta %s%s%s, \\Delta %s%s%s$ có các cặp cạnh góc vuông tương ứng bằng nhau nên bằng nhau theo trường hợp (c.g.c).'''
                    % (A, H, B, E, C, F, D, G, canh_a, A, E, B, F, C, G, D, H, A, E, H, B, F, E, C, G, F, D, H, G))

    # Ý b)
    th_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình vuông với mọi giá trị của $x$ ($0 < x < %s$)' % (E, F, G, H, canh_a)
    th_da_1_s = 'Tứ giác $%s%s%s%s$ chỉ là hình thoi khi $x \\neq %s$' % (E, F, G, H, canh_a // 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Từ bốn tam giác vuông bằng nhau ở ý a suy ra $%s%s = %s%s = %s%s = %s%s$ nên $%s%s%s%s$ là hình thoi.\\\\
Lại có $\\widehat{%s%s%s} = 180^\\circ - (\\widehat{%s%s%s} + \\widehat{%s%s%s}) = 180^\\circ - (\\widehat{%s%s%s} + \\widehat{%s%s%s}) = 180^\\circ - 90^\\circ = 90^\\circ$.\\\\
Hình thoi $%s%s%s%s$ có một góc vuông nên là hình vuông.'''
                    % (E, F, F, G, G, H, H, E, E, F, G, H,
                       H, E, F, A, E, H, B, E, F, A, E, H, A, H, E,
                       E, F, G, H))

    # Ý c)
    vd_da_1_d = '\\True Diện tích tứ giác $%s%s%s%s$ luôn nhỏ hơn $%s\\text{ cm}^2$' % (E, F, G, H, dien_tich_hv)
    vd_da_1_s = 'Diện tích tứ giác $%s%s%s%s$ luôn bằng $%s\\text{ cm}^2$ với mọi $x$' % (E, F, G, H, dien_tich_hv)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Diện tích hình vuông $%s%s%s%s$ bằng $%s^2 = %s\\text{ (cm}^2)$.\\\\
Vì $0 < x < %s$ nên bốn tam giác vuông ở bốn góc đều có diện tích dương, do đó diện tích tứ giác $%s%s%s%s$ luôn nhỏ hơn $%s\\text{ cm}^2$.'''
                    % (A, B, C, D, canh_a, dien_tich_hv, canh_a, E, F, G, H, dien_tich_hv))

    # Ý d)
    vdc_da_1_d = '\\True Khi $x = %s\\text{ cm}$ thì diện tích tứ giác $%s%s%s%s$ bằng $%s\\text{ cm}^2$' % (canh_a // 2, E, F, G, H, dien_tich_nua)
    vdc_da_1_s = 'Khi $x = %s\\text{ cm}$ thì diện tích tứ giác $%s%s%s%s$ bằng $%s\\text{ cm}^2$' % (canh_a // 2, E, F, G, H, dien_tich_tu)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi $x = %s\\text{ cm}$ thì $%s, %s, %s, %s$ là trung điểm bốn cạnh hình vuông $%s%s%s%s$.\\\\
Diện tích mỗi tam giác vuông ở góc bằng $\\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2)$.\\\\
Vậy diện tích hình vuông $%s%s%s%s$ bằng $%s - 4 \\cdot %s = %s\\text{ (cm}^2)$.'''
                     % (canh_a // 2, E, F, G, H, A, B, C, D,
                        canh_a // 2, canh_a // 2, (canh_a // 2)**2 // 2,
                        E, F, G, H, dien_tich_hv, (canh_a // 2)**2 // 2, dien_tich_nua))

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
