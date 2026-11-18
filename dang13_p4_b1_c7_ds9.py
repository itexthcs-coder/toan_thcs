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
    QApplication, QMainWindow, Widget, QDialog, QLabel, QLineEdit, 
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


def bt_dang13_p4_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n1 = 40
        n2 = 45
        kg1 = random.choice([140, 160])
        kg2 = random.choice([180, 225])
        tb1_str = str(Decimal(kg1) / Decimal(n1)).replace('.', ',')
        tb2_str = str(Decimal(kg2) / Decimal(n2)).replace('.', ',')
        tong_kg = kg1 + kg2
        tong_hs = n1 + n2
        tb_chung = (Decimal(tong_kg) / Decimal(tong_hs)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        tb_str = str(tb_chung).replace('.', ',')
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai lớp $9D$ ($40$ học sinh) và $9E$ ($45$ học sinh) cùng tham gia phong trào kế hoạch nhỏ. Lớp $9D$ thu gom được lượng giấy vụn với trung bình mỗi bạn đạt $%s\\text{ kg}$. Lớp $9E$ thu gom được lượng giấy vụn với trung bình mỗi bạn đạt $%s\\text{ kg}$. Tính khối lượng giấy vụn trung bình của một học sinh tính trên tổng số học sinh của cả hai lớp (làm tròn đến chữ số thập phân thứ hai).''' % (tb1_str, tb2_str))
        
        # Nội dung lời giải
        loigiai = ('''Tổng số học sinh của cả hai lớp là: $40 + 45 = 85$ (học sinh).\\
Tổng khối lượng giấy vụn lớp $9D$ thu được là: $40 \\cdot %s = %s\\text{ kg}$.\\
Tổng khối lượng giấy vụn lớp $9E$ thu được là: $45 \\cdot %s = %s\\text{ kg}$.\\
Tổng khối lượng giấy vụn của cả hai lớp là: $%s + %s = %s\\text{ kg}$.\\
Khối lượng giấy vụn trung bình của một học sinh cả hai lớp là:\\
$\\dfrac{%s}{85} \\approx %s\\text{ kg}$.''' % (tb1_str, kg1, tb2_str, kg2, kg1, kg2, tong_kg, tong_kg, tb_str))
        
        # Xuất câu hỏi tự luận theo cấu trúc @tl
        content = ('\\begin{minipage}{\\textwidth} \n' +
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n' +
                   '\\loigiai{ \n' +
                   str(loigiai) + '}\n' +
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content
