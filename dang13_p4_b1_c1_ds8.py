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


def bt_dang13_p4_b1_c1_ds8(self):
    # Dạng 13: Nhân hai đơn thức ba biến hệ số phân số, xác định thành phần và tính giá trị
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tu1, mau1 = 3, 4
        tu2, mau2 = -8, 9
        hs_c = Rational(tu1, mau1) * Rational(tu2, mau2)
        gt_c = hs_c * ((-3) ** 3) * (Rational(1, 2) ** 5) * ((-1) ** 4)

        noidungcauhoi = ('Cho hai đơn thức $A = \\frac{3}{4}x^{2}y^{3}z$ và $B = -\\frac{8}{9}xy^{2}z^{3}$. \\\\\n'
                         'a) Tính tích $C = A \\cdot B$, rồi xác định hệ số, phần biến và bậc của đơn thức $C$. \\\\\n'
                         'b) Tính giá trị của đơn thức $C$ tại $x = -3$; $y = \\frac{1}{2}$; $z = -1$.')

        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Ta có:\n'
                   '\\begin{align*}\n'
                   'C &= A \\cdot B = \\left(\\frac{3}{4}x^{2}y^{3}z\\right) \\cdot \\left(-\\frac{8}{9}xy^{2}z^{3}\\right) \\\\\n'
                   '&= \\left[\\frac{3}{4} \\cdot \\left(-\\frac{8}{9}\\right)\\right](x^{2} \\cdot x)(y^{3} \\cdot y^{2})(z \\cdot z^{3}) \\\\\n'
                   '&= %sx^{3}y^{5}z^{4}.\n'
                   '\\end{align*}\n'
                   'Đơn thức thu gọn $C$ có hệ số là $%s$, phần biến là $x^{3}y^{5}z^{4}$ và bậc là $3 + 5 + 4 = 12$. \n'
                   '\\item Thay $x = -3$; $y = \\frac{1}{2}$; $z = -1$ vào $C$, ta được:\n'
                   '\\begin{align*}\n'
                   'C = %s \\cdot (-3)^{3} \\cdot \\left(\\frac{1}{2}\\right)^{5} \\cdot (-1)^{4} = %s \\cdot (-27) \\cdot \\frac{1}{32} \\cdot 1 = %s.\n'
                   '\\end{align*} \n'
                   '\\end{enumEX} \n'
                   % (latex(hs_c), latex(hs_c), latex(hs_c), latex(hs_c), latex(gt_c)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
