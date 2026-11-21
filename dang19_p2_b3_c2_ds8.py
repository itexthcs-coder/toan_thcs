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


def bt_dang19_p2_b3_c2_ds8(self):
    # Dạng 19 (Thực tế): Bài toán làm hộp không nắp từ tấm bìa hình vuông
    L = random.choice([16, 20, 24])
    nua_L = L // 2
    L2 = L**2
    bon_L = 4 * L
    x0 = randint(2, 4)
    canh_day = L - 2 * x0
    V_kq = x0 * (canh_day**2)

    noidungcauhoi = ('''Từ một tấm bìa hình vuông có cạnh bằng $%s\\text{ cm}$, người ta cắt bỏ ở bốn góc bốn hình vuông nhỏ bằng nhau có cạnh là $x$ ($\\text{cm}$, $0 < x < %s$) rồi gấp lại thành một chiếc hộp hình hộp chữ nhật không nắp. Xét tính đúng sai của các khẳng định sau:''' % (L, nua_L))

    nb_da_1_d = '\\True Chiều dài cạnh đáy của chiếc hộp là $%s - 2x$ ($\\text{cm}$)' % (L)
    nb_da_1_s = 'Chiều dài cạnh đáy của chiếc hộp là $%s - x$ ($\\text{cm}$)' % (L)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì cắt bỏ ở hai đầu mỗi cạnh một đoạn bằng $x\\text{ cm}$ nên chiều dài cạnh đáy của hộp là $%s - 2x$ ($\\text{cm}$).''' % (L))

    th_da_1_d = '\\True Thể tích của chiếc hộp được biểu thị bởi biểu thức $V = x(%s - 2x)^2$ ($\\text{cm}^3$)' % (L)
    th_da_1_s = 'Thể tích của chiếc hộp được biểu thị bởi biểu thức $V = x^2(%s - 2x)$ ($\\text{cm}^3$)' % (L)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Hộp có đáy là hình vuông cạnh $%s - 2x$ ($\\text{cm}$) và chiều cao $x$ ($\\text{cm}$) nên thể tích là $V = x(%s - 2x)^2$ ($\\text{cm}^3$).''' % (L, L))

    vd_da_1_d = '\\True Khai triển đa thức $V$ theo lũy thừa giảm dần của $x$, ta được $V = 4x^3 - %sx^2 + %sx$' % (bon_L, L2)
    vd_da_1_s = 'Khai triển đa thức $V$ theo lũy thừa giảm dần của $x$, ta được $V = 4x^3 - %sx^2 + %sx$' % (2*L, L2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $V = x(%s - %sx + 4x^2) = 4x^3 - %sx^2 + %sx$.''' % (L2, bon_L, bon_L, L2))

    vdc_da_1_d = '\\True Khi cắt góc có cạnh $x = %s\\text{ cm}$, thể tích của chiếc hộp là $%s\\text{ cm}^3$' % (x0, V_kq)
    vdc_da_1_s = 'Khi cắt góc có cạnh $x = %s\\text{ cm}$, thể tích của chiếc hộp là $%s\\text{ cm}^3$' % (x0, x0 * ((L - x0)**2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Thay $x = %s$ vào biểu thức $V$, ta được $V = %s \\cdot (%s - 2 \\cdot %s)^2 = %s \\cdot %s^2 = %s$ ($\\text{cm}^3$).''' % (x0, x0, L, x0, x0, canh_day, V_kq))

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
