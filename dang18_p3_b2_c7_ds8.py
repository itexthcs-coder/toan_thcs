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


def bt_dang18_p3_b2_c7_ds8(self):
    # Dạng 18: Giải bài toán bằng cách lập phương trình - Toán tính điểm thi
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tong_cau = random.choice([20, 25, 30])
        diem_dung = random.choice([4, 5])
        diem_sai = random.choice([1, 2])
        so_dung = random.randint(tong_cau // 2 + 2, tong_cau - 2)
        so_sai = tong_cau - so_dung
        tong_diem = so_dung * diem_dung - so_sai * diem_sai
        kq_str = str(so_dung)
        
        noidungcauhoi = ('''Trong một kỳ thi học sinh giỏi, đề thi gồm $%s$ câu hỏi trắc nghiệm. Mỗi câu trả lời đúng được cộng $%s$ điểm, mỗi câu trả lời sai bị trừ $%s$ điểm, câu bỏ trống không tính điểm. Bạn Minh đã làm hết tất cả $%s$ câu và đạt được $%s$ điểm. Hỏi bạn Minh đã trả lời đúng bao nhiêu câu?'''
                         % (tong_cau, diem_dung, diem_sai, tong_cau, tong_diem))
        
        loigiai = ('''Gọi số câu bạn Minh trả lời đúng là $x$ (câu) (điều kiện: $x \\in \\mathbb{N}^*$, $x \\le %s$). \\\\
Vì bạn Minh đã làm hết cả $%s$ câu nên số câu bạn Minh trả lời sai là $%s - x$ (câu). \\\\
Số điểm bạn Minh nhận được từ các câu trả lời đúng là $%sx$ (điểm). \\\\
Số điểm bạn Minh bị trừ do các câu trả lời sai là $%s(%s - x)$ (điểm). \\\\
Theo đề bài, tổng số điểm đạt được là $%s$ điểm nên ta có phương trình: \\\\
$%sx - %s(%s - x) = %s$ \\\\
$\\Leftrightarrow %sx - %s + %sx = %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy bạn Minh đã trả lời đúng $%s$ câu.'''
                   % (tong_cau, tong_cau, tong_cau,
                      diem_dung, diem_sai, tong_cau,
                      tong_diem,
                      diem_dung, diem_sai, tong_cau, tong_diem,
                      diem_dung, diem_sai*tong_cau, diem_sai, tong_diem,
                      diem_dung + diem_sai, tong_diem + diem_sai*tong_cau, so_dung,
                      so_dung))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
