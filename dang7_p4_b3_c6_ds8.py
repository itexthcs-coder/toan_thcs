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
def bt_dang7_p4_b3_c6_ds8(self):
    # Dạng 7: Rút gọn biểu thức rồi tìm tất cả các giá trị nguyên của biến để biểu thức nhận giá trị nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo = [
            (3, 2, 0, 1, 7),
            (2, 2, 0, 1, 5),
            (1, 2, 0, 1, 3),
            (2, 3, 1, 3, 7)
        ]
        k, a, b, c, N = random.choice(bo)
        uoc_list = [-N, -1, 1, N]
        x_list = [k + u for u in uoc_list]
        
        if b == 0:
            pt3 = '\\dfrac{x}{x - %s}' % k
            tu3 = 'x'
            tu3_mo = '- x'
        else:
            pt3 = '\\dfrac{x - %s}{x - %s}' % (b, k)
            tu3 = '(x - %s)' % b
            tu3_mo = '- x + %s' % b
            
        noidungcauhoi = ('Cho biểu thức $Q = \\dfrac{2x - 1}{x - %s} + \\dfrac{x + %s}{x - %s} - %s$ (với $x \\neq %s$).\\'
                         'a) Rút gọn biểu thức $Q$.\\'
                         'b) Tìm tất cả các giá trị nguyên của $x$ để $Q$ nhận giá trị nguyên.'
                         % (k, a, k, pt3, k))
        
        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Với $x \\neq %s$, ta có:\\'
                   '$$Q = \\dfrac{(2x - 1) + (x + %s) - %s}{x - %s} = \\dfrac{2x - 1 + x + %s %s}{x - %s} = \\dfrac{2x + %s}{x - %s}.$$\n'
                   '\\item Ta tách biểu thức $Q$ như sau:\\'
                   '$$Q = \\dfrac{2(x - %s) + %s}{x - %s} = 2 + \\dfrac{%s}{x - %s}.$$\\'
                   'Với $x \\in \\mathbb{Z}$, để $Q$ nhận giá trị nguyên thì $x - %s$ phải là ước nguyên của $%s$.\\'
                   'Vì $\\text{Ư}(%s) = \\{-%s; -1; 1; %s\\}$ nên ta có các trường hợp sau:\\'
                   '- $x - %s = -%s \\Leftrightarrow x = %s$ (thỏa mãn $x \\neq %s$).\\'
                   '- $x - %s = -1 \\Leftrightarrow x = %s$ (thỏa mãn $x \\neq %s$).\\'
                   '- $x - %s = 1 \\Leftrightarrow x = %s$ (thỏa mãn $x \\neq %s$).\\'
                   '- $x - %s = %s \\Leftrightarrow x = %s$ (thỏa mãn $x \\neq %s$).\\'
                   'Vậy $x \\in \\{%s; %s; %s; %s\\}$.\n'
                   '\\end{enumEX} \n'
                   % (k, a, tu3, k, a, tu3_mo, k, c, k,
                      k, N, k, N, k, k, N, N, N, N,
                      k, N, x_list[0], k,
                      k, x_list[1], k,
                      k, x_list[2], k,
                      k, N, x_list[3], k,
                      x_list[0], x_list[1], x_list[2], x_list[3]))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
