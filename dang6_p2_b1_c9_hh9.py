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


def bt_dang6_p2_b1_c9_hh9(self):
    IA = random.choice([3, 4, 5, 6])
    IB = random.choice([6, 8, 9, 10])
    while (IA * IB) % 3 != 0 and (IA * IB) % 4 != 0:
        IB += 1
    IC = 3 if (IA * IB) % 3 == 0 else 4
    ID = (IA * IB) // IC

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (A) at (135:2);\n'
        '\\coordinate (B) at (315:2);\n'
        '\\coordinate (C) at (45:2);\n'
        '\\coordinate (D) at (220:2);\n'
        '\\coordinate (I) at (intersection of A--B and C--D);\n'
        '\\draw[line width=1pt] (O) circle (2cm);\n'
        '\\draw[line width=1pt] (A)--(B) (C)--(D) (A)--(C) (B)--(D);\n'
        '\\fill (O) circle (1pt) node[below] {$O$};\n'
        '\\fill (A) circle (1pt) node[above left] {$A$};\n'
        '\\fill (B) circle (1pt) node[below right] {$B$};\n'
        '\\fill (C) circle (1pt) node[above right] {$C$};\n'
        '\\fill (D) circle (1pt) node[below left] {$D$};\n'
        '\\fill (I) circle (1pt) node[above] {$I$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho đường tròn $(O)$ và hai dây cung $AB, CD$ cắt nhau tại điểm $I$ nằm bên trong đường tròn như hình vẽ. Biết $IA = %s\\text{ cm}$, $IB = %s\\text{ cm}$, $IC = %s\\text{ cm}$.\n%s'
        % (IA, IB, IC, hinh_ve)
    )

    nb_da_1_d = '\\True Hai góc nội tiếp $\\widehat{ACD}$ và $\\widehat{ABD}$ cùng chắn cung $AD$ nên $\\widehat{ACD} = \\widehat{ABD}$'
    nb_da_1_s = 'Hai góc nội tiếp $\\widehat{ACD}$ và $\\widehat{ABD}$ cùng chắn cung $BC$ nên $\\widehat{ACD} = \\widehat{ABD}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Trong đường tròn $(O)$, hai góc nội tiếp $\\widehat{ACD}$ và $\\widehat{ABD}$ cùng chắn cung nhỏ $AD$ nên $\\widehat{ACD} = \\widehat{ABD}$.'
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tam giác $IAC$ đồng dạng với tam giác $IDB$'
    th_da_1_s = 'Tam giác $IAC$ đồng dạng với tam giác $IBD$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Xét $\\triangle IAC$ và $\\triangle IDB$ có $\\widehat{AIC} = \\widehat{DIB}$ (hai góc đối đỉnh) và $\\widehat{ACI} = \\widehat{DBI}$ (hai góc nội tiếp cùng chắn cung $AD$). Do đó $\\triangle IAC \\backsim \\triangle IDB$ (g.g).'
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đẳng thức $IA \\cdot IB = IC \\cdot ID$ luôn đúng'
    vd_da_1_s = 'Đẳng thức $IA \\cdot IC = IB \\cdot ID$ luôn đúng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Từ $\\triangle IAC \\backsim \\triangle IDB$, ta suy ra tỉ số đồng dạng $\\dfrac{IA}{ID} = \\dfrac{IC}{IB} \\Rightarrow IA \\cdot IB = IC \\cdot ID$.'
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Độ dài đoạn thẳng $ID$ bằng $%s\\text{ cm}$' % (ID)
    vdc_da_1_s = 'Độ dài đoạn thẳng $ID$ bằng $%s\\text{ cm}$' % (ID + 2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Thay $IA = %s\\text{ cm}$, $IB = %s\\text{ cm}$, $IC = %s\\text{ cm}$ vào hệ thức $IA \\cdot IB = IC \\cdot ID$, ta được $ID = \\dfrac{IA \\cdot IB}{IC} = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ cm}$.' % (IA, IB, IC, IA, IB, IC, ID)
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
