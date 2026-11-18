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


def bt_dang2_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([(2, 4, 8, 4, 2, 10, 20, 40, 20, 10, 30), (3, 5, 7, 3, 2, 15, 25, 35, 15, 10, 25)])
        m3, m4, m5, m6, m7, f3, f4, f5, f6, f7, f_tren6 = bo_so
        ds = ['3']*m3 + ['4']*m4 + ['5']*m5 + ['6']*m6 + ['7']*m7
        random.shuffle(ds)
        chuoi_ds = '; '.join(ds)

        noidungcauhoi = (
            'Số cuộc gọi hỗ trợ kỹ thuật mà một tổng đài viên tiếp nhận trong $20$ ca trực được ghi lại như sau:\\\\ '
            '$%s$.\\\\ '
            'a) Lập bảng tần số tương đối cho mẫu dữ liệu trên.\\\\ '
            'b) Tính tỉ lệ phần trăm số ca trực mà tổng đài viên tiếp nhận từ $6$ cuộc gọi trở lên.'
        ) % (chuoi_ds)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Cỡ mẫu là $n = 20$. Tần số của các giá trị $3; 4; 5; 6; 7$ lần lượt là $%s; %s; %s; %s; %s$.\\\\ '
            'Tần số tương đối tương ứng của các giá trị đó lần lượt là $%s\\%%; %s\\%%; %s\\%%; %s\\%%; %s\\%%$.\\\\ '
            'Bảng tần số tương đối:\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|c|}\n'
            '\\hline\n'
            'Số cuộc gọi & $3$ & $4$ & $5$ & $6$ & $7$ \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Số ca trực tiếp nhận từ $6$ cuộc gọi trở lên gồm mức $6$ cuộc gọi ($%s\\%%$) và $7$ cuộc gọi ($%s\\%%$), chiếm tỉ lệ: $%s\\%% + %s\\%% = %s\\%%$.\n'
            '\\end{enumEX}'
        ) % (m3, m4, m5, m6, m7, f3, f4, f5, f6, f7, f3, f4, f5, f6, f7, f6, f7, f6, f7, f_tren6)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
