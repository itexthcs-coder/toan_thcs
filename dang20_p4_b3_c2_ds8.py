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


def bt_dang20_p4_b3_c2_ds8(self):
    # Dạng 20 (Thực tế): Bài toán số học ứng dụng – Quy tắc tính nhẩm tích hai số đối xứng quanh bội của 10
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = randint(4, 8)
        so_tan_5 = a1 * 10 + 5
        kq1 = a1 * (a1 + 1) * 100 + 25

        a2 = randint(4, 9)
        b2 = randint(1, 4)
        so_nho = a2 * 10 - b2
        so_lon = a2 * 10 + b2
        kq2 = (a2 * 10)**2 - b2**2
        tong_kq = kq1 + kq2

        noidungcauhoi = ('''a) Chứng minh đẳng thức $(10a + b)(10a - b) = 100a^2 - b^2$ và đẳng thức $(10a + 5)^2 = 100a(a + 1) + 25$.\\\\
                         b) Vận dụng các đẳng thức trên để tính nhẩm nhanh giá trị của biểu thức $M = %s^2 + %s \\cdot %s$ (trình bày rõ các bước biến đổi).'''
                         % (so_tan_5, so_nho, so_lon))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                    \\item Áp dụng hằng đẳng thức hiệu hai bình phương và bình phương của một tổng, ta có
                    \\begin{align*}
                    (10a + b)(10a - b) &= (10a)^2 - b^2 = 100a^2 - b^2; \\\\
                    (10a + 5)^2 &= (10a)^2 + 2 \\cdot 10a \\cdot 5 + 5^2 = 100a^2 + 100a + 25 = 100a(a + 1) + 25.
                    \\end{align*}
                    \\item Áp dụng hai đẳng thức trên, ta tính được
                    \\begin{align*}
                    M &= %s^2 + %s \\cdot %s \\\\
                    &= (10 \\cdot %s + 5)^2 + (10 \\cdot %s - %s)(10 \\cdot %s + %s) \\\\
                    &= \\left[100 \\cdot %s \\cdot (%s + 1) + 25\\right] + (100 \\cdot %s^2 - %s^2) \\\\
                    &= (%s + 25) + (%s - %s) \\\\
                    &= %s + %s = %s.
                    \\end{align*}
                    \\end{enumEX}'''
                   % (so_tan_5, so_nho, so_lon,
                      a1, a2, b2, a2, b2,
                      a1, a1, a2, b2,
                      a1*(a1+1)*100, (a2*10)**2, b2**2,
                      kq1, kq2, tong_kq))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
