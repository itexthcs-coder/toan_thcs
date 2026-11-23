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


def bt_dang9_p2_b1_c4_hh8(self):
    ab = 3 * random.randint(3, 6)
    ac = 3 * random.randint(4, 7)
    while ab == ac:
        ac = 3 * random.randint(4, 7)
    ae = (2 * ab) // 3
    eb = ab - ae
    af = (2 * ac) // 3
    fc = ac - af

    noidungcauhoi = ("""Cho $\\Delta ABC$ có trọng tâm $G$, đường trung tuyến $AM$ ($M \\in BC$). Qua $G$ kẻ đường thẳng $d$ song song với $BC$, cắt cạnh $AB$ tại $E$ và cắt cạnh $AC$ tại $F$ (như hình vẽ bên dưới). Biết $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (G) at ($(A)!0.6667!(M)$);
\\coordinate (E) at ($(A)!0.6667!(B)$);
\\coordinate (F) at ($(A)!0.6667!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (E)--(F);
\\draw[line width=1pt, dashed] (A)--(M);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (G) circle (1pt) node[below right] {$G$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (F) circle (1pt) node[right] {$F$};
\\end{tikzpicture}
\\end{center}"""
                     % (ab, ac))

    nb_da_1_d = '\\True $\\dfrac{AG}{AM} = \\dfrac{2}{3}$'
    nb_da_1_s = '$\\dfrac{AG}{AM} = \\dfrac{1}{3}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì $G$ là trọng tâm của $\\Delta ABC$ và $AM$ là đường trung tuyến nên $\\dfrac{AG}{AM} = \\dfrac{2}{3}$.""")

    th_da_1_d = '\\True Độ dài đoạn thẳng $AE$ bằng $%s\\text{ cm}$' % (ae)
    th_da_1_s = 'Độ dài đoạn thẳng $AE$ bằng $%s\\text{ cm}$' % (eb)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Xét $\\Delta ABM$ có $EG // BM$, theo định lí Thalès ta có $\\dfrac{AE}{AB} = \\dfrac{AG}{AM} = \\dfrac{2}{3} \\Rightarrow AE = \\dfrac{2}{3} \\cdot %s = %s\\text{ (cm)}$."""
                    % (ab, ae))

    vd_da_1_d = '\\True Độ dài đoạn thẳng $FC$ bằng $%s\\text{ cm}$' % (fc)
    vd_da_1_s = 'Độ dài đoạn thẳng $FC$ bằng $%s\\text{ cm}$' % (af)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Xét $\\Delta AMC$ có $GF // MC$, theo định lí Thalès ta có $\\dfrac{AF}{AC} = \\dfrac{AG}{AM} = \\dfrac{2}{3} \\Rightarrow AF = \\dfrac{2}{3} \\cdot %s = %s\\text{ (cm)}$. \\\\ Do đó $FC = AC - AF = %s - %s = %s\\text{ (cm)}$."""
                    % (ac, af, ac, af, fc))

    vdc_da_1_d = '\\True Tổng $\\dfrac{AE}{EB} + \\dfrac{AF}{FC}$ bằng $4$'
    vdc_da_1_s = 'Tổng $\\dfrac{AE}{EB} + \\dfrac{AF}{FC}$ bằng $\\dfrac{4}{3}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Ta có $\\dfrac{AE}{EB} = \\dfrac{%s}{%s} = 2$ và $\\dfrac{AF}{FC} = \\dfrac{%s}{%s} = 2$, suy ra $\\dfrac{AE}{EB} + \\dfrac{AF}{FC} = 2 + 2 = 4$."""
                     % (ae, eb, af, fc))

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
