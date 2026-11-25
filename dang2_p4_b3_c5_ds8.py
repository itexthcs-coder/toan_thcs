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

def bt_dang2_p4_b3_c5_ds8(self):
    # Dạng 2: Kết hợp biểu đồ cơ cấu chi tiêu công và tổng ngân sách để lập bảng thống kê tuyệt đối
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong_25 = random.choice([10000, 12500, 15000])
        p_gd, p_yt, p_gt, p_qp, p_khac = 34, 24, 22, 14, 6
        
        v_gd = int(tong_25 * p_gd // 100)
        v_yt = int(tong_25 * p_yt // 100)
        v_gt = int(tong_25 * p_gt // 100)
        v_qp = int(tong_25 * p_qp // 100)
        v_khac = int(tong_25 * p_khac // 100)
        
        tong_26 = int(tong_25 * 108 // 100)
        v_gd_26 = int(tong_26 * 36 // 100)
        tang_gd = v_gd_26 - v_gd
        
        def fmt_int(n):
            return f"{n:,}".replace(",", "\\,")
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:122.4:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (122.4:1.9) arc (122.4:208.8:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (208.8:1.9) arc (208.8:288:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!55] (0,0) -- (288:1.9) arc (288:338.4:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (338.4:1.9) arc (338.4:360:1.9) -- cycle;\n' +
            '\\node at (61:1.2) {$34\\%%$};\n' +
            '\\node at (165:1.25) {$24\\%%$};\n' +
            '\\node at (248:1.25) {$22\\%%$};\n' +
            '\\node at (313:1.3) {$14\\%%$};\n' +
            '\\node at (349:1.5) {$6\\%%$};\n' +
            '\\draw[line width=1pt, fill=black!10] (2.6,1.4) rectangle (3.0,1.7) node[right, yshift=-4pt] {Giáo dục và đào tạo};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.6,0.7) rectangle (3.0,1.0) node[right, yshift=-4pt] {Y tế và an sinh};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,0.0) rectangle (3.0,0.3) node[right, yshift=-4pt] {Giao thông và hạ tầng};\n' +
            '\\draw[line width=1pt, fill=black!55] (2.6,-0.7) rectangle (3.0,-0.4) node[right, yshift=-4pt] {Quốc phòng – An ninh};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-1.4) rectangle (3.0,-1.1) node[right, yshift=-4pt] {Các lĩnh vực khác};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Tổng ngân sách chi thường xuyên của một địa phương năm $2025$ là $%s$ tỉ đồng. Biểu đồ hình quạt tròn dưới đây cho biết cơ cấu phân bổ ngân sách cho các lĩnh vực:\n' % fmt_int(tong_25) +
                         tikz_code + '\n' +
                         'a) Lập bảng thống kê số tiền ngân sách (đơn vị: tỉ đồng) phân bổ cho từng lĩnh vực trong năm $2025$.\\\n' +
                         'b) Sang năm $2026$, địa phương dự kiến tăng tổng ngân sách thêm $8\\%%$ so với năm $2025$, đồng thời điều chỉnh tỉ trọng chi cho Giáo dục và đào tạo lên mức $36\\%%$. Tính số tiền ngân sách dành cho Giáo dục và đào tạo năm $2026$ và mức tăng thêm so với năm $2025$.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Số tiền ngân sách phân bổ cho từng lĩnh vực năm $2025$ là:\\\\' +
                   '- Giáo dục và đào tạo: $%s \\cdot 34\\%% = %s$ (tỉ đồng).\\\\' +
                   '- Y tế và an sinh xã hội: $%s \\cdot 24\\%% = %s$ (tỉ đồng).\\\\' +
                   '- Giao thông và hạ tầng đô thị: $%s \\cdot 22\\%% = %s$ (tỉ đồng).\\\\' +
                   '- Quốc phòng – An ninh: $%s \\cdot 14\\%% = %s$ (tỉ đồng).\\\\' +
                   '- Các lĩnh vực khác: $%s \\cdot 6\\%% = %s$ (tỉ đồng).\\\\' +
                   'Ta có bảng thống kê (đơn vị: tỉ đồng):\\\\' +
                   '\\begin{center}\n' +
                   '\\begin{tabular}{|l|c|c|c|c|c|}\n' +
                   '\\hline\n' +
                   '\\textbf{Lĩnh vực} & Giáo dục & Y tế & Giao thông & Quốc phòng & Khác \\\\ \\hline\n' +
                   '\\textbf{Số tiền (tỉ đồng)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' +
                   '\\end{tabular}\n' +
                   '\\end{center}\n' +
                   '\\item Tổng ngân sách năm $2026$ dự kiến là: $%s \\cdot (100\\%% + 8\\%%) = %s$ (tỉ đồng).\\\\' +
                   'Số tiền ngân sách dành cho Giáo dục và đào tạo năm $2026$ là: $%s \\cdot 36\\%% = %s$ (tỉ đồng).\\\\' +
                   'Mức tăng thêm so với năm $2025$ là: $%s - %s = %s$ (tỉ đồng).\n' +
                   '\\end{enumEX}'
                   ) % (fmt_int(tong_25), fmt_int(v_gd), fmt_int(tong_25), fmt_int(v_yt),
                        fmt_int(tong_25), fmt_int(v_gt), fmt_int(tong_25), fmt_int(v_qp),
                        fmt_int(tong_25), fmt_int(v_khac),
                        fmt_int(v_gd), fmt_int(v_yt), fmt_int(v_gt), fmt_int(v_qp), fmt_int(v_khac),
                        fmt_int(tong_25), fmt_int(tong_26), fmt_int(tong_26), fmt_int(v_gd_26),
                        fmt_int(v_gd_26), fmt_int(v_gd), fmt_int(tang_gd))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
