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


def bt_dang7_p2_b1_c6_ds8(self):
    # Dạng 7: Tìm đa thức chưa biết trong đẳng thức hai phân thức bằng nhau (dạng tìm tử thức)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4])
        k = random.choice([2, 3, 5])
        a2 = a * a
        ka = k * a
        
        noidungcauhoi = ('Cho đẳng thức $\\dfrac{A}{%sx + 1} = \\dfrac{%sx^2 - %sx}{%sx^2 - 1}$ (với $x \\neq \\pm \\dfrac{1}{%s}$), trong đó $A$ là một đa thức. Xét tính đúng sai của các khẳng định sau:'
                         % (a, ka, k, a2, a))
        
        nb_da_1_d = '\\True Theo định nghĩa hai phân thức bằng nhau, ta có $A \\cdot (%sx^2 - 1) = (%sx + 1)(%sx^2 - %sx)$' % (a2, a, ka, k)
        nb_da_1_s = 'Theo định nghĩa hai phân thức bằng nhau, ta có $A \\cdot (%sx^2 - %sx) = (%sx + 1)(%sx^2 - 1)$' % (ka, k, a, a2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Áp dụng quy tắc $\\dfrac{M}{N} = \\dfrac{P}{Q} \\Rightarrow M \\cdot Q = N \\cdot P$.'
        loigiai_nb_s = 'Sai. Tích chéo đúng phải là $A \\cdot (%sx^2 - 1) = (%sx + 1)(%sx^2 - %sx)$.' % (a2, a, ka, k)
        
        th_da_1_d = '\\True Phân tích đa thức thành nhân tử ta được $%sx^2 - 1 = (%sx - 1)(%sx + 1)$ và $%sx^2 - %sx = %sx(%sx - 1)$' % (a2, a, a, ka, k, k, a)
        th_da_1_s = 'Phân tích đa thức thành nhân tử ta được $%sx^2 - 1 = (%sx - 1)^2$' % (a2, a)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Sử dụng hằng đẳng thức hiệu hai bình phương và phương pháp đặt nhân tử chung.'
        loigiai_th_s = 'Sai. $%sx^2 - 1 = (%sx)^2 - 1^2 = (%sx - 1)(%sx + 1)$.' % (a2, a, a, a)
        
        vd_da_1_d = '\\True Đa thức $A$ thỏa mãn đẳng thức là $A = %sx$' % k
        vd_da_1_s = 'Đa thức $A$ thỏa mãn đẳng thức là $A = %sx(%sx - 1)$' % (k, a)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Từ $A(%sx - 1)(%sx + 1) = (%sx + 1) \\cdot %sx(%sx - 1) = %sx(%sx - 1)(%sx + 1)$, suy ra $A = %sx$.' % (a, a, a, k, a, k, a, a, k)
        loigiai_vd_s = 'Sai. Chia cả hai vế của $A(%sx - 1)(%sx + 1) = %sx(%sx - 1)(%sx + 1)$ cho $(%sx - 1)(%sx + 1)$ ta được $A = %sx$.' % (a, a, k, a, a, a, a, k)
        
        vdc_da_1_d = '\\True Tại $x = 2$, giá trị của đa thức $A$ bằng $%s$' % (2 * k)
        vdc_da_1_s = 'Tại $x = 2$, giá trị của đa thức $A$ bằng $%s$' % (2 * k + 1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Thay $x = 2$ vào $A = %sx$, ta được $A = %s \\cdot 2 = %s$.' % (k, k, 2 * k)
        loigiai_vdc_s = 'Sai. Thay $x = 2$ vào $A = %sx$, ta được $A = %s \\cdot 2 = %s \\neq %s$.' % (k, k, 2 * k, 2 * k + 1)
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
