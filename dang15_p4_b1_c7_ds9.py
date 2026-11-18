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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang15_p4_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        f0, f1, f2, f3, f4 = 8, 12, 50, 110, 20
        tong_mui = 0*f0 + 1*f1 + 2*f2 + 3*f3 + 4*f4
        co_mau = 200
        tb = Decimal(tong_mui) / Decimal(co_mau)
        tb_str = str(tb).replace('.', ',')
        tu_3 = f3 + f4
        pct_3 = tu_3 * 100 // co_mau
        # Nội dung câu hỏi
        noidungcauhoi = ('''Dựa vào bảng tần số khảo sát số lượng tiêm phòng vắc-xin của $200$ hộ dân trong khu phố:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
Số mũi tiêm & $0$ & $1$ & $2$ & $3$ & $4$ \\\\
\\hline
Số hộ dân & $8$ & $12$ & $50$ & $110$ & $20$ \\\\
\\hline
\\end{tabular}
\\end{center}
a) Tính số mũi tiêm phòng vắc-xin trung bình cho mỗi hộ dân trong khu phố.\\\\
b) Đánh giá xem đa số hộ dân đã đạt mức tiêm từ $3$ mũi trở lên hay chưa.''')
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \\
    \\item Tổng số mũi tiêm phòng vắc-xin của tất cả các hộ dân là:\\
    $0 \\cdot 8 + 1 \\cdot 12 + 2 \\cdot 50 + 3 \\cdot 110 + 4 \\cdot 20 = 0 + 12 + 100 + 330 + 80 = 522$ (mũi).\\
    Số mũi tiêm trung bình cho mỗi hộ dân là: $\\dfrac{522}{200} = 2,61$ (mũi).\\
    \\item Đánh giá: Số hộ dân đạt từ $3$ mũi trở lên là $110 + 20 = 130$ hộ, chiếm $\\dfrac{130}{200} \\cdot 100\\%% = 65\\%% > 50\\%%$ tổng số hộ. Do đó, đa số hộ dân đã đạt mức tiêm từ $3$ mũi trở lên.\\
\\end{enumEX}''')
        
        # Xuất câu hỏi tự luận theo cấu trúc @tl
        content = ('\\begin{minipage}{\\textwidth} \n' +
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n' +
                   '\\loigiai{ \n' +
                   str(loigiai) + '}\n' +
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content
