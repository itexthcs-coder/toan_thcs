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


def bt_dang20_p4_b1_c6_ds8(self):
    # Dạng 20: Bài toán Kinh tế - Doanh thu và giá bán sản phẩm nông sản
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            ('2\\,000', '1\\,200', '800', 5, 2, 25, 23), # 1200x + 800(x-5) = 2000x - 4000 => /2000 = x - 2
            ('3\\,000', '2\\,000', '1\\,000', 6, 2, 30, 28), # 2000x + 1000(x-6) = 3000x - 6000 => /3000 = x - 2
            ('2\\,500', '1\\,500', '1\\,000', 5, 2, 28, 26)  # 1500x + 1000(x-5) = 2500x - 5000 => /2500 = x - 2
        ]
        tong_kg, kg1, kg2, giam, tru_tb, x_val, ans = random.choice(scenarios)
        
        noidungcauhoi = ('Một hợp tác xã nông nghiệp thu hoạch được $%s\\text{ kg}$ vải thiều. Trong đợt đầu, hợp tác xã bán được $%s\\text{ kg}$ với giá $x$ nghìn đồng/kg ($x > %s$). Do thời tiết nắng nóng, số vải còn lại phải giảm giá bán $%s$ nghìn đồng/kg so với đợt đầu mới bán hết.\\\\'
                         'a) Viết phân thức biểu thị khối lượng vải bán được ở đợt đầu theo doanh thu $D_1$ (nghìn đồng) của đợt đầu và phân thức biểu thị khối lượng vải bán được ở đợt sau theo doanh thu $D_2$ (nghìn đồng) của đợt sau.\\\\'
                         'b) Lập phân thức biểu thị giá bán trung bình của mỗi kilôgam vải thiều trên toàn bộ vụ thu hoạch theo $x$, rút gọn biểu thức đó và tính giá bán trung bình khi $x = %s$ nghìn đồng/kg.'
                         % (tong_kg, kg1, giam, giam, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Giá bán đợt đầu là $x$ (nghìn đồng/kg) nên khối lượng vải bán được ở đợt đầu là $\\dfrac{D_1}{x}\\text{ (kg)}$.\\\\'
                   'Giá bán đợt sau là $x - %s$ (nghìn đồng/kg) nên khối lượng vải bán được ở đợt sau là $\\dfrac{D_2}{x - %s}\\text{ (kg)}$.\n'
                   '\\item Tổng doanh thu cả hai đợt là $D = %sx + %s(x - %s) = %sx - %s \\cdot %s$ (nghìn đồng).\\\\'
                   'Phân thức biểu thị giá bán trung bình trên toàn bộ vụ thu hoạch là:\\\\'
                   '$P(x) = \\dfrac{%sx + %s(x - %s)}{%s} = \\dfrac{%s(x - %s)}{%s} = x - %s$ (nghìn đồng/kg).\\\\'
                   'Khi $x = %s$ nghìn đồng/kg, giá bán trung bình của mỗi kilôgam vải thiều là $%s - %s = %s$ (nghìn đồng/kg).\n'
                   '\\end{enumEX}'
                   % (giam, giam, kg1, kg2, giam, tong_kg, kg2, giam,
                      kg1, kg2, giam, tong_kg, tong_kg, tru_tb, tong_kg, tru_tb,
                      x_val, x_val, tru_tb, ans))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
