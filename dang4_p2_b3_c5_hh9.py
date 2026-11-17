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
from PyQt5.QtGui import QTextCursor, QFont
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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D








def bt_dang4_p2_b3_c5_hh9(self):
    R_val = random.choice([5, 10])
    r_val = 3 if R_val == 5 else 6
    C_lon = 2 * R_val * pi
    S_nho = (r_val**2) * pi
    Sv_val = (R_val**2 - r_val**2) * pi
    ti_so = Rational(R_val**2 - r_val**2, R_val**2)
    goc_q = Rational(360 * (R_val**2 - r_val**2), R_val**2)

    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8]
        \\fill[blue!15] (0,0) circle (1.9cm);
        \\fill[white] (0,0) circle (1.1cm);
        \\draw[thick] (0,0) circle (1.9cm);
        \\draw[thick] (0,0) circle (1.1cm);
        \\fill (0,0) circle (1.5pt) node[below] {$O$};
        \\draw[->] (0,0) -- (30:1.9cm) node[midway, above] {$R$};
        \\draw[->] (0,0) -- (150:1.1cm) node[midway, above] {$r$};
    \\end{tikzpicture}
    \\end{center}''')

    noidungcauhoi = ('''Cho hai đường tròn đồng tâm $(O; R)$ và $(O; r)$ với $R > r$ (như hình vẽ). Biết chu vi đường tròn lớn bằng $%s\\text{ cm}$ và diện tích đường tròn nhỏ bằng $%s\\text{ cm}^2$. Xét tính đúng sai của các khẳng định sau:
    %s''' % (latex(C_lon), latex(S_nho), hinh_ve))

    nb_da_1_d = '\\True Bán kính đường tròn lớn là $R = %d\\text{ cm}$ và bán kính đường tròn nhỏ là $r = %d\\text{ cm}$' % (R_val, r_val)
    nb_da_1_s = 'Bán kính đường tròn lớn là $R = %d\\text{ cm}$ và bán kính đường tròn nhỏ là $r = %d\\text{ cm}$' % (2*R_val, r_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''Ta có $C = 2\\pi R = %s \\implies R = %d\\text{ (cm)}$ và $S_{\\text{nhỏ}} = \\pi r^2 = %s \\implies r = %d\\text{ (cm)}$.''' % (latex(C_lon), R_val, latex(S_nho), r_val))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích hình vành khuyên tạo bởi hai đường tròn đồng tâm trên bằng $%s\\text{ cm}^2$' % latex(Sv_val)
    th_da_1_s = 'Diện tích hình vành khuyên tạo bởi hai đường tròn đồng tâm trên bằng $%s\\text{ cm}^2$' % latex(((R_val - r_val)**2)*pi)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Diện tích hình vành khuyên là $S_v = \\pi(R^2 - r^2) = \\pi(%d^2 - %d^2) = %s\\text{ (cm}^2\\text{)}$.''' % (R_val, r_val, latex(Sv_val)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tỉ số giữa diện tích hình vành khuyên và diện tích hình tròn lớn bằng $%s$' % latex(ti_so)
    vd_da_1_s = 'Tỉ số giữa diện tích hình vành khuyên và diện tích hình tròn lớn bằng $%s$' % latex(Rational(R_val - r_val, R_val))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Tỉ số cần tìm là $\\dfrac{S_v}{S_{\\text{lớn}}} = \\dfrac{%s}{%s} = %s$.''' % (latex(Sv_val), latex((R_val**2)*pi), latex(ti_so)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Một hình quạt tròn của đường tròn $(O; R)$ có diện tích bằng diện tích hình vành khuyên trên thì ứng với cung có số đo $%s^\\circ$' % latex(goc_q)
    vdc_da_1_s = 'Một hình quạt tròn của đường tròn $(O; R)$ có diện tích bằng diện tích hình vành khuyên trên thì ứng với cung có số đo $180^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Ta có $\\dfrac{n}{360}\\pi R^2 = %s \\implies n = 360 \\cdot %s = %s$. Vậy cung đó có số đo $%s^\\circ$.''' % (latex(Sv_val), latex(ti_so), latex(goc_q), latex(goc_q)))
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
