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

def bt_dang8_p3_b3_c5_ds8(self):
    # Dạng 8: Quy đổi số đo góc ở tâm trên biểu đồ hình quạt tròn ra giá trị tuyệt đối
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong_sach = random.choice([2000, 2400, 3000, 3600])
        goc_tk = random.choice([99, 108, 117, 126])
        kq = int(tong_sach * goc_tk // 360)
        kq_str = str(kq)
        
        pct_tk = Decimal(goc_tk * 100) / Decimal(360)
        pct_str = str(pct_tk).rstrip('0').rstrip('.').replace('.', ',')
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.8) arc (0:135:1.8) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!30] (0,0) -- (135:1.8) arc (135:%s:1.8) -- cycle;\n' % (135 + goc_tk) +
            '\\draw[line width=1pt, fill=black!45] (0,0) -- (%s:1.8) arc (%s:315:1.8) -- cycle;\n' % (135 + goc_tk, 135 + goc_tk) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (315:1.8) arc (315:360:1.8) -- cycle;\n' +
            '\\node at (%s:1.1) {$%s^\\circ$};\n' % (135 + goc_tk / 2.0, goc_tk) +
            '\\draw[line width=1pt, fill=black!10] (2.5,1.1) rectangle (2.9,1.4) node[right, yshift=-4pt] {Sách giáo khoa};\n' +
            '\\draw[line width=1pt, fill=black!30] (2.5,0.3) rectangle (2.9,0.6) node[right, yshift=-4pt] {Sách tham khảo};\n' +
            '\\draw[line width=1pt, fill=black!45] (2.5,-0.5) rectangle (2.9,-0.2) node[right, yshift=-4pt] {Truyện thiếu nhi};\n' +
            '\\draw[line width=1pt, fill=white] (2.5,-1.3) rectangle (2.9,-1.0) node[right, yshift=-4pt] {Sách kĩ năng sống};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một thư viện trường học có tổng cộng $%s$ đầu sách gồm bốn thể loại. Khi biểu diễn cơ cấu số sách này bằng biểu đồ hình quạt tròn, góc ở tâm của hình quạt biểu diễn Sách tham khảo đo được là $%s^\\circ$:\n' % (tong_sach, goc_tk) +
                         tikz_code + '\n' +
                         'Tính số đầu sách tham khảo hiện có trong thư viện đó.')
        
        loigiai = ('Vì cả hình tròn ứng với $360^\\circ$ nên tỉ lệ phần trăm của Sách tham khảo trong tổng số sách của thư viện là:\\\\' +
                   '$$\\dfrac{%s^\\circ}{360^\\circ} \\cdot 100\\%% = %s\\%%.$$\\\\' +
                   'Số đầu sách tham khảo hiện có trong thư viện là:\\\\' +
                   '$$%s \\cdot %s\\%% = %s \\text{ (cuốn)}.$$'
                   ) % (goc_tk, pct_str, tong_sach, pct_str, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
