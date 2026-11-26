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
def bt_dang11_p2_b3_c6_ds8(self):
    # Dạng 11: Cộng/trừ hai phân thức có mẫu là bình phương của một hiệu và hiệu hai bình phương
    k = random.choice([1, 2, 3])
    str_k = '' if k == 1 else '%s' % k
    
    noidungcauhoi = ('Cho biểu thức $T = \\dfrac{%sx}{(x - y)^2} - \\dfrac{%sy}{x^2 - y^2}$ (với $x \\neq \\pm y$). Xét tính đúng, sai của các khẳng định sau:' % (str_k, str_k))
    
    list_nb_da_1 = [
        '\\True Ta có $x^2 - y^2 = (x - y)(x + y)$, nên mẫu thức chung đơn giản nhất là $(x - y)^2(x + y)$',
        'Mẫu thức chung đơn giản nhất của hai phân thức là $(x - y)(x + y)$'
    ]
    loigiai_nb_1 = ('Phân tích $x^2 - y^2 = (x - y)(x + y)$, kết hợp với $(x - y)^2$ ta có mẫu thức chung đơn giản nhất là $(x - y)^2(x + y)$.')
    
    list_th_da_1 = [
        '\\True Khi quy đồng, tử thức của phân thức thứ nhất là $%sx(x + y)$ và tử thức của phân thức thứ hai là $%sy(x - y)$' % (str_k, str_k),
        'Khi quy đồng, tử thức của phân thức thứ nhất là $%sx(x - y)$ và tử thức của phân thức thứ hai là $%sy(x + y)$' % (str_k, str_k)
    ]
    loigiai_th_1 = ('Nhân tử phụ của phân thức thứ nhất là $x + y$, của phân thức thứ hai là $x - y$, nên các tử thức sau khi quy đồng là $%sx(x + y)$ và $%sy(x - y)$.' % (str_k, str_k))
    
    list_vd_da_1 = [
        '\\True Tử thức của hiệu sau khi thu gọn là $%s(x^2 + y^2)$' % str_k,
        'Tử thức của hiệu sau khi thu gọn là $%s(x^2 - y^2)$' % str_k
    ]
    loigiai_vd_1 = ('Hiệu hai tử thức là $%sx(x + y) - %sy(x - y) = %s(x^2 + xy - xy + y^2) = %s(x^2 + y^2)$.' % (str_k, str_k, str_k, str_k))
    
    list_vdc_da_1 = [
        '\\True Biểu thức $T$ viết dưới dạng phân thức rút gọn là $\\dfrac{%s(x^2 + y^2)}{(x - y)^2(x + y)}$' % str_k,
        'Biểu thức $T$ viết dưới dạng phân thức rút gọn là $\\dfrac{%s}{x - y}$' % str_k
    ]
    loigiai_vdc_1 = ('Vì $x^2 + y^2$ không có nhân tử chung với $(x - y)^2(x + y)$ nên phân thức rút gọn là $T = \\dfrac{%s(x^2 + y^2)}{(x - y)^2(x + y)}$.' % str_k)
    
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
            
    combined = list(zip(answers, [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
