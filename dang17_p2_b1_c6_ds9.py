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


def bt_dang17_p2_b1_c6_ds9(self):
    def fmt_dec(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    a_dec = random.choice([Decimal('0.06'), Decimal('0.08'), Decimal('0.1')])
    a_str = fmt_dec(a_dec)

    v1 = 15
    d1 = a_dec * Decimal(str(v1 ** 2))
    d1_str = fmt_dec(d1)

    v2 = 20
    d2 = a_dec * Decimal(str(v2 ** 2))
    d2_str = fmt_dec(d2)
    obs_dist = int(d2) - 2

    v_safe = 10
    d_safe = a_dec * Decimal(str(v_safe ** 2))
    d_safe_str = fmt_dec(d_safe)

    noidungcauhoi = (
        'Trên một đoạn đường nhựa khô ráo, quãng đường phanh $d$ (mét) của một chiếc xe máy kể từ lúc người lái bắt đầu đạp phanh cho đến khi xe dừng hẳn phụ thuộc vào vận tốc $v$ ($\\text{m/s}$) của xe theo công thức $d = %sv^2$.' % (a_str)
    )

    nb_da_1_d = '\\True Công thức $d = %sv^2$ là một hàm số dạng $y = ax^2$ với $a = %s$' % (a_str, a_str)
    nb_da_1_s = 'Công thức $d = %sv^2$ là một hàm số bậc nhất theo biến số $v$' % (a_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Công thức $d = %sv^2$ có dạng $y = ax^2$ với biến số là $v$ và hệ số $a = %s \\ne 0$.' % (a_str, a_str)
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Nếu xe đang đi với vận tốc $15\\text{ m/s}$ thì quãng đường phanh cần thiết để dừng lại là $%s\\text{ m}$' % (d1_str)
    th_da_1_s = 'Nếu xe đang đi với vận tốc $15\\text{ m/s}$ thì quãng đường phanh cần thiết để dừng lại là $%s\\text{ m}$' % (fmt_dec(a_dec * Decimal('15')))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay $v = 15$ vào công thức ta được: $d = %s \\cdot 15^2 = %s \\cdot 225 = %s\\text{ (m)}$.' % (a_str, a_str, d1_str)
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Để quãng đường phanh không vượt quá $%s\\text{ m}$, người lái xe chỉ được phép di chuyển với vận tốc tối đa là $10\\text{ m/s}$' % (d_safe_str)
    vd_da_1_s = 'Để quãng đường phanh không vượt quá $%s\\text{ m}$, người lái xe có thể di chuyển với vận tốc tối đa là $12\\text{ m/s}$' % (d_safe_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Ta có $%sv^2 \\le %s \\Leftrightarrow v^2 \\le 100$. Vì $v > 0$ nên $v \\le 10\\text{ (m/s)}$. \\\\ Vậy vận tốc tối đa cho phép là $10\\text{ m/s}$.' % (a_str, d_safe_str)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu thấy chướng ngại vật phía trước cách $%s\\text{ m}$ và lập tức phanh xe khi đang đi ở vận tốc $20\\text{ m/s}$, xe sẽ không dừng kịp trước khi va chạm' % (str(obs_dist))
    vdc_da_1_s = 'Nếu thấy chướng ngại vật phía trước cách $%s\\text{ m}$ và lập tức phanh xe khi đang đi ở vận tốc $20\\text{ m/s}$, xe sẽ dừng lại an toàn trước khi va chạm' % (str(obs_dist))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Tại vận tốc $v = 20\\text{ m/s}$, quãng đường phanh cần thiết là: $d = %s \\cdot 20^2 = %s \\cdot 400 = %s\\text{ (m)}$. \\\\ Vì $%s\\text{ m} > %s\\text{ m}$ nên xe không thể dừng lại kịp trước chướng ngại vật.' % (a_str, a_str, d2_str, d2_str, str(obs_dist))
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
