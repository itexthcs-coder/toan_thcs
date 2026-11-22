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


def bt_dang14_p2_b5_c3_hh8(self):
    # Khai báo biến
    bo_dinh = random.choice([
        ('A', 'B', 'C', 'M', 'N', 'P', 'Q'),
        ('D', 'E', 'F', 'I', 'H', 'K', 'G')
    ])
    A, B, C, M, N, P, Q = bo_dinh

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,2.2);
\\coordinate (C) at (3.2,0);
\\coordinate (M) at (1.6,1.1);
\\coordinate (N) at (0,1.1);
\\coordinate (P) at (1.6,0);
\\coordinate (Q) at (1.6,-1.1);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (M)--(Q) (A)--(M) (A)--(Q)--(C);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\draw[line width=1pt] (0,1.3)--(0.2,1.3)--(0.2,1.1);
\\draw[line width=1pt] (1.6,0.2)--(1.8,0.2)--(1.8,0);
\\fill (A) circle (1pt) node[left] {$%s$};
\\fill (B) circle (1pt) node[above] {$%s$};
\\fill (C) circle (1pt) node[right] {$%s$};
\\fill (M) circle (1pt) node[above right] {$%s$};
\\fill (N) circle (1pt) node[left] {$%s$};
\\fill (P) circle (1pt) node[below left] {$%s$};
\\fill (Q) circle (1pt) node[below] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, M, N, P, Q))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ ($%s%s < %s%s$), $%s$ là trung điểm của $%s%s$. Hạ $%s%s \\perp %s%s$ ($%s \\in %s%s$), $%s%s \\perp %s%s$ ($%s \\in %s%s$). Lấy điểm $%s$ sao cho $%s$ là trung điểm của $%s%s$. Xét tính đúng sai của các khẳng định sau:%s'''
                     % (A, B, C, A, A, B, A, C, M, B, C, M, P, A, C, P, A, C, M, N, A, B, N, A, B, Q, P, M, Q, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình chữ nhật và $%s, %s$ lần lượt là trung điểm của $%s%s, %s%s$' % (A, P, M, N, N, P, A, B, A, C)
    nb_da_1_s = 'Tứ giác $%s%s%s%s$ là hình vuông với mọi tam giác vuông $%s%s%s$' % (A, P, M, N, A, B, C)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tứ giác $%s%s%s%s$ có $\\widehat{%s} = \\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$ nên là hình chữ nhật.\\\\
Vì $%s%s // %s%s$ và $%s$ là trung điểm của $%s%s$ nên $%s$ là trung điểm của $%s%s$.\\\\
Tương tự, $%s%s // %s%s$ và $%s$ là trung điểm của $%s%s$ nên $%s$ là trung điểm của $%s%s$.'''
                    % (A, P, M, N, A, A, P, M, A, N, M,
                       M, P, A, B, M, B, C, P, A, C,
                       M, N, A, C, M, B, C, N, A, B))

    # Ý b)
    th_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình thoi' % (A, M, C, Q)
    th_da_1_s = 'Tứ giác $%s%s%s%s$ là hình chữ nhật có hai đường chéo không vuông góc' % (A, M, C, Q)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tứ giác $%s%s%s%s$ có hai đường chéo $%s%s$ và $%s%s$ cắt nhau tại trung điểm $%s$ của mỗi đường nên là hình bình hành.\\\\
Mặt khác $%s%s \\perp %s%s$ tại $%s$ nên hình bình hành $%s%s%s%s$ là hình thoi.'''
                    % (A, M, C, Q, A, C, M, Q, P,
                       M, Q, A, C, P, A, M, C, Q))

    # Ý c)
    vd_da_1_d = '\\True Chu vi của hình thoi $%s%s%s%s$ bằng $2%s%s$' % (A, M, C, Q, B, C)
    vd_da_1_s = 'Chu vi của hình thoi $%s%s%s%s$ bằng $%s%s$' % (A, M, C, Q, B, C)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong tam giác $%s%s%s$ vuông tại $%s$, $%s%s$ là đường trung tuyến ứng với cạnh huyền $%s%s$ nên $%s%s = \\dfrac{1}{2}%s%s$.\\\\
Vì $%s%s%s%s$ là hình thoi nên chu vi của nó bằng $4%s%s = 4 \\cdot \\dfrac{1}{2}%s%s = 2%s%s$.'''
                    % (A, B, C, A, A, M, B, C, A, M, B, C,
                       A, M, C, Q, A, M, B, C, B, C))

    # Ý d)
    vdc_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình vuông khi và chỉ khi $\\widehat{%s%s%s} = 45^\\circ$' % (A, M, C, Q, A, B, C)
    vdc_da_1_s = 'Tứ giác $%s%s%s%s$ là hình vuông khi và chỉ khi $\\widehat{%s%s%s} = 60^\\circ$' % (A, M, C, Q, A, B, C)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Hình thoi $%s%s%s%s$ là hình vuông $\\Leftrightarrow \\widehat{%s%s%s} = 90^\\circ \\Leftrightarrow %s%s \\perp %s%s$.\\\\
Khi đó $%s%s$ vừa là đường trung tuyến vừa là đường cao của tam giác $%s%s%s$, nên tam giác $%s%s%s$ vuông cân tại $%s$, tương đương $\\widehat{%s%s%s} = 45^\\circ$.'''
                     % (A, M, C, Q, A, M, C, A, M, B, C,
                        A, M, A, B, C, A, B, C, A, A, B, C))

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
