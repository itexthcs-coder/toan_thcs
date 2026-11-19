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


def bt_dang1_p2_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        ten = random.choice(['Tuấn', 'Nam', 'Khoa', 'Huy'])
        hinh_ve = '''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.5cm);
\\draw[line width=1pt] (-1.06,1.06)--(1.06,-1.06);
\\draw[line width=1pt] (-1.06,-1.06)--(1.06,1.06);
\\draw[line width=1pt, ->] (0,0)--(0,-1.1);
\\fill (0,0) circle (1pt);
\\node at (0,0.9) {$1$};
\\node at (0.9,0) {$2$};
\\node at (0,-0.9) {$3$};
\\node at (-0.9,0) {$4$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Một tấm bìa cứng hình tròn được chia làm $4$ hình quạt bằng nhau, đánh số $1; 2; 3; 4$ và được gắn vào trục quay có mũi tên ở tâm như hình vẽ. Bạn %s quay tấm bìa hai lần liên tiếp, quan sát và ghi lại số của hình quạt mà mũi tên chỉ vào.%s''' % (ten, hinh_ve))

        # Ý a
        nb_da_1_d = '\\True Không gian mẫu $\\Omega$ của phép thử có $16$ phần tử'
        nb_da_1_s = 'Không gian mẫu $\\Omega$ của phép thử có $8$ phần tử'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Mỗi lần quay có $4$ khả năng xảy ra nên quay $2$ lần liên tiếp có $4 \\cdot 4 = 16$ kết quả có thể. Vậy $n(\\Omega) = 16$.''')

        # Ý b
        th_da_1_d = '\\True Các kết quả thuận lợi cho biến cố $E$: ``Tổng hai số ghi trên hai hình quạt ở hai lần quay bằng $5$'' là $(1, 4); (2, 3); (3, 2); (4, 1)$'
        th_da_1_s = 'Chỉ có $2$ kết quả thuận lợi cho biến cố $E$: ``Tổng hai số ghi trên hai hình quạt ở hai lần quay bằng $5$'' là $(1, 4)$ và $(2, 3)$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Các cặp số $(a, b)$ với $a, b \\in \\{1; 2; 3; 4\\}$ thỏa mãn $a + b = 5$ gồm: $(1, 4); (2, 3); (3, 2); (4, 1)$. Có tất cả $4$ kết quả thuận lợi.''')

        # Ý c
        vd_da_1_d = '\\True Xác suất của biến cố $F$: ``Tích hai số ghi trên hai hình quạt ở hai lần quay bằng $4$'' là $\\dfrac{3}{16}$'
        vd_da_1_s = 'Xác suất của biến cố $F$: ``Tích hai số ghi trên hai hình quạt ở hai lần quay bằng $4$'' là $\\dfrac{1}{4}$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Các kết quả thuận lợi cho biến cố $F$ ($a \\cdot b = 4$) là: $(1, 4); (2, 2); (4, 1)$, suy ra $n(F) = 3$.\\\\
Vậy xác suất của biến cố $F$ là $P(F) = \\dfrac{n(F)}{n(\\Omega)} = \\dfrac{3}{16}$.''')

        # Ý d
        vdc_da_1_d = '\\True Xác suất của biến cố $G$: ``Số ghi ở lần quay thứ nhất lớn hơn số ghi ở lần quay thứ hai'' là $\\dfrac{3}{8}$'
        vdc_da_1_s = 'Xác suất của biến cố $G$: ``Số ghi ở lần quay thứ nhất lớn hơn số ghi ở lần quay thứ hai'' là $\\dfrac{1}{2}$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Các kết quả thuận lợi cho biến cố $G$ ($a > b$) là: $(2, 1); (3, 1); (3, 2); (4, 1); (4, 2); (4, 3)$, suy ra $n(G) = 6$.\\\\
Vậy xác suất của biến cố $G$ là $P(G) = \\dfrac{6}{16} = \\dfrac{3}{8}$.''')

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

        list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
