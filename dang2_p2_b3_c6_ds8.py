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
def bt_dang2_p2_b3_c6_ds8(self):
    # Dạng 2: Hiệu hai phân thức có mẫu là lũy thừa và đơn thức nhiều biến
    bo = [
        (5, 7, 6, 9, 18, 3, 2, 15, 14),
        (3, 5, 4, 6, 12, 3, 2, 9, 10),
        (7, 4, 6, 15, 30, 5, 2, 35, 8),
        (2, 5, 9, 12, 36, 4, 3, 8, 15)
    ]
    t1, t2, h1, h2, mtc, p1, p2, nt1, nt2 = random.choice(bo)
    
    noidungcauhoi = ('Cho biểu thức $M = \\dfrac{%s}{%sxy^2} - \\dfrac{%s}{%sx^2y}$ (với $x \\neq 0, y \\neq 0$). Xét tính đúng, sai của các khẳng định sau:' % (t1, h1, t2, h2))
    
    list_nb_da_1 = [
        '\\True Mẫu thức chung đơn giản nhất của hai phân thức là $%sx^2y^2$' % mtc,
        'Mẫu thức chung đơn giản nhất của hai phân thức là $%sxy$' % mtc
    ]
    loigiai_nb_1 = ('Vì $\\text{BCNN}(%s, %s) = %s$ và lũy thừa bậc cao nhất của $x, y$ là $x^2, y^2$ nên mẫu thức chung đơn giản nhất là $%sx^2y^2$.' % (h1, h2, mtc, mtc))
    
    list_th_da_1 = [
        '\\True Nhân tử phụ của phân thức $\\dfrac{%s}{%sxy^2}$ là $%sx$' % (t1, h1, p1),
        'Nhân tử phụ của phân thức $\\dfrac{%s}{%sxy^2}$ là $%sy$' % (t1, h1, p1)
    ]
    loigiai_th_1 = ('Ta có $%sx^2y^2 : (%sxy^2) = %sx$ nên nhân tử phụ của phân thức $\\dfrac{%s}{%sxy^2}$ là $%sx$.' % (mtc, h1, p1, t1, h1, p1))
    
    list_vd_da_1 = [
        '\\True Sau khi quy đồng và trừ hai phân thức, tử thức thu gọn là $%sx - %sy$' % (nt1, nt2),
        'Sau khi quy đồng và trừ hai phân thức, tử thức thu gọn là $%sx + %sy$' % (nt1, nt2)
    ]
    loigiai_vd_1 = ('Ta có: $M = \\dfrac{%s \\cdot %sx}{%sx^2y^2} - \\dfrac{%s \\cdot %sy}{%sx^2y^2} = \\dfrac{%sx - %sy}{%sx^2y^2}$. Vậy tử thức thu gọn là $%sx - %sy$.' % (t1, p1, mtc, t2, p2, mtc, nt1, nt2, mtc, nt1, nt2))
    
    list_vdc_da_1 = [
        '\\True Biểu thức $M$ luôn nhận giá trị dương với mọi $x > 0, y < 0$',
        'Biểu thức $M$ luôn nhận giá trị âm với mọi $x > 0, y < 0$'
    ]
    loigiai_vdc_1 = ('Với $x > 0$ và $y < 0$ thì $%sx > 0$ và $-%sy > 0$, suy ra tử thức $%sx - %sy > 0$; đồng thời mẫu thức $%sx^2y^2 > 0$. Do đó $M > 0$ với mọi $x > 0, y < 0$.' % (nt1, nt2, nt1, nt2, mtc))
    
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
