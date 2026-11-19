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


def bt_dang13_p2_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        b1, b2 = random.choice([('Nam', 'Bình'), ('Hùng', 'Dũng'), ('Lan', 'Vy')])
        hinh_ve = '''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.3cm);
\\draw[line width=1pt] (0,0)--(0,1.3);
\\draw[line width=1pt] (0,0)--(1.12,-0.65);
\\draw[line width=1pt] (0,0)--(-1.12,-0.65);
\\draw[line width=1pt, ->] (0,0)--(0,-0.95);
\\fill (0,0) circle (1pt);
\\node at (-0.65,0.45) {$1$};
\\node at (0.65,0.45) {$2$};
\\node at (0,-0.75) {$3$};
\\node at (0,-1.7) {Tấm bìa $A$};

\\draw[line width=1pt] (4,0) circle (1.3cm);
\\draw[line width=1pt] (4,0)--(4,1.3);
\\draw[line width=1pt] (4,0)--(5.24,0.4);
\\draw[line width=1pt] (4,0)--(4.76,-1.05);
\\draw[line width=1pt] (4,0)--(3.24,-1.05);
\\draw[line width=1pt] (4,0)--(2.76,0.4);
\\draw[line width=1pt, ->] (4,0)--(4,-0.95);
\\fill (4,0) circle (1pt);
\\node at (3.4,0.75) {$1$};
\\node at (4.6,0.75) {$2$};
\\node at (4.85,-0.25) {$3$};
\\node at (4,-0.85) {$4$};
\\node at (3.15,-0.25) {$5$};
\\node at (4,-1.7) {Tấm bìa $B$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Tấm bìa cứng $A$ hình tròn được chia thành $3$ hình quạt bằng nhau đánh số $1; 2; 3$ và tấm bìa cứng $B$ hình tròn được chia thành $5$ hình quạt bằng nhau đánh số $1; 2; 3; 4; 5$ như hình vẽ. Bạn %s quay tấm bìa $A$, bạn %s quay tấm bìa $B$ và quan sát số ở hình quạt mà hai mũi tên chỉ vào.%s''' % (b1, b2, hinh_ve))

        nb_da_1_d = '\\True Xác suất của biến cố $E$: ``Tích hai số ở hình quạt mà hai mũi tên chỉ vào bằng $6$'' là $\\dfrac{2}{15}$'
        nb_da_1_s = 'Xác suất của biến cố $E$: ``Tích hai số ở hình quạt mà hai mũi tên chỉ vào bằng $6$'' là $\\dfrac{1}{15}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Không gian mẫu $\\Omega$ có $3 \\cdot 5 = 15$ phần tử. Có $2$ kết quả thuận lợi cho biến cố $E$ là $(2, 3)$ và $(3, 2)$.\\\\
Vậy $P(E) = \\dfrac{2}{15}$.''')

        th_da_1_d = '\\True Xác suất của biến cố $F$: ``Tích hai số ở hình quạt mà hai mũi tên chỉ vào nhỏ hơn $5$'' là $\\dfrac{7}{15}$'
        th_da_1_s = 'Xác suất của biến cố $F$: ``Tích hai số ở hình quạt mà hai mũi tên chỉ vào nhỏ hơn $5$'' là $\\dfrac{2}{5}$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Các kết quả thuận lợi cho biến cố $F$ là $(1, 1); (1, 2); (1, 3); (1, 4); (2, 1); (2, 2); (3, 1)$, suy ra $n(F) = 7$.\\\\
Vậy $P(F) = \\dfrac{7}{15}$.''')

        vd_da_1_d = '\\True Xác suất của biến cố $G$: ``Tích hai số ở hình quạt mà hai mũi tên chỉ vào là số chẵn'' là $\\dfrac{3}{5}$'
        vd_da_1_s = 'Xác suất của biến cố $G$: ``Tích hai số ở hình quạt mà hai mũi tên chỉ vào là số chẵn'' là $\\dfrac{8}{15}$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Có $9$ kết quả thuận lợi cho biến cố $G$ là $(1, 2); (1, 4); (2, 1); (2, 2); (2, 3); (2, 4); (2, 5); (3, 2); (3, 4)$.\\\\
Vậy $P(G) = \\dfrac{9}{15} = \\dfrac{3}{5}$.''')

        vdc_da_1_d = '\\True Xác suất của biến cố $H$: ``Tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số chia hết cho $3$'' là $\\dfrac{1}{3}$'
        vdc_da_1_s = 'Xác suất của biến cố $H$: ``Tổng hai số ở hình quạt mà hai mũi tên chỉ vào là số chia hết cho $3$'' là $\\dfrac{4}{15}$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Các kết quả có tổng chia hết cho $3$ là $(1, 2); (1, 5); (2, 1); (2, 4); (3, 3)$, suy ra $n(H) = 5$.\\\\
Vậy $P(H) = \\dfrac{5}{15} = \\dfrac{1}{3}$.''')

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
