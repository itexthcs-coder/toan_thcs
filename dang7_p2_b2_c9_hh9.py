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

def bt_dang7_p2_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        af = randint(2, 4)
        bf = randint(3, 5)
        ce = randint(4, 6)
        ab = af + bf
        ac = af + ce
        bc = bf + ce

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (I) at (1.62,0.9);
\\coordinate (D) at (1.62,0);
\\coordinate (E) at (2.44,1.25);
\\coordinate (F) at (0.84,1.4);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.9);
\\draw[line width=1pt, dashed] (I)--(D) (I)--(E) (I)--(F);
\\fill (I) circle (1pt) node[above] {$I$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (F) circle (1pt) node[left] {$F$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác $%s%s%s$ có ba đường phân giác trong đồng quy tại $I$. Gọi $D, E, F$ lần lượt là chân các đường vuông góc kẻ từ $I$ xuống các cạnh $%s%s, %s%s, %s%s$. Xét tính đúng, sai của các khẳng định sau:%s''' % (A, B, C, B, C, C, A, A, B, hinh_ve))

        ######################################################################## Nhận biết ############################################
        nb_da_1_d = '\\True Ba đoạn thẳng $ID, IE, IF$ có độ dài bằng nhau'
        nb_da_1_s = 'Ba đoạn thẳng $I%s, I%s, I%s$ có độ dài bằng nhau' % (A, B, C)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        list_nb_1 = [nb_da_1]
        loigiai_nb_1 = ('''Vì $I$ là giao điểm ba đường phân giác trong của tam giác $%s%s%s$ nên $I$ cách đều ba cạnh của tam giác, suy ra $ID = IE = IF$.''' % (A, B, C))
        list_nb_2 = [loigiai_nb_1]

        ######################################################################## Thông hiểu ############################################
        th_da_1_d = '\\True Đường tròn $(I; ID)$ tiếp xúc với ba cạnh $%s%s, %s%s, %s%s$ lần lượt tại $D, E, F$' % (B, C, C, A, A, B)
        th_da_1_s = 'Đường tròn $(I; ID)$ đi qua ba đỉnh $%s, %s, %s$' % (A, B, C)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        list_th_1 = [th_da_1]
        loigiai_th_1 = ('''Vì $ID = IE = IF$ và $ID \\perp %s%s$, $IE \\perp %s%s$, $IF \\perp %s%s$ nên đường tròn $(I; ID)$ tiếp xúc với ba cạnh $%s%s, %s%s, %s%s$ lần lượt tại $D, E, F$.''' % (B, C, C, A, A, B, B, C, C, A, A, B))
        list_th_2 = [loigiai_th_1]

        ######################################################################## Vận dụng ############################################
        vd_da_1_d = '\\True Khi $%sF = %s\\text{ cm}$ thì $%sE = %s\\text{ cm}$' % (A, af, A, af)
        vd_da_1_s = 'Khi $%sF = %s\\text{ cm}$ thì $%sF = %s\\text{ cm}$' % (A, af, B, af)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        list_vd_1 = [vd_da_1]
        loigiai_vd_1 = ('''Theo tính chất hai tiếp tuyến cắt nhau của đường tròn $(I)$, ta có $%sE = %sF = %s\\text{ cm}$.''' % (A, A, af))
        list_vd_2 = [loigiai_vd_1]

        ######################################################################## Vận dụng cao ############################################
        vdc_da_1_d = '\\True Nếu $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$ thì $%sD = %s\\text{ cm}$' % (A, B, ab, A, C, ac, B, C, bc, B, bf)
        vdc_da_1_s = 'Nếu $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$ thì $%sD = %s\\text{ cm}$' % (A, B, ab, A, C, ac, B, C, bc, B, ce)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        list_vdc_1 = [vdc_da_1]
        loigiai_vdc_1 = ('''Đặt $%sF = %sE = x$. Ta có $%sF = %sD = %s - x$ và $%sE = %sD = %s - x$.\\\\
Vì $%sD + %sD = %s%s$ nên $(%s - x) + (%s - x) = %s \\Rightarrow 2x = %s \\Rightarrow x = %s\\text{ (cm)}$.\\\\
Suy ra $%sD = %s - %s = %s\\text{ (cm)}$.''' % (A, A, B, B, ab, C, C, ac, B, C, B, C, ab, ac, bc, ab + ac - bc, af, B, ab, af, bf))
        list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
