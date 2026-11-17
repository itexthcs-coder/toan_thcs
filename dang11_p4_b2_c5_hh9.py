# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang11_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gio = random.choice([2, 3, 4, 5])
        cung_nho = gio * 30
        cung_lon = 360 - cung_nho
        tg_phut = Rational(cung_nho * 2, 11)
        cung_quay = Rational(cung_nho * 12, 11)
        cung_quay_approx = str(Decimal(float(cung_quay)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        noidungcauhoi = ('''Trên mặt một chiếc đồng hồ có $12$ vạch số chia đường tròn thành $12$ phần bằng nhau (như hình vẽ). Lúc $%s$ giờ đúng, kim giờ chỉ đúng số $%s$ và kim phút chỉ đúng số $12$.\\\\
                         a) Tính số đo cung nhỏ và cung lớn tạo bởi hai đầu kim đồng hồ lúc $%s$ giờ đúng.\\\\
                         b) Hỏi sau bao lâu kể từ lúc $%s$ giờ đúng thì kim phút đuổi kịp kim giờ lần đầu tiên? Khi đó đầu kim phút đã vạch nên một cung có số đo bằng bao nhiêu độ (làm tròn đến hàng phần trăm)?
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\foreach \\x in {1,...,12} {
                             \\draw[line width=1pt] (90-30*\\x:1.65)--(90-30*\\x:1.8);
                             \\node at (90-30*\\x:1.4) {\\x};
                         }
                         \\draw[line width=1pt] (O)--(0:1.05);
                         \\draw[line width=1pt] (O)--(90:1.5);
                         \\fill (O) circle (1.2pt);
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (gio, gio, gio, gio))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Mỗi khoảng giữa hai số liên tiếp trên mặt đồng hồ ứng với một cung có số đo bằng $\\dfrac{360^\\circ}{12} = 30^\\circ$.\\\\
                        Lúc $%s$ giờ đúng, kim giờ và kim phút cách nhau $%s$ khoảng nên góc ở tâm giữa hai kim bằng $%s \\cdot 30^\\circ = %s^\\circ$.\\\\
                        Do đó số đo cung nhỏ bằng $%s^\\circ$ và số đo cung lớn bằng $360^\\circ - %s^\\circ = %s^\\circ$.
                        \\item Trong $1$ phút, đầu kim phút vạch nên một cung có số đo bằng $\\dfrac{360^\\circ}{60} = 6^\\circ$, còn đầu kim giờ vạch nên một cung có số đo bằng $\\dfrac{30^\\circ}{60} = 0,5^\\circ$.\\\\
                        Như vậy sau mỗi phút, kim phút rút ngắn khoảng cách góc so với kim giờ một lượng là $6^\\circ - 0,5^\\circ = 5,5^\\circ = \\dfrac{11}{2}^\\circ$.\\\\
                        Để đuổi kịp kim giờ (khoảng cách ban đầu là $%s^\\circ$), thời gian cần thiết là:\\\\
                        $t = \\dfrac{%s}{5,5} = %s\\text{ (phút)}$.\\\\
                        Khi đó đầu kim phút đã vạch nên một cung có số đo bằng $%s \\cdot 6^\\circ = %s^\\circ \\approx %s^\\circ$.
                        \\end{enumEX}'''
                   % (gio, gio, gio, cung_nho, cung_nho, cung_nho, cung_lon,
                      cung_nho, cung_nho, latex(tg_phut), latex(tg_phut), latex(cung_quay), cung_quay_approx))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
