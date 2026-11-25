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

def bt_dang20_p1_b3_c5_ds8(self):
    # Dạng 20: Chọn biểu đồ phù hợp để so sánh đa nhóm đối tượng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v_gold = [random.randint(3, 8) for _ in range(4)]
        v_silver = [random.randint(3, 8) for _ in range(4)]
        
        da = 'Biểu đồ cột kép (mỗi lớp gồm $2$ cột biểu diễn số huy chương Vàng và huy chương Bạc)'
        s_pool = [
            'Một biểu đồ hình quạt tròn duy nhất biểu diễn tất cả các số liệu trên',
            'Biểu đồ đoạn thẳng chỉ có một đường biểu diễn duy nhất',
            'Biểu đồ tranh sử dụng bốn biểu tượng khác nhau cho bốn lớp'
        ]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        bang_latex = (
            '\\begin{center}\n' +
            '\\begin{tabular}{|l|c|c|c|c|}\n' +
            '\\hline\n' +
            '\\textbf{Lớp} & $8\\text{A}$ & $8\\text{B}$ & $8\\text{C}$ & $8\\text{D}$ \\\\ \\hline\n' +
            '\\textbf{Huy chương Vàng} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % (v_gold[0], v_gold[1], v_gold[2], v_gold[3]) +
            '\\textbf{Huy chương Bạc} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % (v_silver[0], v_silver[1], v_silver[2], v_silver[3]) +
            '\\end{tabular}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Bảng thống kê sau ghi lại số huy chương Vàng và huy chương Bạc của $4$ lớp khối $8$ đạt được trong Hội khỏe Phù Đổng cấp trường:\n' +
                         bang_latex + '\n' +
                         'Để so sánh trực quan số lượng từng loại huy chương của mỗi lớp, ta nên chọn loại biểu đồ nào?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Để so sánh trực quan hai đại lượng có cùng đơn vị đo (số huy chương Vàng và số huy chương Bạc) trên từng đối tượng riêng biệt (từng lớp $8\\text{A}, 8\\text{B}, 8\\text{C}, 8\\text{D}$), ta sử dụng biểu đồ cột kép là thích hợp nhất.\\\\' +
                   'Vậy chọn phương án: %s.'
                   ) % (da)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
