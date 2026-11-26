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
def bt_dang19_p3_b3_c6_ds8(self):
    # Dạng 19: Bài toán chuyển động đường bộ gồm hai chặng khác vận tốc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # t = s1/x + s2/(x + dv)
        bo = [
            (40, 90, 40, 50, '1,8'),
            (30, 80, 30, 50, '1,6'),
            (24, 100, 60, 40, '1,6'),
            (45, 120, 30, 50, '2,4')
        ]
        s1, s2, dv, x_val, kq_str = random.choice(bo)
        tu_tong = '%sx + %s' % (s1 + s2, s1 * dv)
        
        noidungcauhoi = ('Anh Nam lái xe đi từ tỉnh A đến tỉnh B. Chặng đầu dài $%s\\text{ km}$ anh đi trong khu dân cư với vận tốc $x\\text{ (km/h)}$ ($x > 0$). Chặng sau dài $%s\\text{ km}$ trên đường cao tốc, anh tăng vận tốc thêm $%s\\text{ km/h}$. Khi $x = %s\\text{ km/h}$, tổng thời gian anh Nam đi từ tỉnh A đến tỉnh B là bao nhiêu giờ?' % (s1, s2, dv, x_val))
        
        loigiai = ('Thời gian đi chặng đầu là $\\dfrac{%s}{x}$ (giờ), thời gian đi chặng sau là $\\dfrac{%s}{x + %s}$ (giờ).\\'
                   'Phân thức biểu thị tổng thời gian anh Nam đi từ tỉnh A đến tỉnh B là:\\'
                   '$$t = \\dfrac{%s}{x} + \\dfrac{%s}{x + %s} = \\dfrac{%s(x + %s) + %sx}{x(x + %s)} = \\dfrac{%s}{x(x + %s)}\\text{ (giờ)}.$$\\'
                   'Thay $x = %s$ vào biểu thức trên, ta được tổng thời gian đi là $\\dfrac{%s}{%s} + \\dfrac{%s}{%s} = %s$ (giờ).'
                   % (s1, s2, dv, s1, s2, dv, s1, dv, s2, dv, tu_tong, dv, x_val, s1, x_val, s2, x_val + dv, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
