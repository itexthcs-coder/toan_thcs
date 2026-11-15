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


def bt_dang11_p3_b3_c2_ds9(self):
    x = symbols('x')
    tong_cau = random.choice([20, 25, 30, 40])
    diem_tang = random.choice([0, 5, 10])
    diem_dung = random.choice([2, 3, 4])
    diem_sai = random.choice([1, 2])
    
    x_min = randint(int(tong_cau * 0.5), int(tong_cau * 0.85))
    diem_chuan = diem_tang + diem_dung * x_min - diem_sai * (tong_cau - x_min) - randint(0, diem_dung + diem_sai - 1)
    
    vp = diem_chuan - diem_tang + diem_sai * tong_cau
    he_so = diem_dung + diem_sai
    ans = math.ceil(vp / he_so)
    kq_str = str(ans)
    
    tang_str = f"Mỗi thí sinh được tặng sẵn {diem_tang} điểm. " if diem_tang > 0 else ""
    hang_tu_do = diem_sai * tong_cau - diem_tang
    
    noidungcauhoi = ('''Trong một cuộc thi gồm $%s$ câu hỏi, thí sinh bắt buộc phải trả lời tất cả các câu hỏi. %sMỗi câu trả lời đúng được cộng $%s$ điểm, mỗi câu trả lời sai bị trừ $%s$ điểm. Để vượt qua vòng thi, thí sinh cần đạt từ $%s$ điểm trở lên. Hỏi thí sinh phải trả lời đúng ít nhất bao nhiêu câu hỏi?'''
                     % (tong_cau, tang_str, diem_dung, diem_sai, diem_chuan))
    
    loigiai = ('''Gọi $x$ ($x \\in \\mathbb{N}^*$, $x \\le %s$) là số câu trả lời đúng. Số câu trả lời sai là $%s - x$. \\
               Tổng số điểm thí sinh đạt được là: $%s + %sx - %s(%s - x) = %sx - %s$. \\
               Để đạt từ $%s$ điểm trở lên, ta có bất phương trình: \\
               $%sx - %s \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow x \\ge %.2f$. \\
               Vì $x \\in \\mathbb{N}^*$ nên thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi.'''
               % (tong_cau, tong_cau,
                  diem_tang, diem_dung, diem_sai, tong_cau, he_so, hang_tu_do,
                  diem_chuan,
                  he_so, hang_tu_do, diem_chuan, he_so, vp, vp / he_so,
                  kq_str))
    
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
