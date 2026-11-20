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


def bt_dang1_p4_b3_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        a1 = Rational(7, 2)
        a2 = Rational(-3, 2)
        b1 = Rational(-2, 3)
        b2 = Rational(5, 3)
        k = random.choice([3, 4, 5])
        c1 = Rational(-5, 4)
        c2 = Rational(13, 4)
        
        A = a1*x**3*y + b1*x**2*y**2 + k*x*y + c1
        B = a2*x**3*y + b2*x**2*y**2 - k*x*y + c2
        
        tong = simplify(A + B)
        x0 = -2
        y0 = Rational(1, 2)
        gt = int(tong.subs({x: x0, y: y0}))
        
        noidungcauhoi = ('''Cho hai đa thức:
                         $$A = 3,5x^3y - \\frac{2}{3}x^2y^2 + %sxy - 1,25; \\qquad B = -1,5x^3y + \\frac{5}{3}x^2y^2 - %sxy + 3,25.$$ \\\\
                         a) Tính đa thức tổng $A + B$ và đa thức hiệu $A - B$, sau đó xác định bậc của mỗi đa thức thu được. \\\\
                         b) Tính giá trị của đa thức $A + B$ tại $x = -2$ và $y = 0,5$.'''
                         % (k, k))
        
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Ta có:
                        \\begin{align*}
                        A + B &= \\left(3,5x^3y - \\frac{2}{3}x^2y^2 + %sxy - 1,25\\right) + \\left(-1,5x^3y + \\frac{5}{3}x^2y^2 - %sxy + 3,25\\right) \\\\
                        &= (3,5 - 1,5)x^3y + \\left(-\\frac{2}{3} + \\frac{5}{3}\\right)x^2y^2 + (%s - %s)xy + (-1,25 + 3,25) \\\\
                        &= %s.
                        \\end{align*}
                        Đa thức $A + B$ có bậc là $4$. \\\\
                        Tương tự, ta có:
                        \\begin{align*}
                        A - B &= \\left(3,5x^3y - \\frac{2}{3}x^2y^2 + %sxy - 1,25\\right) - \\left(-1,5x^3y + \\frac{5}{3}x^2y^2 - %sxy + 3,25\\right) \\\\
                        &= (3,5 + 1,5)x^3y + \\left(-\\frac{2}{3} - \\frac{5}{3}\\right)x^2y^2 + (%s + %s)xy + (-1,25 - 3,25) \\\\
                        &= 5x^3y - \\frac{7}{3}x^2y^2 + %sxy - 4,5.
                        \\end{align*}
                        Đa thức $A - B$ có bậc là $4$. \n
                        \\item Thay $x = -2$ và $y = 0,5$ vào đa thức $A + B = %s$, ta được:
                        $$2 \\cdot (-2)^3 \\cdot 0,5 + (-2)^2 \\cdot 0,5^2 + 2 = -8 + 1 + 2 = %s.$$ \n
                        \\end{enumEX} \n'''
                   % (k, k, k, k, latex(tong),
                      k, k, k, k, 2*k,
                      latex(tong), gt))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
