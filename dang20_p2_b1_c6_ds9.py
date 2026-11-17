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


def bt_dang20_p2_b1_c6_ds9(self):
    def fmt_dec(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    a_abs = random.choice([Decimal('0.3'), Decimal('0.4'), Decimal('0.5')])
    a_str = fmt_dec(-a_abs)
    a_abs_str = fmt_dec(a_abs)

    w_gate = 8
    h_gate = a_abs * Decimal('16')
    h_gate_str = fmt_dec(h_gate)

    y_led = a_abs * Decimal('4')
    h_led = h_gate - y_led
    h_led_str = fmt_dec(h_led)
    y_led_str = fmt_dec(y_led)

    y_truck = a_abs * Decimal('2.25')
    h_clear = h_gate - y_truck
    h_truck = h_clear - Decimal('0.5')
    y_truck_str = fmt_dec(y_truck)
    h_clear_str = fmt_dec(h_clear)
    h_truck_str = fmt_dec(h_truck)

    tikz_code = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[->, line width=1pt] (-4.5,0) -- (4.5,0) node[below] {$x$};\n'
        '\\draw[->, line width=1pt] (0,-4) -- (0,0.8) node[right] {$y$};\n'
        '\\draw[line width=1pt, smooth, samples=100, domain=-3.5:3.5] plot (\\x, {-0.28*(\\x)^2});\n'
        '\\draw[line width=1pt, dashed] (-3.5,-3.43) -- (3.5,-3.43);\n'
        '\\draw[line width=1pt] (-1.8,-0.91) -- (1.8,-0.91);\n'
        '\\fill (0,0) circle (1pt) node[above right] {$O$};\n'
        '\\fill (-3.5,-3.43) circle (1pt) node[below left] {$A$};\n'
        '\\fill (3.5,-3.43) circle (1pt) node[below right] {$B$};\n'
        '\\fill (0,-3.43) circle (1pt) node[below] {$I$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một cổng chào sự kiện được dựng bằng khung thép có hình dạng là một parabol $y = ax^2$ ($a < 0$) đặt trên mặt đất bằng phẳng. Chọn hệ trục toạ độ $Oxy$ sao cho đỉnh cổng là gốc toạ độ $O(0;0)$, trục $Oy$ hướng thẳng đứng lên trên. Biết khoảng cách giữa hai chân cổng trên mặt đất là $AB = %s\\text{ m}$ và chiều cao của cổng là $OI = %s\\text{ m}$.%s' % (str(w_gate), h_gate_str, tikz_code)
    )

    nb_da_1_d = '\\True Hai chân cổng $A$ và $B$ nằm trên mặt đất có toạ độ là $(-4; -%s)$ và $(4; -%s)$' % (h_gate_str, h_gate_str)
    nb_da_1_s = 'Hai chân cổng $A$ và $B$ nằm trên mặt đất có toạ độ là $(-8; -%s)$ và $(8; -%s)$' % (h_gate_str, h_gate_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Vì khoảng cách hai chân cổng là $AB = 8\\text{ m}$ và $Oy$ là trục đối xứng nên mỗi chân cổng cách $Oy$ một đoạn $4\\text{ m}$. Chiều cao cổng là $%s\\text{ m}$ nên hai chân cổng có toạ độ là $A(-4; -%s)$ và $B(4; -%s)$.' % (h_gate_str, h_gate_str, h_gate_str)
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Phương trình parabol của khung cổng là $y = %sx^2$' % (a_str)
    th_da_1_s = 'Phương trình parabol của khung cổng là $y = %sx^2$' % (a_abs_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay toạ độ điểm $B(4; -%s)$ vào phương trình $y = ax^2$ ta được: \\\\ $a \\cdot 4^2 = -%s \\Leftrightarrow 16a = -%s \\Leftrightarrow a = %s$. Vậy phương trình parabol là $y = %sx^2$.' % (h_gate_str, h_gate_str, h_gate_str, a_str, a_str)
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Người ta treo một dải đèn LED nằm ngang nối hai bên sườn cổng ở độ cao $%s\\text{ m}$ so với mặt đất. Chiều dài của dải đèn LED này là $4\\text{ m}$' % (h_led_str)
    vd_da_1_s = 'Người ta treo một dải đèn LED nằm ngang nối hai bên sườn cổng ở độ cao $%s\\text{ m}$ so với mặt đất. Chiều dài của dải đèn LED này là $2\\text{ m}$' % (h_led_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vị trí treo đèn LED ở độ cao $%s\\text{ m}$ so với mặt đất nên cách đỉnh $O$ một khoảng $%s - %s = %s\\text{ m}$, tức là có tung độ $y = -%s$. \\\\ Thay $y = -%s$ vào phương trình $y = %sx^2$ ta được: $%sx^2 = -%s \\Leftrightarrow x^2 = 4 \\Leftrightarrow x = 2$ hoặc $x = -2$. \\\\ Chiều dài dải đèn LED là $2 - (-2) = 4\\text{ (m)}$.' % (h_led_str, h_gate_str, h_led_str, y_led_str, y_led_str, y_led_str, a_str, a_str, y_led_str)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Một chiếc xe chuyên dụng có chiều rộng $3\\text{ m}$ và chiều cao $%s\\text{ m}$ đi chính giữa cổng thì có thể qua lọt mà không chạm khung cổng' % (h_truck_str)
    vdc_da_1_s = 'Một chiếc xe chuyên dụng có chiều rộng $3\\text{ m}$ và chiều cao $%s\\text{ m}$ đi chính giữa cổng thì sẽ bị vướng vào khung cổng' % (h_truck_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Khi xe rộng $3\\text{ m}$ đi chính giữa cổng, hai mép bên của xe ứng với hoành độ $x = 1,5$ và $x = -1,5$. \\\\ Thay $x = 1,5$ vào phương trình parabol ta được $y = %s \\cdot (1,5)^2 = -%s$. \\\\ Chiều cao thông thuỷ của cổng tại vị trí mép xe là $%s - %s = %s\\text{ (m)}$. Vì $%s\\text{ m} > %s\\text{ m}$ nên xe có thể đi qua lọt.' % (a_str, y_truck_str, h_gate_str, y_truck_str, h_clear_str, h_clear_str, h_truck_str)
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
