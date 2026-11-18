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


def bt_dang13_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        noidungcauhoi = ('''Thống kê thời gian chờ thanh toán tại quầy thu ngân (đơn vị: phút) của $60$ khách hàng trong khung giờ sáng cho kết quả:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Thời gian chờ (phút) & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ \\\\
\\hline
Số khách hàng & $18$ & $27$ & $9$ & $6$ \\\\
\\hline
\\end{tabular}
\\end{center}
Trong khung giờ chiều, siêu thị mở thêm quầy thanh toán nhanh và phục vụ thêm $40$ khách hàng, trong đó có $22$ khách chờ dưới $2$ phút, $13$ khách chờ từ $2$ đến dưới $4$ phút, $5$ khách chờ từ $4$ đến dưới $6$ phút và không có khách nào chờ từ $6$ phút trở lên.\\
a) Lập bảng tần số tương đối ghép nhóm cho dữ liệu tổng hợp của cả hai khung giờ sáng và chiều.\\
b) So sánh tỉ lệ khách hàng phải chờ từ $4$ phút trở lên trước và sau khi siêu thị mở thêm quầy thanh toán nhanh.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tổng số khách hàng của cả hai khung giờ là $n = 60 + 40 = 100$ (khách hàng).\\
Tần số tổng hợp của các nhóm lần lượt là: $[0; 2)$ có $18 + 22 = 40$ khách; $[2; 4)$ có $27 + 13 = 40$ khách; $[4; 6)$ có $9 + 5 = 14$ khách; $[6; 8)$ có $6 + 0 = 6$ khách. Ta có bảng tần số tương đối ghép nhóm tổng hợp:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Thời gian chờ (phút) & $[0; 2)$ & $[2; 4)$ & $[4; 6)$ & $[6; 8)$ \\\\
\\hline
Tần số tương đối & $40\\%%$ & $40\\%%$ & $14\\%%$ & $6\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Trong khung giờ sáng (trước khi mở thêm quầy), tỉ lệ khách chờ từ $4$ phút trở lên là: $\\dfrac{9 + 6}{60} \\cdot 100\\%% = 25\\%%$.\\
Tính chung cả hai khung giờ (sau khi mở thêm quầy), tỉ lệ này giảm xuống còn: $14\\%% + 6\\%% = 20\\%%$ (riêng buổi chiều chỉ còn $\\dfrac{5}{40} \\cdot 100\\%% = 12,5\\%%$). Điều này cho thấy quầy thanh toán nhanh đã rút ngắn đáng kể thời gian chờ đợi của khách hàng.
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
