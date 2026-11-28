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


def bt_dang16_p3_b3_c8_ds8(self):
    # Dạng 16: Bài toán xác suất hình học thực nghiệm trên lưới ô vuông/bia tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_ban = random.choice([200, 250, 300])
        k_trung = random.randint(int(0.68 * n_ban), int(0.8 * n_ban))
        k_truot = n_ban - k_trung
        n_them = random.choice([150, 180, 220, 240])

        val_raw = Decimal(n_them * k_truot) / Decimal(n_ban)
        kq = val_raw.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)
        val_raw_str = str(val_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Một vận động viên bắn cung thực hiện $%s$ phát bắn vào một tấm bia tròn có gắn vùng hồng tâm ở giữa, kết quả có $%s$ mũi tên trúng vào vùng hồng tâm.\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.5cm);
\\draw[line width=1pt] (0,0) circle (1.0cm);
\\draw[line width=1pt] (0,0) circle (0.45cm);
\\fill (0.15,-0.1) circle (1pt);
\\fill (-0.2,0.15) circle (1pt);
\\fill (0.8,0.5) circle (1pt);
\\fill (-1.1,-0.4) circle (1pt);
\\end{tikzpicture}
\\end{center}
Nếu vận động viên này thực hiện thêm $%s$ phát bắn với phong độ tương tự, dự đoán có khoảng bao nhiêu mũi tên bắn trượt ra ngoài vùng hồng tâm (làm tròn kết quả đến hàng đơn vị)?'''
                         % (n_ban, k_trung, n_them))

        loigiai = ('''Trong $%s$ phát bắn đầu tiên, số mũi tên bắn trượt ra ngoài vùng hồng tâm là: $%s - %s = %s$ (mũi tên).\\\\
Xác suất thực nghiệm của biến cố $E$: ``Mũi tên bắn trượt ra ngoài vùng hồng tâm'' là $\\dfrac{%s}{%s}$.\\\\
Gọi $k$ là số mũi tên bắn trượt ra ngoài vùng hồng tâm trong $%s$ phát bắn thêm.\\\\
Ta có $\\dfrac{k}{%s} \\approx \\dfrac{%s}{%s}$, suy ra $k \\approx %s \\cdot \\dfrac{%s}{%s} = %s \\approx %s$.\\\\
Vậy dự đoán có khoảng $%s$ mũi tên bắn trượt ra ngoài vùng hồng tâm.'''
                   % (n_ban, n_ban, k_trung, k_truot, k_truot, n_ban, n_them, n_them, k_truot, n_ban, n_them, k_truot, n_ban, val_raw_str, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
