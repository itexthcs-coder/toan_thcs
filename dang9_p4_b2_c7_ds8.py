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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang9_p4_b2_c7_ds8(self):
    # Dạng 9: Biện luận tham số m để phương trình bậc nhất vô nghiệm
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # (m^2 - a)x + b*m = c*x + m + d
        # <=> (m^2 - a - c)x = (1 - b)m + d
        # Chọn a + c = k^2 (ví dụ 1 + 3 = 4, 2 + 7 = 9, 4 + 5 = 9, 5 + 11 = 16)
        a, c, k = random.choice([(1, 3, 2), (2, 7, 3), (4, 5, 3), (5, 11, 4), (7, 9, 4)])
        b = random.choice([2, 3, 4])
        # Đảm bảo với m = k hoặc m = -k thì vế phải khác 0
        d = random.randint(1, 6)
        while (1 - b) * k + d == 0 or (1 - b) * (-k) + d == 0:
            d = random.randint(1, 8)
            
        noidungcauhoi = ('''Cho phương trình ẩn $x$: $(m^2 - %s)x + %sm = %sx + m + %s$. Tìm tất cả các giá trị của tham số $m$ để phương trình đã cho vô nghiệm.'''
                         % (a, b, c, d))
        
        loigiai = ('''Chuyển các hạng tử chứa $x$ về vế trái và các hạng tử không chứa $x$ về vế phải, ta được: \\\\
$(m^2 - %s)x - %sx = m + %s - %sm$ \\\\
$\\Leftrightarrow (m^2 - %s)x = %s - %sm$. \\\\
Phương trình bậc nhất $Ax = B$ vô nghiệm khi và chỉ khi $A = 0$ và $B \\neq 0$, tức là: \\\\
$\\begin{cases} m^2 - %s = 0 \\\\ %s - %sm \\neq 0 \\end{cases} \\Leftrightarrow \\begin{cases} m^2 = %s \\\\ m \\neq %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\text{ hoặc } m = -%s \\\\ m \\neq %s \\end{cases} \\Leftrightarrow m \\in \\{-%s; %s\\}$. \\\\
Vậy với $m = -%s$ hoặc $m = %s$ thì phương trình đã cho vô nghiệm.'''
                   % (a, c, d, b,
                      a + c, d, b - 1,
                      a + c, d, b - 1, a + c, latex(Rational(d, b - 1)), k, k, latex(Rational(d, b - 1)), k, k,
                      k, k))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
