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


def bt_dang16_p2_b3_c2_ds8(self):
    # Dạng 16 (Thực tế): Hiệu thể tích hai khối lập phương (gia công khối gỗ)
    d = randint(2, 4)
    x_val = randint(3, 6)
    h2 = 3 * d
    h1 = 3 * (d**2)
    h0 = d**3
    V_kq = h2 * (x_val**2) + h1 * x_val + h0

    noidungcauhoi = ('''Từ một khối gỗ hình lập phương lớn có độ dài cạnh là $x + %s$ ($\\text{cm}$), người thợ mộc khoét đi một khối lập phương nhỏ có độ dài cạnh là $x$ ($\\text{cm}$) (với $x > 0$). Xét tính đúng sai của các khẳng định sau:''' % (d))

    nb_da_1_d = '\\True Thể tích phần gỗ còn lại được biểu thị bởi công thức $V = (x + %s)^3 - x^3$ ($\\text{cm}^3$)' % (d)
    nb_da_1_s = 'Thể tích phần gỗ còn lại được biểu thị bởi công thức $V = (x + %s)^3 + x^3$ ($\\text{cm}^3$)' % (d)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Thể tích khối lập phương lớn là $(x + %s)^3$, thể tích khối lập phương bị khoét đi là $x^3$, nên phần còn lại có thể tích $V = (x + %s)^3 - x^3$ ($\\text{cm}^3$).''' % (d, d))

    th_da_1_d = '\\True Áp dụng hằng đẳng thức hiệu hai lập phương, ta có $V = %s\\left[(x + %s)^2 + x(x + %s) + x^2\\right]$' % (d, d, d)
    th_da_1_s = 'Áp dụng hằng đẳng thức hiệu hai lập phương, ta có $V = %s\\left[(x + %s)^2 - x(x + %s) + x^2\\right]$' % (d, d, d)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $V = \\left[(x + %s) - x\\right]\\left[(x + %s)^2 + x(x + %s) + x^2\\right] = %s\\left[(x + %s)^2 + x(x + %s) + x^2\\right]$.''' % (d, d, d, d, d, d))

    vd_da_1_d = '\\True Rút gọn đa thức $V$ theo biến $x$, ta được $V = %sx^2 + %sx + %s$ ($\\text{cm}^3$)' % (h2, h1, h0)
    vd_da_1_s = 'Rút gọn đa thức $V$ theo biến $x$, ta được $V = %sx^2 + %sx + %s$ ($\\text{cm}^3$)' % (d, h1, h0)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $V = %s(x^2 + %sx + %s + x^2 + %sx + x^2) = %s(3x^2 + %sx + %s) = %sx^2 + %sx + %s$ ($\\text{cm}^3$).''' % (d, 2*d, d**2, d, d, 3*d, d**2, h2, h1, h0))

    vdc_da_1_d = '\\True Khi $x = %s\\text{ cm}$, thể tích phần gỗ còn lại là $%s\\text{ cm}^3$' % (x_val, V_kq)
    vdc_da_1_s = 'Khi $x = %s\\text{ cm}$, thể tích phần gỗ còn lại là $%s\\text{ cm}^3$' % (x_val, V_kq - h0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Thay $x = %s$ vào biểu thức rút gọn, ta được $V = %s \\cdot %s^2 + %s \\cdot %s + %s = %s$ ($\\text{cm}^3$).''' % (x_val, h2, x_val, h1, x_val, h0, V_kq))

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
