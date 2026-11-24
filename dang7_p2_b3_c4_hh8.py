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

def bt_dang7_p2_b3_c4_hh8(self):
    # Dạng 7: Kết hợp bất đẳng thức tam giác và đường trung bình trong tứ giác
    ab = random.choice([6, 8, 10])
    cd = random.choice([12, 14, 16])
    ek = cd // 2
    fk = ab // 2
    hieu_ef = ek - fk
    tong_ef = ek + fk

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0.6,2.8);\n'
        '\\coordinate (B) at (3.4,3.1);\n'
        '\\coordinate (C) at (4.8,0);\n'
        '\\coordinate (D) at (0,0);\n'
        '\\coordinate (E) at ($(A)!0.5!(D)$);\n'
        '\\coordinate (F) at ($(B)!0.5!(C)$);\n'
        '\\coordinate (K) at ($(A)!0.5!(C)$);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (E)--(K)--(F)--cycle;\n'
        '\\fill (A) circle (1pt) node[above left] {$A$};\n'
        '\\fill (B) circle (1pt) node[above right] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (D) circle (1pt) node[below left] {$D$};\n'
        '\\fill (E) circle (1pt) node[left] {$E$};\n'
        '\\fill (F) circle (1pt) node[right] {$F$};\n'
        '\\fill (K) circle (1pt) node[below] {$K$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho tứ giác $ABCD$ có hai cạnh đối $AB$ và $CD$ không song song, biết $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$. Gọi $E, F, K$ lần lượt là trung điểm của $AD, BC, AC$.\n%s'
        % (ab, cd, hinh_ve)
    )

    nb_da_1_d = '\\True $EK // CD$ và $EK = %s\\text{ cm}$' % ek
    nb_da_1_s = '$EK // CD$ và $EK = %s\\text{ cm}$' % cd
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Vì $E, K$ lần lượt là trung điểm của $AD, AC$ nên $EK$ là đường trung bình của tam giác $ADC$, suy ra $EK // CD$ và $EK = \\frac{1}{2}CD = %s\\text{ cm}$.' % ek
    loigiai_nb_s = 'Sai. $EK$ là đường trung bình của tam giác $ADC$ nên $EK = \\frac{1}{2}CD = %s\\text{ cm}$.' % ek

    th_da_1_d = '\\True $FK // AB$ và $FK = %s\\text{ cm}$' % fk
    th_da_1_s = '$FK // AB$ và $FK = %s\\text{ cm}$' % ab
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Vì $F, K$ lần lượt là trung điểm của $BC, AC$ nên $FK$ là đường trung bình của tam giác $ABC$, suy ra $FK // AB$ và $FK = \\frac{1}{2}AB = %s\\text{ cm}$.' % fk
    loigiai_th_s = 'Sai. $FK$ là đường trung bình của tam giác $ABC$ nên $FK = \\frac{1}{2}AB = %s\\text{ cm}$.' % fk

    vd_da_1_d = '\\True Ba điểm $E, K, F$ không thẳng hàng'
    vd_da_1_s = 'Ba điểm $E, K, F$ luôn thẳng hàng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Nếu $E, K, F$ thẳng hàng thì qua $K$ có hai đường thẳng $EK, FK$ trùng nhau cùng song song với $CD$ và $AB$, suy ra $AB // CD$ (mâu thuẫn giả thiết). Vậy ba điểm $E, K, F$ không thẳng hàng.'
    loigiai_vd_s = 'Sai. Vì hai cạnh $AB$ và $CD$ không song song nên hai đường thẳng $EK$ và $FK$ không trùng nhau, do đó $E, K, F$ không thẳng hàng.'

    vdc_da_1_d = '\\True Độ dài đoạn thẳng $EF$ luôn thỏa mãn $%s\\text{ cm} < EF < %s\\text{ cm}$' % (hieu_ef, tong_ef)
    vdc_da_1_s = 'Độ dài đoạn thẳng $EF$ luôn bằng $%s\\text{ cm}$' % tong_ef
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Áp dụng bất đẳng thức tam giác cho tam giác $EFK$, ta có $EK - FK < EF < EK + FK$, tức là $%s - %s < EF < %s + %s$ hay $%s\\text{ cm} < EF < %s\\text{ cm}$.' % (ek, fk, ek, fk, hieu_ef, tong_ef)
    loigiai_vdc_s = 'Sai. Trong tam giác $EFK$, theo bất đẳng thức tam giác ta có $%s\\text{ cm} < EF < %s\\text{ cm}$.' % (hieu_ef, tong_ef)

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
