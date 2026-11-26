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


def bt_dang16_p3_b2_c7_ds8(self):
    # Dạng 16: Giải bài toán bằng cách lập phương trình - Chuyển động trên dòng nước
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        t_xuoi = random.randint(3, 6)
        t_nguoc = t_xuoi + random.randint(1, 2)
        v_nuoc = random.randint(2, 4)
        num = v_nuoc * (t_xuoi + t_nguoc)
        den = t_nguoc - t_xuoi
        while num % den != 0:
            v_nuoc = random.randint(2, 5)
            num = v_nuoc * (t_xuoi + t_nguoc)
            
        v_tau = num // den
        kq_str = str(v_tau)
        
        noidungcauhoi = ('''Một tàu thủy chạy xuôi dòng từ bến $A$ đến bến $B$ mất $%s$ giờ và chạy ngược dòng từ $B$ về $A$ mất $%s$ giờ. Biết vận tốc dòng nước là $%s\\text{ km/h}$. Tính vận tốc riêng của tàu thủy khi nước yên lặng (đơn vị: $\\text{km/h}$).'''
                         % (t_xuoi, t_nguoc, v_nuoc))
        
        loigiai = ('''Gọi vận tốc riêng của tàu thủy khi nước yên lặng là $x\\text{ (km/h)}$ (điều kiện: $x > %s$). \\\\
Vận tốc của tàu thủy khi chạy xuôi dòng là $x + %s\\text{ (km/h)}$. \\\\
Vận tốc của tàu thủy khi chạy ngược dòng là $x - %s\\text{ (km/h)}$. \\\\
Quãng đường tàu thủy chạy xuôi dòng từ $A$ đến $B$ là $%s(x + %s)\\text{ (km)}$. \\\\
Quãng đường tàu thủy chạy ngược dòng từ $B$ về $A$ là $%s(x - %s)\\text{ (km)}$. \\\\
Vì quãng đường $AB$ không đổi nên ta có phương trình: \\\\
$%s(x + %s) = %s(x - %s)$ \\\\
$\\Leftrightarrow %sx + %s = %sx - %s$ \\\\
$\\Leftrightarrow %sx - %sx = %s + %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy vận tốc riêng của tàu thủy khi nước yên lặng là $%s\\text{ km/h}$.'''
                   % (v_nuoc, v_nuoc, v_nuoc,
                      t_xuoi, v_nuoc, t_nguoc, v_nuoc,
                      t_xuoi, v_nuoc, t_nguoc, v_nuoc,
                      t_xuoi, t_xuoi*v_nuoc, t_nguoc, t_nguoc*v_nuoc,
                      t_nguoc, t_xuoi, t_xuoi*v_nuoc, t_nguoc*v_nuoc,
                      den, num, v_tau,
                      v_tau))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
