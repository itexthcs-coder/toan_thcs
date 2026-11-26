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


def bt_dang17_p3_b3_c7_ds8(self):
    # Dạng 17: Ứng dụng thực tế hàm số vào bài toán tính cước taxi
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        gia_mo_cua = random.choice([12, 14, 15, 16])  # nghìn đồng
        gia_tiep = random.choice([10, 11, 12, 13])    # nghìn đồng/km
        x_km = random.randint(6, 18)

        tong_tien = gia_mo_cua + gia_tiep * (x_km - 1)
        kq_str = str(tong_tien)

        noidungcauhoi = ('''Giá cước của một hãng taxi công nghệ được tính như sau: mở cửa (cho $1\\text{ km}$ đầu tiên) giá $%s\\,000$ đồng; từ sau ki-lô-mét thứ nhất trở đi, mỗi ki-lô-mét tính thêm $%s\\,000$ đồng. Gọi $T$ (nghìn đồng) là số tiền khách phải trả khi đi quãng đường $x\\text{ km}$ ($x > 1$). Tính giá trị của $T$ khi $x = %s$.'''
                         % (gia_mo_cua, gia_tiep, x_km))

        loigiai = ('''Khi khách hàng đi quãng đường $x\\text{ km}$ ($x > 1$) thì quãng đường tính cước từ sau ki-lô-mét đầu tiên là $(x - 1)\\text{ km}$. \\\\
Do đó, hàm số biểu thị số tiền $T$ (nghìn đồng) khách phải trả theo quãng đường $x$ là: \\\\
$T = f(x) = %s + %s(x - 1)$. \\\\
Thay $x = %s$ vào công thức hàm số trên, ta được: \\\\
$T = f(%s) = %s + %s \\cdot (%s - 1) = %s + %s \\cdot %s = %s + %s = %s$. \\\\
Vậy khi đi quãng đường $%s\\text{ km}$ thì giá trị của $T$ là $%s$ (nghìn đồng).'''
                   % (gia_mo_cua, gia_tiep,
                      x_km,
                      x_km, gia_mo_cua, gia_tiep, x_km,
                      gia_mo_cua, gia_tiep, x_km - 1,
                      gia_mo_cua, gia_tiep * (x_km - 1), kq_str,
                      x_km, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
