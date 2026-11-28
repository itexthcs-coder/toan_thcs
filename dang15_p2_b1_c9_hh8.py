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
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        s = ('%.4f' % val).rstrip('0').rstrip('.')
        return s.replace('.', ',')
    if isinstance(val, Decimal):
        s = str(val).rstrip('0').rstrip('.') if '.' in str(val) else str(val)
        return s.replace('.', ',')
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        return '\dfrac{%s}{%s}' % (val.numerator, val.denominator)
    return str(val)

def bt_dang15_p2_b1_c9_hh8(self):
    # Dạng 15: AE = 1/n EC, M là trung điểm BC, AM cắt BE tại I, MK // BE
    n = random.choice([2, 3, 4])
    ratio_ae_ak = Fraction(2, n + 2)
    ratio_ai_im = Fraction(2, n)

    AC = (n + 1) * 2 * random.choice([2, 3])
    AE = AC // (n + 1)
    EC = AC - AE
    EK = EC // 2
    AK = AE + EK

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (A) at (1.8,3.4);'
        '\\coordinate (B) at (0,0);'
        '\\coordinate (C) at (4.8,0);'
        '\\coordinate (M) at ($(B)!0.5!(C)$);'
        '\\coordinate (E) at ($(A)!0.3333!(C)$);'
        '\\coordinate (K) at ($(E)!0.5!(C)$);'
        '\\coordinate (I) at (intersection of A--M and B--E);'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(M) (B)--(E);'
        '\\draw[line width=1pt, dashed] (M)--(K);'
        '\\fill (A) circle (1pt) node[above] {$A$};'
        '\\fill (B) circle (1pt) node[left] {$B$};'
        '\\fill (C) circle (1pt) node[right] {$C$};'
        '\\fill (M) circle (1pt) node[below] {$M$};'
        '\\fill (E) circle (1pt) node[right] {$E$};'
        '\\fill (K) circle (1pt) node[right] {$K$};'
        '\\fill (I) circle (1pt) node[above left] {$I$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho $\\Delta ABC$, trên cạnh $AC$ lấy điểm $E$ sao cho $AE = %s EC$. '
        'Gọi $M$ là trung điểm của cạnh $BC$, đoạn thẳng $AM$ cắt $BE$ tại $I$. Qua $M$ kẻ đường thẳng song song với $BE$ cắt $AC$ tại $K$.%s'
        % (fmt_num(Fraction(1, n)), tikz)
    )

    nb_da_1_d = '\\True $\\Delta CMK \\backsim \\Delta CBE$ theo tỉ số đồng dạng $k = \\dfrac{1}{2}$'
    nb_da_1_s = '$\\Delta CMK \\backsim \\Delta CBE$ theo tỉ số đồng dạng $k = %s$' % fmt_num(Fraction(1, n))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Xét $\\Delta CBE$ có $MK // BE$ ($M \\in BC, K \\in EC$) nên $\\Delta CMK \\backsim \\Delta CBE$.\\ '
        'Vì $M$ là trung điểm của $BC$ nên tỉ số đồng dạng là $k = \\dfrac{CM}{CB} = \\dfrac{1}{2}$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True $\\Delta AEI \\backsim \\Delta AKM$ theo tỉ số đồng dạng $k = %s$' % fmt_num(ratio_ae_ak)
    th_da_1_s = '$\\Delta AEI \\backsim \\Delta AKM$ theo tỉ số đồng dạng $k = \\dfrac{1}{2}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Từ $\\Delta CMK \\backsim \\Delta CBE$ tỉ số $\\dfrac{1}{2}$, suy ra $K$ là trung điểm của $EC$, nên $EK = \\dfrac{1}{2} EC = %s AE$.\\ '
        'Do đó $AK = AE + EK = %s AE \\Rightarrow \\dfrac{AE}{AK} = %s$.\\ '
        'Xét $\\Delta AKM$ có $EI // KM$ nên $\\Delta AEI \\backsim \\Delta AKM$ theo tỉ số đồng dạng $k = \\dfrac{AE}{AK} = %s$.'
        % (fmt_num(Fraction(n, 2)), fmt_num(Fraction(n + 2, 2)), fmt_num(ratio_ae_ak), fmt_num(ratio_ae_ak))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tỉ số $\\dfrac{AI}{IM}$ bằng $%s$' % fmt_num(ratio_ai_im)
    vd_da_1_s = 'Tỉ số $\\dfrac{AI}{IM}$ bằng $%s$' % fmt_num(Fraction(1, n))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì $\\Delta AEI \\backsim \\Delta AKM$ nên $\\dfrac{AI}{AM} = \\dfrac{AE}{AK} = %s$.\\ '
        'Suy ra $\\dfrac{AI}{IM} = \\dfrac{2}{%s} = %s$.'
        % (fmt_num(ratio_ae_ak), n, fmt_num(ratio_ai_im))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu $AC = %s\\text{ cm}$ thì $AK = %s\\text{ cm}$' % (AC, AK)
    vdc_da_1_s = 'Nếu $AC = %s\\text{ cm}$ thì $AK = %s\\text{ cm}$' % (AC, EK)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Vì $AE = %s EC$ và $AE + EC = %s\\text{ cm}$ nên $AE = %s\\text{ cm}$, $EC = %s\\text{ cm}$.\\ '
        'Vì $K$ là trung điểm của $EC$ nên $EK = \\dfrac{%s}{2} = %s\\text{ cm}$. Vậy $AK = AE + EK = %s + %s = %s\\text{ cm}$.'
        % (fmt_num(Fraction(1, n)), AC, AE, EC, EC, EK, AE, EK, AK)
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
