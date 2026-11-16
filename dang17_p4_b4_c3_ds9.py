# -*- coding: utf-8 -*-
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

def bt_dang17_p4_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([3, 4, 5])
        P1 = 1013 - k**3
        v1 = Decimal(str(6.3 * k)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        v1_str = str(v1).replace('.', ',')

        P2 = randint(890, 930)
        while P2 == P1:
            P2 = randint(890, 930)
        delta_P2 = 1013 - P2
        v2 = Decimal(str(6.3 * (delta_P2**(1/3)))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        v2_str = str(v2).replace('.', ',')

        noidungcauhoi = ('''Tốc độ gió $v$ (tính bằng $\\text{m/s}$) ở tâm một cơn bão nhiệt đới có mối liên hệ với áp suất khí quyển $P$ (tính bằng $\\text{hPa}$) tại tâm bão thông qua công thức thực nghiệm: $v = 6,3\\sqrt[3]{1013 - P}$. \\\\
                         a) Tính tốc độ gió ở tâm một cơn bão khi áp suất tại tâm bão đo được là $%s\\text{ hPa}$. \\\\
                         b) Một cơn bão được phân loại là "siêu bão" khi tốc độ gió tại tâm đạt từ $51,5\\text{ m/s}$ trở lên. Hỏi khi áp suất tại tâm bão giảm xuống mức $%s\\text{ hPa}$ thì cơn bão đó đã đạt cấp độ siêu bão chưa? Giải thích (làm tròn tốc độ gió đến chữ số thập phân thứ hai).'''
                         % (str(P1), str(P2)))

        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                   \\item Thay $P = %s$ vào công thức, ta được tốc độ gió ở tâm bão là: \\\\
                   $v = 6,3\\sqrt[3]{1013 - %s} = 6,3\\sqrt[3]{%s} = 6,3 \\cdot %s = %s\\text{ (m/s)}$. \n
                   \\item Khi $P = %s\\text{ hPa}$, tốc độ gió tại tâm bão là: \\\\
                   $v = 6,3\\sqrt[3]{1013 - %s} = 6,3\\sqrt[3]{%s} \\approx %s\\text{ (m/s)}$. \\\\
                   Vì $%s\\text{ m/s} < 51,5\\text{ m/s}$ nên cơn bão này chưa đạt cấp độ siêu bão. \n
                   \\end{enumEX} \n'''
                   % (str(P1), str(P1), str(k**3), str(k), v1_str,
                      str(P2), str(P2), str(delta_P2), v2_str, v2_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
