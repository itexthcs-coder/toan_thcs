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

def bt_dang13_p3_b3_c5_ds8(self):
    # Dạng 13: Bài toán dân số độ tuổi lao động kết hợp biểu đồ hình quạt tròn (Liên môn Địa lí)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p_duoi = Decimal('21.5')
        p_ld = Decimal('68.5')
        p_tren = Decimal('10.0')
        
        dan_tren_nghin = random.choice([280, 320, 360, 400])
        tong_dan_nghin = dan_tren_nghin * 10
        dan_ld_nghin = int(Decimal(tong_dan_nghin) * p_ld / Decimal(100))
        kq_str = str(dan_ld_nghin)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:77.4:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!30] (0,0) -- (77.4:1.9) arc (77.4:324:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (324:1.9) arc (324:360:1.9) -- cycle;\n' +
            '\\node at (38:1.2) {$21,5\\%%$};\n' +
            '\\node at (200:1.15) {$68,5\\%%$};\n' +
            '\\node at (342:1.35) {$10,0\\%%$};\n' +
            '\\draw[line width=1pt, fill=black!10] (2.6,0.9) rectangle (3.0,1.2) node[right, yshift=-4pt] {Dưới $15$ tuổi};\n' +
            '\\draw[line width=1pt, fill=black!30] (2.6,0.0) rectangle (3.0,0.3) node[right, yshift=-4pt] {Từ $15$ đến $64$ tuổi};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-0.9) rectangle (3.0,-0.6) node[right, yshift=-4pt] {Trên $64$ tuổi};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây thống kê cơ cấu dân số của một thành phố năm $2025$ theo ba nhóm tuổi:\n' +
                         tikz_code + '\n' +
                         'Biết số người thuộc nhóm Trên $64$ tuổi của thành phố là $%s$ nghìn người. Hỏi số người thuộc nhóm tuổi lao động chính (Từ $15$ đến $64$ tuổi) của thành phố đó là bao nhiêu nghìn người?' % dan_tren_nghin)
        
        loigiai = ('Nhóm người trên $64$ tuổi chiếm $10,0\\%%$ tổng dân số và có $%s$ nghìn người nên tổng dân số của thành phố là:\\\\' +
                   '$$\\dfrac{%s}{10,0\\%%} = %s \\text{ (nghìn người)}.$$\\\\' +
                   'Số người thuộc nhóm tuổi lao động chính (từ $15$ đến $64$ tuổi) chiếm $68,5\\%%$ tổng dân số, bằng:\\\\' +
                   '$$%s \\cdot 68,5\\%% = %s \\text{ (nghìn người)}.$$'
                   ) % (dan_tren_nghin, dan_tren_nghin, tong_dan_nghin, tong_dan_nghin, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
