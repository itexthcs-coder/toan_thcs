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


def bt_dang2_p2_b1_c4_hh8(self):
    a = random.randint(2, 4)
    b = a + 1
    k = random.randint(3, 6)
    ab = (a + b) * k
    ma = a * k
    mb = b * k
    na = a * ab
    nb = b * ab
    mn = na + ma
    ts_mn_ab = Rational(mn, ab)

    noidungcauhoi = ("""Trên đoạn thẳng $AB = %s\\text{ cm}$ lấy điểm $M$ sao cho $\\dfrac{MA}{MB} = \\dfrac{%s}{%s}$. Lấy điểm $N$ nằm trên tia đối của tia $BA$ sao cho $\\dfrac{NA}{NB} = \\dfrac{%s}{%s}$ (như hình vẽ bên dưới). Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (N) at (0,0);
\\coordinate (A) at (3.2,0);
\\coordinate (M) at (4.4,0);
\\coordinate (B) at (6.0,0);
\\draw[line width=1pt] (N)--(B);
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (B) circle (1pt) node[below] {$B$};
\\end{tikzpicture}
\\end{center}"""
                     % (ab, a, b, a, b))

    nb_da_1_d = '\\True Độ dài đoạn thẳng $MA$ bằng $%s\\text{ cm}$' % (ma)
    nb_da_1_s = 'Độ dài đoạn thẳng $MA$ bằng $%s\\text{ cm}$' % (mb)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì điểm $M$ nằm trên đoạn thẳng $AB$ và $\\dfrac{MA}{MB} = \\dfrac{%s}{%s}$ nên $MA = \\dfrac{%s}{%s + %s} AB = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$."""
                    % (a, b, a, a, b, a, a + b, ab, ma))

    th_da_1_d = '\\True Độ dài đoạn thẳng $MB$ bằng $%s\\text{ cm}$' % (mb)
    th_da_1_s = 'Độ dài đoạn thẳng $MB$ bằng $%s\\text{ cm}$' % (mb - 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Ta có $MB = AB - MA = %s - %s = %s\\text{ (cm)}$."""
                    % (ab, ma, mb))

    vd_da_1_d = '\\True Độ dài đoạn thẳng $NB$ bằng $%s\\text{ cm}$' % (nb)
    vd_da_1_s = 'Độ dài đoạn thẳng $NB$ bằng $%s\\text{ cm}$' % (na)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Vì điểm $N$ nằm trên tia đối của tia $BA$ nên điểm $A$ nằm giữa hai điểm $N$ và $B$, suy ra $NB - NA = AB = %s\\text{ cm}$. \\\\ Kết hợp với $\\dfrac{NA}{NB} = \\dfrac{%s}{%s}$ ta có $\\dfrac{NB - NA}{NB} = \\dfrac{%s - %s}{%s} = \\dfrac{1}{%s} \\Rightarrow NB = %s \\cdot %s = %s\\text{ (cm)}$."""
                    % (ab, a, b, b, a, b, b, b, ab, nb))

    vdc_da_1_d = '\\True Tỉ số $\\dfrac{MN}{AB}$ bằng $%s$' % (latex(ts_mn_ab))
    vdc_da_1_s = 'Tỉ số $\\dfrac{MN}{AB}$ bằng $%s$' % (latex(Rational(na, ab)))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Ta có $NA = NB - AB = %s - %s = %s\\text{ (cm)}$. \\\\ Vì điểm $A$ nằm giữa $N$ và $M$ nên $MN = NA + AM = %s + %s = %s\\text{ (cm)}$. \\\\ Suy ra $\\dfrac{MN}{AB} = \\dfrac{%s}{%s} = %s$."""
                     % (nb, ab, na, na, ma, mn, mn, ab, latex(ts_mn_ab)))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
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
