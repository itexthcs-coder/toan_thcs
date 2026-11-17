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


def bt_dang9_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    k = random.randint(1, 3)
    R = 9 * k
    r = 4 * k
    oo1 = 15 * k
    so1 = 12 * k
    so = 27 * k
    ab_expr = sqrt(oo1**2 - (R - r)**2)

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (3.75,0);
\\coordinate (S) at (6.75,0);
\\coordinate (A) at (0.75,2.12);
\\coordinate (B) at (4.08,0.94);
\\coordinate (A') at (0.75,-2.12);
\\coordinate (B') at (4.08,-0.94);
\\draw[line width=1pt] (O) circle (2.25cm);
\\draw[line width=1pt] (O') circle (1cm);
\\draw[line width=1pt] (O)--(S);
\\draw[line width=1pt] (A)--(S) (A')--(S);
\\draw[line width=1pt] (O)--(A) (O')--(B);
\\draw[line width=1pt, dashed] (A)--(A') (O)--(A') (O')--(B');
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O') circle (1pt) node[below] {$O'$};
\\fill (S) circle (1pt) node[right] {$S$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (A') circle (1pt) node[below] {$A'$};
\\fill (B') circle (1pt) node[below] {$B'$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Cho hai đường tròn ngoài nhau $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ có đoạn nối tâm $OO' = %s\\text{ cm}$. Một tiếp tuyến chung ngoài tiếp xúc với $(O)$ tại $A$, tiếp xúc với $(O')$ tại $B$ ($O$ và $O'$ nằm cùng phía đối với $AB$) và cắt đường thẳng $OO'$ tại $S$.
%s""" % (fmt(R), fmt(r), fmt(oo1), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Tỉ số khoảng cách $\\frac{SO}{SO\'}$ bằng $\\frac{9}{4}$'
    nb_da_1_s = 'Tỉ số khoảng cách $\\frac{SO}{SO\'}$ bằng $\\frac{4}{9}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì $AB$ tiếp xúc với $(O)$ tại $A$ và $(O')$ tại $B$ nên $OA \\perp SA$ và $O'B \\perp SB$, suy ra $O'B // OA$. \\\\ Theo hệ quả định lí Thalès trong tam giác $SOA$, ta có: $\\frac{SO}{SO'} = \\frac{OA}{O'B} = \\frac{%s}{%s} = \\frac{9}{4}$.""" % (fmt(R), fmt(r)))

    # Thông hiểu
    th_da_1_d = '\\True Độ dài đoạn thẳng $SO\'$ bằng $%s\\text{ cm}$' % (fmt(so1))
    th_da_1_s = 'Độ dài đoạn thẳng $SO\'$ bằng $%s\\text{ cm}$' % (fmt(so))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Ta có $\\frac{SO}{SO'} = \\frac{9}{4} \\Rightarrow \\frac{SO - SO'}{SO'} = \\frac{9 - 4}{4} = \\frac{5}{4}$. \\\\ Mà $SO - SO' = OO' = %s\\text{ cm}$ nên $SO' = \\frac{4}{5} \\cdot %s = %s\\text{ cm}$.""" % (fmt(oo1), fmt(oo1), fmt(so1)))

    # Vận dụng
    vd_da_1_d = '\\True Độ dài đoạn tiếp tuyến chung $AB$ bằng $%s\\text{ cm}$' % (latex(ab_expr))
    vd_da_1_s = 'Độ dài đoạn tiếp tuyến chung $AB$ bằng $%s\\text{ cm}$' % (fmt(oo1))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Độ dài đoạn tiếp tuyến chung ngoài $AB$ được tính theo công thức: $AB = \\sqrt{OO'^2 - (R - r)^2} = \\sqrt{%s^2 - (%s - %s)^2} = \\sqrt{%s} = %s\\text{ cm}$.""" % (fmt(oo1), fmt(R), fmt(r), fmt(oo1**2 - (R - r)**2), latex(ab_expr)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu $A\'$ là điểm đối xứng với $A$ qua $OO\'$ thì đường thẳng $SA\'$ tiếp xúc với cả hai đường tròn $(O)$ và $(O\')$'
    vdc_da_1_s = 'Nếu $A\'$ là điểm đối xứng với $A$ qua $OO\'$ thì đường thẳng $SA\'$ không tiếp xúc với đường tròn $(O\')$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Do tính đối xứng trục qua đường nối tâm $OO'$, điểm $A'$ đối xứng với $A$ qua $OO'$ thuộc $(O)$ và $SA'$ là ảnh đối xứng của tiếp tuyến chung ngoài $SA$ qua $OO'$. Do đó $SA'$ cũng là tiếp tuyến chung ngoài của cả hai đường tròn $(O)$ và $(O')$.""")

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
