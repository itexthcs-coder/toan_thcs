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


def bt_dang15_p3_b2_c8_ds8(self):
    # Dạng 15: Ứng dụng lịch và thời gian (chọn ngày trong năm)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        nam, so_ngay, loai_nam = random.choice([
            (2025, 365, "năm không nhuận"),
            (2026, 365, "năm không nhuận"),
            (2024, 366, "năm nhuận"),
            (2028, 366, "năm nhuận")
        ])
        p_dec = (Decimal(12) / Decimal(so_ngay)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).replace('.', ',')
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (3.2,2.2);\n"
            "\\draw[line width=1pt] (0,1.6) -- (3.2,1.6);\n"
            "\\node at (1.6,1.9) {LỊCH NĂM $%s$};\n"
            "\\node at (1.6,0.8) {$%s$ ngày / $12$ tháng};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}" % (nam, so_ngay)
        )
        
        noidungcauhoi = (
            "Chọn ngẫu nhiên một ngày trong năm $%s$ (%s có $%s$ ngày). "
            "Tính xác suất để ngày được chọn là ngày cuối cùng của một tháng trong năm "
            "(viết kết quả dưới dạng số thập phân làm tròn đến hàng phần trăm).\n%s"
            % (nam, loai_nam, so_ngay, hinh_ve)
        )
        
        loigiai = (
            "Năm $%s$ là %s nên có tất cả $%s$ ngày.\\\n"
            "Khi chọn ngẫu nhiên một ngày trong năm, có $%s$ kết quả có thể là đồng khả năng.\\\n"
            "Vì một năm có $12$ tháng và mỗi tháng chỉ có duy nhất một ngày cuối cùng của tháng nên có $12$ ngày thỏa mãn điều kiện bài toán.\\\n"
            "Do đó có $12$ kết quả thuận lợi cho biến cố trên.\\\n"
            "Vậy xác suất để ngày được chọn là ngày cuối cùng của một tháng là: $P = \\dfrac{12}{%s} \\approx %s$."
            % (nam, loai_nam, so_ngay, so_ngay, so_ngay, p_str)
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
