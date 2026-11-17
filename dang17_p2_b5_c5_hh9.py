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


def bt_dang17_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    R = random.choice([50, 100, 150, 200])
    r_expr = R * (sqrt(2) - 1)

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O1) at (1.0355,1.0355);
\\coordinate (O2) at (-1.0355,1.0355);
\\coordinate (O3) at (-1.0355,-1.0355);
\\coordinate (O4) at (1.0355,-1.0355);
\\draw[line width=1pt] (O) circle (2.5cm);
\\draw[line width=1pt] (O1) circle (1.0355cm);
\\draw[line width=1pt] (O2) circle (1.0355cm);
\\draw[line width=1pt] (O3) circle (1.0355cm);
\\draw[line width=1pt] (O4) circle (1.0355cm);
\\draw[line width=1pt, dashed] (O1)--(O2)--(O3)--(O4)--cycle (O1)--(O3) (O2)--(O4);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (O1) circle (1pt) node[above right] {$O_1$};
\\fill (O2) circle (1pt) node[above left] {$O_2$};
\\fill (O3) circle (1pt) node[below left] {$O_3$};
\\fill (O4) circle (1pt) node[below right] {$O_4$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Một ô cửa sổ kiến trúc có khung ngoài là đường tròn $(O; %s\\text{ cm})$. Bên trong khung, kiến trúc sư bố trí $4$ ô kính tròn nhỏ bằng nhau tâm $O_1, O_2, O_3, O_4$ có cùng bán kính $r$, sao cho mỗi ô kính nhỏ đều tiếp xúc trong với khung tròn $(O)$ và tiếp xúc ngoài với hai ô kính nhỏ kề nó.
%s""" % (fmt(R), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Khoảng cách từ tâm $O$ đến tâm của mỗi ô kính nhỏ bằng $%s - r\\text{ (cm)}$' % (fmt(R))
    nb_da_1_s = 'Khoảng cách từ tâm $O$ đến tâm của mỗi ô kính nhỏ bằng $%s + r\\text{ (cm)}$' % (fmt(R))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì mỗi ô kính nhỏ bán kính $r$ tiếp xúc trong với khung tròn $(O; %s\\text{ cm})$ nên khoảng cách từ tâm $O$ đến tâm $O_i$ ($i = 1, 2, 3, 4$) bằng $OO_i = %s - r\\text{ (cm)}$.""" % (fmt(R), fmt(R)))

    # Thông hiểu
    th_da_1_d = '\\True Khoảng cách giữa tâm của hai ô kính nhỏ kề nhau bằng $2r\\text{ (cm)}$'
    th_da_1_s = 'Khoảng cách giữa tâm của hai ô kính nhỏ kề nhau bằng $r\\sqrt{2}\\text{ (cm)}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì hai ô kính nhỏ kề nhau có cùng bán kính $r$ và tiếp xúc ngoài với nhau nên khoảng cách giữa hai tâm của chúng bằng $r + r = 2r\\text{ (cm)}$.""")

    # Vận dụng
    vd_da_1_d = '\\True Tâm của $4$ ô kính nhỏ tạo thành một hình vuông có tâm đối xứng là điểm $O$'
    vd_da_1_s = 'Tâm của $4$ ô kính nhỏ tạo thành một hình thoi có hai đường chéo không bằng nhau'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Tứ giác $O_1O_2O_3O_4$ có bốn cạnh bằng nhau (cùng bằng $2r$) và bốn đỉnh cách đều điểm $O$ (cùng bằng $%s - r$) nên hai đường chéo $O_1O_3$ và $O_2O_4$ bằng nhau và cắt nhau tại trung điểm $O$. Vậy $O_1O_2O_3O_4$ là hình vuông tâm $O$.""" % (fmt(R)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Bán kính $r$ của mỗi ô kính nhỏ bằng $%s\\text{ cm}$' % (latex(r_expr))
    vdc_da_1_s = 'Bán kính $r$ của mỗi ô kính nhỏ bằng $%s\\text{ cm}$' % (fmt(R // 2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Đường chéo của hình vuông $O_1O_2O_3O_4$ cạnh $2r$ có độ dài là $O_1O_3 = 2r\\sqrt{2}$. Mặt khác $O_1O_3 = OO_1 + OO_3 = 2(%s - r)$. \\\\ Ta có phương trình: $2r\\sqrt{2} = 2(%s - r) \\Leftrightarrow r(\\sqrt{2} + 1) = %s \\Leftrightarrow r = \\frac{%s}{\\sqrt{2} + 1} = %s\\text{ cm}$.""" % (fmt(R), fmt(R), fmt(R), fmt(R), latex(r_expr)))

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
