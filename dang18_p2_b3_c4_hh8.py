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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang18_p2_b3_c4_hh8(self):
    # Dạng 18: Thiết kế thanh giằng mái nhà hình tam giác (Thực tế)
    bo_so = [
        (6, 9, 10, 4, 3.6, 5.4, 7.6),
        (8, 12, 15, 6, 4.8, 7.2, 10.8),
        (4, 6, 5, 2, 2.4, 3.6, 4.4)
    ]
    ab, ac, bc, bd, ae, ec, tong = random.choice(bo_so)
    s_ae = fmt_num(ae)
    s_ec = fmt_num(ec)
    s_tong = fmt_num(tong)

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (2.0,2.5);\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (5.2,0);\n'
        '\\coordinate (D) at (2.08,0);\n'
        '\\coordinate (E) at ($(A)!0.4!(C)$);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (D)--(E);\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (D) circle (1pt) node[below] {$D$};\n'
        '\\fill (E) circle (1pt) node[above right] {$E$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một khung vì kèo mái nhà có dạng tam giác $ABC$ với hai mái nghiêng $AB = %s\\text{ m}$, $AC = %s\\text{ m}$ và xà ngang $BC = %s\\text{ m}$. Kỹ sư lắp một thanh chống từ đỉnh $A$ xuống điểm $D$ trên xà ngang $BC$ sao cho $AD$ là tia phân giác của góc $BAC$, đồng thời lắp thanh ngang $DE // AB$ ($E \\in AC$).\n%s'
        % (ab, ac, bc, hinh_ve)
    )

    nb_da_1_d = '\\True Vị trí điểm $D$ cách đầu mút $B$ một khoảng bằng $%s\\text{ m}$' % bd
    nb_da_1_s = 'Vị trí điểm $D$ cách đầu mút $B$ một khoảng bằng $%s\\text{ m}$' % (bc - bd)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Vì $AD$ là tia phân giác góc $BAC$ nên $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{%s}{%s}$, kết hợp $BD + CD = %s\\text{ m}$ suy ra $BD = %s\\text{ m}$.' % (ab, ac, bc, bd)
    loigiai_nb_s = 'Sai. Ta tính được $BD = %s\\text{ m}$ và $CD = %s\\text{ m}$.' % (bd, bc - bd)

    th_da_1_d = '\\True Vị trí điểm $E$ chia mái $AC$ thành hai đoạn $AE = %s\\text{ m}$ và $EC = %s\\text{ m}$' % (s_ae, s_ec)
    th_da_1_s = 'Vị trí điểm $E$ chia mái $AC$ thành hai đoạn bằng nhau'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Vì $DE // AB$ nên theo định lí Thalès, $\\frac{AE}{EC} = \\frac{BD}{CD} = \\frac{%s}{%s}$, kết hợp $AE + EC = %s\\text{ m}$ suy ra $AE = %s\\text{ m}$ và $EC = %s\\text{ m}$.' % (ab, ac, ac, s_ae, s_ec)
    loigiai_th_s = 'Sai. Vì $AB \\neq AC$ nên $D$ không là trung điểm $BC$, suy ra $E$ không chia $AC$ thành hai đoạn bằng nhau ($AE = %s\\text{ m}, EC = %s\\text{ m}$).' % (s_ae, s_ec)

    vd_da_1_d = '\\True Chiều dài thanh ngang $DE$ bằng $%s\\text{ m}$' % s_ae
    vd_da_1_s = 'Chiều dài thanh ngang $DE$ bằng $%s\\text{ m}$' % bd
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Vì $DE // AB$ nên $\\widehat{ADE} = \\widehat{BAD} = \\widehat{EAD}$, suy ra tam giác $ADE$ cân tại $E$. Do đó $DE = AE = %s\\text{ m}$.' % s_ae
    loigiai_vd_s = 'Sai. Tam giác $ADE$ cân tại $E$ nên $DE = AE = %s\\text{ m}$.' % s_ae

    vdc_da_1_d = '\\True Tổng chiều dài hai đoạn $BD$ và $DE$ bằng $%s\\text{ m}$' % s_tong
    vdc_da_1_s = 'Tổng chiều dài hai đoạn $BD$ và $DE$ bằng $%s\\text{ m}$' % fmt_num(tong + 2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Tổng chiều dài hai đoạn là $BD + DE = %s + %s = %s\\text{ m}$.' % (bd, s_ae, s_tong)
    loigiai_vdc_s = 'Sai. Tổng chiều dài là $BD + DE = %s + %s = %s\\text{ m}$.' % (bd, s_ae, s_tong)

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

    loigiai_nb_1 = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    loigiai_th_1 = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    loigiai_vd_1 = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    loigiai_vdc_1 = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    list_nb_1 = [nb_da_1]
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    list_vd_1 = [vd_da_1]
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    list_vdc_1 = [vdc_da_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
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
