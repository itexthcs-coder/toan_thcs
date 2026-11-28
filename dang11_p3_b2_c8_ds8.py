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


def bt_dang11_p3_b2_c8_ds8(self):
    # Dạng 11: Tung đồng thời các đồng xu cân đối
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        so_xu = random.choice([2, 3])
        if so_xu == 2:
            tong_kq = 4
            thuan_loi = 3
            ten_bc = "Có ít nhất một đồng xu xuất hiện mặt ngửa"
            liet_ke_mau = "$\\{NN; NS; SN; SS\\}$"
            liet_ke_tl = "$\\{NN; NS; SN\\}$"
            p_dec = Decimal('0.75')
        else:
            tong_kq = 8
            thuan_loi = 7
            ten_bc = "Có ít nhất một đồng xu xuất hiện mặt ngửa"
            liet_ke_mau = "$\\{NNN; NNS; NSN; SNN; NSS; SNS; SSN; SSS\\}$"
            liet_ke_tl = "$\\{NNN; NNS; NSN; SNN; NSS; SNS; SSN\\}$"
            p_dec = Decimal('0.88')
        p_str = str(p_dec).replace('.', ',')
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) circle (0.65);\n"
            "\\draw[line width=1pt] (2,0) circle (0.65);\n"
            "\\node at (0,0) {Xu 1};\n"
            "\\node at (2,0) {Xu 2};\n"
            "\\node[below] at (1,-0.8) {Tung đồng thời $%s$ đồng xu cân đối};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % so_xu
        )
        
        noidungcauhoi = (
            "Tung đồng thời $%s$ đồng xu cân đối và đồng chất một lần. "
            "Tính xác suất của biến cố: “%s” (viết kết quả dưới dạng số thập phân làm tròn đến hàng phần trăm).\n%s"
            % (so_xu, ten_bc, hinh_ve)
        )
        
        loigiai = (
            "Kí hiệu $N$ là mặt ngửa, $S$ là mặt sấp. Khi tung đồng thời $%s$ đồng xu cân đối, tập hợp các kết quả có thể là:\\\n"
            "%s, gồm có $%s$ kết quả đồng khả năng.\\\n"
            "Các kết quả thuận lợi cho biến cố “%s” là:\\\n"
            "%s, gồm có $%s$ kết quả thuận lợi.\\\n"
            "Vậy xác suất của biến cố trên là: $P = \\dfrac{%s}{%s} \\approx %s$."
            % (so_xu, liet_ke_mau, tong_kq, ten_bc, liet_ke_tl, thuan_loi, thuan_loi, tong_kq, p_str)
        )
        
        dapan = "\\shortans[0]{$%s$}\n" % p_str

    content = (
        "\\begin{minipage}{\\textwidth}\n"
        "\\begin{ex}\n" +
        str(noidungcauhoi) + str(dapan) +
        "\\loigiai{\n" + str(loigiai) + "}\n"
        "\\end{ex}\n\\end{minipage}\n\n"
    )
    return content
