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


def bt_dang19_p3_b2_c8_ds8(self):
    # Dạng 19: Bài toán thực tế về mã khóa / mật khẩu đơn giản
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        so_vong = random.choice([2, 3])
        if so_vong == 2:
            tong_kq = 100
            vi_du = "$00; 11; 22; \\dots; 99$"
            p_dec = Decimal('0.1')
        else:
            tong_kq = 1000
            vi_du = "$000; 111; 222; \\dots; 999$"
            p_dec = Decimal('0.01')
        p_str = str(p_dec).replace('.', ',')
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (3.6,1.6);\n"
            "\\draw[line width=1pt] (0.8,1.6) arc (180:0:1);\n"
            "\\draw[line width=1pt] (0.5,0.4) rectangle (1.3,1.2);\n"
            "\\draw[line width=1pt] (1.4,0.4) rectangle (2.2,1.2);\n"
            "\\draw[line width=1pt] (2.3,0.4) rectangle (3.1,1.2);\n"
            "\\node at (0.9,0.8) {$0$};\n"
            "\\node at (1.8,0.8) {$0$};\n"
            "\\node at (2.7,0.8) {$0$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )
        
        noidungcauhoi = (
            "Một ổ khóa số gồm $%s$ vòng xoay độc lập, mỗi vòng có các chữ số từ $0$ đến $9$. "
            "Một người quên mật khẩu nên xoay ngẫu nhiên tất cả các vòng số để thử mở khóa. "
            "Biết mật khẩu đúng gồm $%s$ chữ số giống nhau (ví dụ %s). "
            "Tính xác suất để ngay lần thử đầu tiên người đó xoay được mật khẩu gồm $%s$ chữ số giống nhau "
            "(viết kết quả dưới dạng số thập phân).\n%s"
            % (so_vong, so_vong, vi_du, so_vong, hinh_ve)
        )
        
        loigiai = (
            "Mỗi vòng xoay có $10$ cách chọn chữ số từ $0$ đến $9$.\\\n"
            "Khi xoay ngẫu nhiên $%s$ vòng số độc lập, tổng số mã số có thể tạo thành là $%s$ mã số và các kết quả này là đồng khả năng.\\\n"
            "Các mã số gồm $%s$ chữ số giống nhau là: %s, gồm có $10$ kết quả thuận lợi.\\\n"
            "Vậy xác suất để ngay lần thử đầu tiên người đó xoay được mật khẩu gồm $%s$ chữ số giống nhau là:\\\n"
            "$P = \\dfrac{10}{%s} = %s$."
            % (so_vong, tong_kq, so_vong, vi_du, so_vong, tong_kq, p_str)
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
