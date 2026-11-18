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


def bt_dang12_p4_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = random.choice([4, 5, 6])
        b_val = 10 - a_val
        tong_diem = 112 + 7*a_val + 9*b_val
        rhs = tong_diem - 112
        tb_dec = Decimal(tong_diem) / Decimal(25)
        tb_str = str(tb_dec).replace('.', ',')
        # Nội dung câu hỏi
        noidungcauhoi = ('''Điểm kiểm tra học kỳ môn Toán của một nhóm $25$ học sinh được ghi lại qua bảng tần số sau:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|c|}
\\hline
Điểm số & $5$ & $6$ & $7$ & $8$ & $9$ & $10$ \\\\
\\hline
Tần số & $2$ & $3$ & $a$ & $8$ & $b$ & $2$ \\\\
\\hline
\\end{tabular}
\\end{center}
Biết điểm số trung bình cộng của cả nhóm học sinh này bằng $%s$. Hãy tính các tần số ẩn $a$ và $b$.''' % tb_str)
        
        # Nội dung lời giải
        loigiai = ('''Vì tổng số học sinh là $25$ nên ta có phương trình:\\
$2 + 3 + a + 8 + b + 2 = 25 \\Leftrightarrow a + b = 10 \\Leftrightarrow a = 10 - b$.\\
Tổng số điểm của cả nhóm học sinh là: $25 \\cdot %s = %s$.\\
Mặt khác, tổng số điểm tính theo bảng tần số là:\\
$5 \\cdot 2 + 6 \\cdot 3 + 7a + 8 \\cdot 8 + 9b + 10 \\cdot 2 = 112 + 7a + 9b$.\\
Suy ra: $112 + 7a + 9b = %s \\Leftrightarrow 7a + 9b = %s$.\\
Thay $a = 10 - b$ vào phương trình trên ta được:\\
$7(10 - b) + 9b = %s \\Leftrightarrow 70 + 2b = %s \\Leftrightarrow 2b = %s \\Leftrightarrow b = %s$.\\
Suy ra $a = 10 - %s = %s$. Vậy $a = %s$ và $b = %s$.''' % (tb_str, tong_diem, tong_diem, rhs, rhs, rhs, rhs - 70, b_val, b_val, a_val, a_val, b_val))
        
        # Xuất câu hỏi tự luận theo cấu trúc @tl
        content = ('\\begin{minipage}{\\textwidth} \n' +
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n' +
                   '\\loigiai{ \n' +
                   str(loigiai) + '}\n' +
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content
