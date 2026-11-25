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


def bt_dang19_p4_b1_c6_ds8(self):
    # Dạng 19: Bài toán Vật lí - Tốc độ trung bình trên cả quãng đường đi và về
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (40, 60, 48), # 2*40*60 / (40+60) = 4800/100 = 48
            (30, 60, 40), # 2*30*60 / (30+60) = 3600/90 = 40
            (60, 90, 72)  # 2*60*90 / (60+90) = 10800/150 = 72
        ]
        v1, v2, v_tb = random.choice(scenarios)
        
        noidungcauhoi = ('Một người đi xe máy từ nhà đến cơ quan dài $s\\text{ (km)}$ ($s > 0$) với vận tốc trung bình $v_1 = %s\\text{ km/h}$, sau đó quay trở về nhà theo đường cũ với vận tốc trung bình $v_2 = x\\text{ (km/h)}$ ($x > 0$). Biết tốc độ trung bình trên cả hành trình đi và về được tính bằng tổng quãng đường chia cho tổng thời gian đi và về.\\\n'
                         'a) Biết tốc độ trung bình $v_{\\text{tb}}$ của người đó trên cả hành trình được rút gọn thành phân thức $\\dfrac{%sx}{x + %s}\\text{ (km/h)}$. Hãy giải thích vì sao $\\dfrac{2s}{\\frac{s}{%s} + \\frac{s}{x}} = \\dfrac{%sx}{x + %s}$ (với $s > 0, x > 0$).\\\n'
                         'b) Tính tốc độ trung bình trên cả hành trình nếu vận tốc lúc về là $%s\\text{ km/h}$.'
                         % (v1, 2 * v1, v1, v1, 2 * v1, v1, v2))
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Tổng thời gian cả đi và về là $\\dfrac{s}{%s} + \\dfrac{s}{x} = \\dfrac{sx + %ss}{%sx} = \\dfrac{s(x + %s)}{%sx}$ (giờ).\\\n'
                   'Do đó tốc độ trung bình trên cả hành trình là:\\\n'
                   '$v_{\\text{tb}} = 2s : \\dfrac{s(x + %s)}{%sx} = 2s \\cdot \\dfrac{%sx}{s(x + %s)} = \\dfrac{%sx}{x + %s}\\text{ (km/h)}$.\n'
                   '\\item Thay $x = %s$ vào phân thức $v_{\\text{tb}} = \\dfrac{%sx}{x + %s}$, ta được:\\\n'
                   '$v_{\\text{tb}} = \\dfrac{%s \\cdot %s}{%s + %s} = \\dfrac{%s}{%s} = %s\\text{ (km/h)}$.\n'
                   '\\end{enumEX}'
                   % (v1, v1, v1, v1, v1, v1, v1, v1, v1, 2 * v1, v1,
                      v2, 2 * v1, v1, 2 * v1, v2, v2, v1, 2 * v1 * v2, v1 + v2, v_tb))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
