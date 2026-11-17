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


def bt_dang5_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    k = random.randint(1, 3)
    R = 8 * k
    r = 3 * k
    oo1 = R - r
    km = 4 * k
    kn = Rational(R * km, r)
    mn = kn - km

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (2.2,0);
\\coordinate (K) at (3.6,0);
\\coordinate (M) at (1.5,1.21);
\\coordinate (N) at (-2.0,3.0);
\\draw[line width=1pt] (O) circle (3.6cm);
\\draw[line width=1pt] (O') circle (1.4cm);
\\draw[line width=1pt] (O)--(K)--(N);
\\draw[line width=1pt] (O')--(M) (O)--(N);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (O') circle (1pt) node[below] {$O'$};
\\fill (K) circle (1pt) node[right] {$K$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (N) circle (1pt) node[above left] {$N$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc trong tại điểm $K$. Một đường thẳng đi qua $K$ cắt đường tròn $(O')$ tại $M$ và cắt đường tròn $(O)$ tại $N$ ($M, N \\ne K$).
%s""" % (fmt(R), fmt(r), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Ba điểm $O, O\', K$ thẳng hàng và điểm $O\'$ nằm giữa $O$ và $K$'
    nb_da_1_s = 'Ba điểm $O, O\', K$ thẳng hàng và điểm $O$ nằm giữa $O\'$ và $K$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì hai đường tròn $(O)$ và $(O')$ tiếp xúc trong tại $K$ nên tiếp điểm $K$ thẳng hàng với hai tâm $O, O'$ và $O'$ nằm giữa $O, K$ (do $OK = %s\\text{ cm} > O'K = %s\\text{ cm}$).""" % (fmt(R), fmt(r)))

    # Thông hiểu
    th_da_1_d = '\\True Độ dài đoạn nối tâm $OO\'$ bằng $%s\\text{ cm}$' % (fmt(oo1))
    th_da_1_s = 'Độ dài đoạn nối tâm $OO\'$ bằng $%s\\text{ cm}$' % (fmt(R + r))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì $O'$ nằm giữa $O$ và $K$ nên độ dài đoạn nối tâm là $OO' = OK - O'K = %s - %s = %s\\text{ cm}$.""" % (fmt(R), fmt(r), fmt(oo1)))

    # Vận dụng
    vd_da_1_d = '\\True Hai bán kính $O\'M$ và $ON$ song song với nhau'
    vd_da_1_s = 'Hai bán kính $O\'M$ và $ON$ vuông góc với nhau'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Tam giác $O'KM$ cân tại $O'$ ($O'K = O'M$) nên $\\widehat{O'KM} = \\widehat{O'MK}$. Tam giác $OKN$ cân tại $O$ ($OK = ON$) nên $\\widehat{OKN} = \\widehat{ONK}$. \\\\ Vì $O'$ nằm trên đoạn $OK$ và $M$ nằm trên đoạn $KN$ nên $\\widehat{O'KM} = \\widehat{OKN}$, suy ra $\\widehat{O'MK} = \\widehat{ONK}$. Hai góc này ở vị trí đồng vị nên $O'M // ON$.""")

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu $KM = %s\\text{ cm}$ thì độ dài đoạn thẳng $MN$ bằng $%s\\text{ cm}$' % (fmt(km), latex(mn))
    vdc_da_1_s = 'Nếu $KM = %s\\text{ cm}$ thì độ dài đoạn thẳng $MN$ bằng $%s\\text{ cm}$' % (fmt(km), latex(kn))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Vì $O'M // ON$, theo hệ quả của định lí Thalès trong tam giác $OKN$, ta có: $\\frac{KM}{KN} = \\frac{O'M}{ON} = \\frac{%s}{%s}$. \\\\ Suy ra $KN = \\frac{%s \\cdot %s}{%s} = %s\\text{ cm}$. Do đó $MN = KN - KM = %s - %s = %s\\text{ cm}$.""" % (fmt(r), fmt(R), fmt(R), fmt(km), fmt(r), latex(kn), latex(kn), fmt(km), latex(mn)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
