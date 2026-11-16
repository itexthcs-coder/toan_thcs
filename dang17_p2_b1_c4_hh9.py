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


def bt_dang17_p2_b1_c4_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = symbols('a', positive=True)
        he_so = random.choice([1, 2, 3, 4])
        canh_thoi = he_so * a
        BD_expr = canh_thoi
        AC_expr = canh_thoi * sqrt(3)

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (A) at (-2.4,0);\n"
            "\\coordinate (C) at (2.4,0);\n"
            "\\coordinate (B) at (0,1.38);\n"
            "\\coordinate (D) at (0,-1.38);\n"
            "\\coordinate (O) at (0,0);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n"
            "\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);\n"
            "\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);\n"
            "\\fill (A) circle (1pt) node[left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above] {$B$};\n"
            "\\fill (C) circle (1pt) node[right] {$C$};\n"
            "\\fill (D) circle (1pt) node[below] {$D$};\n"
            "\\fill (O) circle (1pt) node[below left] {$O$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            "Cho hình thoi $ABCD$ có cạnh bằng $%s$ ($a > 0$) và $\\widehat{BAD} = 60^\\circ$. Gọi $O$ là giao điểm hai đường chéo.\n%s"
            % (latex(canh_thoi), hinh_ve)
        )

        nb_da_1_d = "\\True Tam giác $ABD$ là tam giác đều cạnh $%s$" % (latex(canh_thoi))
        nb_da_1_s = "Tam giác $ABD$ là tam giác vuông cân tại $A$"
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = (
            "Vì $ABCD$ là hình thoi nên $AB = AD = %s$. Tam giác $ABD$ cân tại $A$ có $\\widehat{BAD} = 60^\\circ$ nên là tam giác đều cạnh $%s$."
            % (latex(canh_thoi), latex(canh_thoi))
        )
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = "\\True Độ dài đường chéo $BD$ bằng $%s$" % (latex(BD_expr))
        th_da_1_s = "Độ dài đường chéo $BD$ bằng $%s$" % (latex(AC_expr))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            "Vì tam giác $ABD$ đều cạnh $%s$ nên $BD = AB = %s$."
            % (latex(canh_thoi), latex(BD_expr))
        )
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = "\\True Độ dài đường chéo $AC$ bằng $%s$" % (latex(AC_expr))
        vd_da_1_s = "Độ dài đường chéo $AC$ bằng $%s$" % (latex(Rational(1, 2) * AC_expr))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            "Trong hình thoi $ABCD$, hai đường chéo vuông góc với nhau tại trung điểm $O$ của mỗi đường và $AC$ là phân giác của $\\widehat{BAD}$ nên $\\widehat{BAO} = 30^\\circ$. \\\\ "
            "Xét tam giác $AOB$ vuông tại $O$, ta có $AO = AB \\cdot \\cos 30^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2}$. \\\\ "
            "Suy ra $AC = 2AO = %s$."
            % (latex(canh_thoi), latex(AC_expr))
        )
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = "\\True $\\tan \\widehat{BAO} \\cdot \\sin \\widehat{ABO} = \\dfrac{1}{2}$"
        vdc_da_1_s = "$\\tan \\widehat{BAO} \\cdot \\sin \\widehat{ABO} = \\dfrac{\\sqrt{3}}{2}$"
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            "Ta có $\\widehat{BAO} = 30^\\circ$ và $\\widehat{ABO} = 90^\\circ - 30^\\circ = 60^\\circ$. \\\\ "
            "Do đó $\\tan \\widehat{BAO} \\cdot \\sin \\widehat{ABO} = \\tan 30^\\circ \\cdot \\sin 60^\\circ = \\dfrac{\\sqrt{3}}{3} \\cdot \\dfrac{\\sqrt{3}}{2} = \\dfrac{1}{2}$."
        )
        list_vdc_2 = [loigiai_vdc_1]

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

    content = (
        '\\begin{minipage}{\\textwidth} \n'
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
        '\\end{ex}\n \\end{minipage}\n\n'
    )
    return content
