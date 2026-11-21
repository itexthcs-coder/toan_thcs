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


def bt_dang18_p2_b3_c2_ds8(self):
    # Dạng 18 (Thực tế): Bài toán lãi kép ngân hàng trong kỳ hạn 3 năm
    P = random.choice([100, 200, 300])
    r_pct = random.choice([5, 6])
    r_str = '0,0' + str(r_pct)
    S_dec = Decimal(str(P)) * (Decimal('1') + Decimal('0.0' + str(r_pct)))**3
    S_str = str(S_dec.normalize()).replace('.', ',')
    S_don_str = str(P + 3 * P * r_pct // 100)

    noidungcauhoi = ('''Cô Lan gửi tiết kiệm $%s$ triệu đồng vào ngân hàng theo thể thức lãi kép định kì với lãi suất không đổi $x$ mỗi năm. Số tiền cô Lan nhận được sau $3$ năm được tính theo công thức $S = %s(1 + x)^3$ (triệu đồng). Xét tính đúng sai của các khẳng định sau:''' % (P, P))

    nb_da_1_d = '\\True Khai triển $S$ thành đa thức theo biến $x$, ta được $S = %s + %sx + %sx^2 + %sx^3$' % (P, 3*P, 3*P, P)
    nb_da_1_s = 'Khai triển $S$ thành đa thức theo biến $x$, ta được $S = %s + %sx + %sx^2 + %sx^3$' % (P, P, P, P)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta có $S = %s(1 + 3x + 3x^2 + x^3) = %s + %sx + %sx^2 + %sx^3$.''' % (P, P, 3*P, 3*P, P))

    th_da_1_d = '\\True Đa thức biểu thị số tiền lãi cô Lan nhận được sau $3$ năm là $L = %sx^3 + %sx^2 + %sx$ (triệu đồng)' % (P, 3*P, 3*P)
    th_da_1_s = 'Đa thức biểu thị số tiền lãi cô Lan nhận được sau $3$ năm là $L = %sx^3 + %sx^2 + %sx + %s$ (triệu đồng)' % (P, 3*P, 3*P, P)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số tiền lãi bằng tổng số tiền nhận được trừ đi tiền vốn ban đầu: $L = S - %s = %sx^3 + %sx^2 + %sx$ (triệu đồng).''' % (P, P, 3*P, 3*P))

    vd_da_1_d = '\\True Nếu lãi suất là $x = %s\\%%$/năm ($x = %s$), số tiền cô Lan nhận được sau $3$ năm là $%s$ triệu đồng' % (r_pct, r_str, S_str)
    vd_da_1_s = 'Nếu lãi suất là $x = %s\\%%$/năm ($x = %s$), số tiền cô Lan nhận được sau $3$ năm là $%s$ triệu đồng' % (r_pct, r_str, S_don_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Với $x = %s\\%% = %s$, ta có $S = %s \\cdot (1 + %s)^3 = %s \\cdot 1,0%s^3 = %s$ (triệu đồng).''' % (r_pct, r_str, P, r_str, P, r_pct, S_str))

    vdc_da_1_d = '\\True Đa thức $S$ là một đa thức bậc $3$ theo biến $x$ có hệ số cao nhất là $%s$' % (P)
    vdc_da_1_s = 'Đa thức $S$ là một đa thức bậc $3$ theo biến $x$ có hệ số cao nhất là $%s$' % (3*P)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Đa thức $S = %sx^3 + %sx^2 + %sx + %s$ có bậc là $3$ và hệ số của $x^3$ là $%s$.''' % (P, 3*P, 3*P, P, P))

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
