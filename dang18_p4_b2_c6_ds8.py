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


def bt_dang18_p4_b2_c6_ds8(self):
    # Dạng 18: Chuyển động đường thủy - Bài toán ca nô xuôi dòng và ngược dòng
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        s_ab = random.choice([48, 60, 72])
        v_nuoc = random.choice([3, 4])
        nghi_phut = 30
        v_cano = 20 if v_nuoc == 4 else 21
        t_xuoi = Rational(s_ab, v_cano + v_nuoc)
        t_nguoc = Rational(s_ab, v_cano - v_nuoc)
        tong_tg = t_xuoi + Rational(1, 2) + t_nguoc
        mtc = '(x + %s)(x - %s)' % (v_nuoc, v_nuoc)

        noidungcauhoi = ('Một ca nô đi xuôi dòng từ bến sông A đến bến sông B cách nhau $%s\\text{ km}$, sau đó nghỉ tại bến B $%s$ phút rồi quay ngược dòng từ B trở về A. Biết vận tốc của dòng nước là $%s\\text{ km/h}$ và vận tốc riêng của ca nô khi nước yên lặng là $x\\ (\\text{km/h})$ ($x > %s$).\\\n'
                         'a) Viết các phân thức biểu thị thời gian ca nô đi xuôi dòng từ A đến B và thời gian ca nô đi ngược dòng từ B về A.\\\n'
                         'b) Quy đồng mẫu thức hai phân thức tìm được ở câu a).\\\n'
                         'c) Nếu vận tốc riêng của ca nô là $%s\\text{ km/h}$ thì tổng thời gian kể từ lúc ca nô xuất phát từ A đến khi quay trở về A là bao nhiêu giờ?'
                         % (s_ab, nghi_phut, v_nuoc, v_nuoc, v_cano))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Vận tốc ca nô khi xuôi dòng là $(x + %s)\\text{ km/h}$ và khi ngược dòng là $(x - %s)\\text{ km/h}$.\\\n'
                   '- Phân thức biểu thị thời gian ca nô đi xuôi dòng từ A đến B là $\\dfrac{%s}{x + %s}$ (giờ).\\\n'
                   '- Phân thức biểu thị thời gian ca nô đi ngược dòng từ B về A là $\\dfrac{%s}{x - %s}$ (giờ).\n'
                   '\\item Mẫu thức chung của hai phân thức là $%s = x^2 - %s$.\\\n'
                   'Quy đồng mẫu thức:\\\n'
                   '- $\\dfrac{%s}{x + %s} = \\dfrac{%s(x - %s)}{%s}$.\\\n'
                   '- $\\dfrac{%s}{x - %s} = \\dfrac{%s(x + %s)}{%s}$.\n'
                   '\\item Đổi $%s$ phút $= \\dfrac{1}{2}$ giờ. Với $x = %s\\text{ km/h}$, ta có:\\\n'
                   '- Thời gian đi xuôi dòng là $\\dfrac{%s}{%s + %s} = %s$ (giờ).\\\n'
                   '- Thời gian đi ngược dòng là $\\dfrac{%s}{%s - %s} = %s$ (giờ).\\\n'
                   'Tổng thời gian kể từ lúc xuất phát đến khi trở về A là $%s + \\dfrac{1}{2} + %s = %s$ (giờ).\n'
                   '\\end{enumEX}'
                   % (v_nuoc, v_nuoc, s_ab, v_nuoc, s_ab, v_nuoc,
                      mtc, v_nuoc**2, s_ab, v_nuoc, s_ab, v_nuoc, mtc, s_ab, v_nuoc, s_ab, v_nuoc, mtc,
                      nghi_phut, v_cano, s_ab, v_cano, v_nuoc, latex(t_xuoi), s_ab, v_cano, v_nuoc, latex(t_nguoc),
                      latex(t_xuoi), latex(t_nguoc), latex(tong_tg)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
