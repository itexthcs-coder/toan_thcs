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

def bt_dang17_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v1 = 80
        v2 = 40
        c_s = random.choice([5, 7, 8])
        S_total = 40 * c_s
        y_sample = c_s - 3
        max_x_str = str(Decimal(str(c_s / 2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        sum_eq_time = Rational(2 * c_s, 3)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ô tô di chuyển từ tỉnh $A$ đến tỉnh $B$ dài $%s\\text{ km}$ gồm hai chặng: đi trên đường cao tốc với vận tốc trung bình $%s\\text{ km/h}$ trong $x$ giờ và đi trên đường tỉnh lộ với vận tốc trung bình $%s\\text{ km/h}$ trong $y$ giờ ($x > 0, y > 0$).'''
                         % (S_total, v1, v2))

        # Nhận biết
        nb_da_1_d = '\\True Mối liên hệ giữa thời gian $x$ và $y$ được biểu diễn bởi phương trình $2x + y = %s$' % (c_s)
        nb_da_1_s = 'Mối liên hệ giữa thời gian $x$ và $y$ được biểu diễn bởi phương trình $x + 2y = %s$' % (c_s)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Tổng quãng đường ô tô đi được là $%sx + %sy = %s$. Chia cả hai vế cho $40$ ta được phương trình $2x + y = %s$.'''
                        % (v1, v2, S_total, c_s))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Nếu ô tô đi trên đường cao tốc trong $1{,}5$ giờ thì thời gian đi trên đường tỉnh lộ là $%s$ giờ' % (y_sample)
        th_da_1_s = 'Nếu ô tô đi trên đường cao tốc trong $1{,}5$ giờ thì thời gian đi trên đường tỉnh lộ là $%s$ giờ' % (y_sample + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thay $x = 1{,}5$ vào phương trình $2x + y = %s$ ta được $2 \\cdot 1{,}5 + y = %s \\Leftrightarrow 3 + y = %s \\Leftrightarrow y = %s$ (giờ).'''
                        % (c_s, c_s, c_s, y_sample))
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Thời gian ô tô đi trên đường cao tốc luôn nhỏ hơn $%s$ giờ' % (max_x_str)
        vd_da_1_s = 'Thời gian ô tô đi trên đường cao tốc có thể bằng $%s$ giờ' % (c_s)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vì $y > 0$ nên từ $2x + y = %s$ suy ra $2x = %s - y < %s \\Leftrightarrow x < %s$ (giờ).'''
                        % (c_s, c_s, c_s, max_x_str))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Nếu thời gian đi trên hai loại đường bằng nhau thì tổng thời gian di chuyển từ $A$ đến $B$ là $%s$ giờ' % (latex(sum_eq_time))
        vdc_da_1_s = 'Nếu thời gian đi trên hai loại đường bằng nhau thì tổng thời gian di chuyển từ $A$ đến $B$ là $%s$ giờ' % (c_s)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi $x = y$, thay vào phương trình ta được $2x + x = %s \\Leftrightarrow 3x = %s \\Leftrightarrow x = y = \\dfrac{%s}{3}$ (giờ). Tổng thời gian di chuyển là $x + y = %s$ giờ.'''
                         % (c_s, c_s, c_s, latex(sum_eq_time)))
        list_vdc_2 = [loigiai_vdc_1]

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
