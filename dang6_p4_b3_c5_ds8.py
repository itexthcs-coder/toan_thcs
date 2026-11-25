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

def bt_dang6_p4_b3_c5_ds8(self):
    # Dạng 6: Phân tích biểu đồ cột kép về kim ngạch xuất - nhập khẩu và cán cân thương mại
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xk = [Decimal('371.3'), Decimal('354.7'), Decimal('405.5'), Decimal('438.2')]
        nk = [Decimal('358.9'), Decimal('326.4'), Decimal('380.8'), Decimal('412.5')]
        shift = Decimal(random.choice([0, 5, 10]))
        xk = [x + shift for x in xk]
        nk = [x + shift for x in nk]
        
        tong = [xk[i] + nk[i] for i in range(4)]
        can_can = [xk[i] - nk[i] for i in range(4)]
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        bang_latex = (
            '\\begin{center}\n' +
            '\\begin{tabular}{|l|c|c|c|c|}\n' +
            '\\hline\n' +
            '\\textbf{Năm} & $2022$ & $2023$ & $2024$ & $2025$ \\\\ \\hline\n' +
            '\\textbf{Xuất khẩu (tỉ USD)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % tuple(fmt_vn(x) for x in xk) +
            '\\textbf{Nhập khẩu (tỉ USD)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % tuple(fmt_vn(x) for x in nk) +
            '\\end{tabular}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Số liệu từ biểu đồ cột kép ghi lại trị giá xuất khẩu và trị giá nhập khẩu hàng hóa (đơn vị: tỉ USD) của một quốc gia trong $4$ năm từ $2022$ đến $2025$ được cho trong bảng sau (biết Cán cân thương mại = Trị giá xuất khẩu $-$ Trị giá nhập khẩu; nếu dương gọi là xuất siêu):\n' +
                         bang_latex + '\n' +
                         'a) Tính tổng kim ngạch xuất nhập khẩu (tổng trị giá xuất khẩu và nhập khẩu) của quốc gia đó trong từng năm.\\\n' +
                         'b) Tính mức xuất siêu của quốc gia đó trong từng năm từ $2022$ đến $2025$. Năm nào quốc gia đạt mức xuất siêu cao nhất?')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Tổng kim ngạch xuất nhập khẩu của quốc gia trong từng năm là:\\\\' +
                   '- Năm $2022$: $%s + %s = %s$ (tỉ USD).\\\\' +
                   '- Năm $2023$: $%s + %s = %s$ (tỉ USD).\\\\' +
                   '- Năm $2024$: $%s + %s = %s$ (tỉ USD).\\\\' +
                   '- Năm $2025$: $%s + %s = %s$ (tỉ USD).\n' +
                   '\\item Mức xuất siêu của quốc gia trong từng năm là:\\\\' +
                   '- Năm $2022$: $%s - %s = %s$ (tỉ USD).\\\\' +
                   '- Năm $2023$: $%s - %s = %s$ (tỉ USD).\\\\' +
                   '- Năm $2024$: $%s - %s = %s$ (tỉ USD).\\\\' +
                   '- Năm $2025$: $%s - %s = %s$ (tỉ USD).\\\\' +
                   'So sánh bốn năm, năm $2023$ quốc gia đạt mức xuất siêu cao nhất ($%s$ tỉ USD).\n' +
                   '\\end{enumEX}'
                   ) % (fmt_vn(xk[0]), fmt_vn(nk[0]), fmt_vn(tong[0]),
                        fmt_vn(xk[1]), fmt_vn(nk[1]), fmt_vn(tong[1]),
                        fmt_vn(xk[2]), fmt_vn(nk[2]), fmt_vn(tong[2]),
                        fmt_vn(xk[3]), fmt_vn(nk[3]), fmt_vn(tong[3]),
                        fmt_vn(xk[0]), fmt_vn(nk[0]), fmt_vn(can_can[0]),
                        fmt_vn(xk[1]), fmt_vn(nk[1]), fmt_vn(can_can[1]),
                        fmt_vn(xk[2]), fmt_vn(nk[2]), fmt_vn(can_can[2]),
                        fmt_vn(xk[3]), fmt_vn(nk[3]), fmt_vn(can_can[3]),
                        fmt_vn(can_can[1]))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
