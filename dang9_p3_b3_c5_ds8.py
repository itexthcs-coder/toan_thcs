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

def bt_dang9_p3_b3_c5_ds8(self):
    # Dạng 9: Tính tổng doanh thu từ biểu đồ tranh có nửa biểu tượng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Số biểu tượng: w1 nguyên, w2 có .5, w3 nguyên, w4 có .5 -> tổng nguyên
        w1 = random.randint(3, 5)
        w2_int = random.randint(4, 6)
        w3 = random.randint(5, 7)
        w4_int = random.randint(3, 5)
        tong_bt = w1 + w2_int + w3 + w4_int + 1
        
        dv_ao = 40
        gia_nghin = 125 # 0,125 triệu đồng
        tong_ao = tong_bt * dv_ao
        dt_trieu = int(tong_ao * gia_nghin // 1000)
        kq_str = str(dt_trieu)
        
        bang_latex = (
            '\\begin{center}\n' +
            '\\begin{tabular}{|c|l|}\n' +
            '\\hline\n' +
            '\\textbf{Tuần} & \\textbf{Số biểu tượng áo} \\\\ \\hline\n' +
            'Tuần $1$ & $%s$ biểu tượng đầy đủ \\\\ \\hline\n' % w1 +
            'Tuần $2$ & $%s$ biểu tượng đầy đủ và $1$ nửa biểu tượng \\\\ \\hline\n' % w2_int +
            'Tuần $3$ & $%s$ biểu tượng đầy đủ \\\\ \\hline\n' % w3 +
            'Tuần $4$ & $%s$ biểu tượng đầy đủ và $1$ nửa biểu tượng \\\\ \\hline\n' % w4_int +
            '\\end{tabular}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ tranh thống kê số lượng áo đồng phục bán được của một xưởng may trong $4$ tuần của tháng $9$ được tóm tắt như sau:\n' +
                         bang_latex + '\n' +
                         'Biết mỗi biểu tượng đầy đủ ứng với $%s$ chiếc áo và giá bán mỗi chiếc áo là $%s$ nghìn đồng. Hỏi tổng doanh thu của xưởng may trong cả $4$ tuần đạt bao nhiêu triệu đồng?' % (dv_ao, gia_nghin))
        
        loigiai = ('Tổng số biểu tượng áo bán được trong cả $4$ tuần là:\\\\' +
                   '$$%s + %s,5 + %s + %s,5 = %s \\text{ (biểu tượng)}.$$\\\\' +
                   'Tổng số chiếc áo xưởng may bán được là: $%s \\cdot %s = %s$ (chiếc).\\\\' +
                   'Với giá bán $%s$ nghìn đồng ($0,125$ triệu đồng) mỗi chiếc, tổng doanh thu đạt được là:\\\\' +
                   '$$%s \\cdot 0,125 = %s \\text{ (triệu đồng)}.$$'
                   ) % (w1, w2_int, w3, w4_int, tong_bt, tong_bt, dv_ao, tong_ao, gia_nghin, tong_ao, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
