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

def bt_dang12_p4_b3_c5_ds8(self):
    # Dạng 12: Bài toán tối ưu hóa quy ước biểu tượng khi lập biểu đồ tranh từ bảng số liệu lớn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # 450, 600, 525, 750 -> ƯCLN = 75 -> quy ước 150 cây (3, 4, 3.5, 5 biểu tượng)
        mult = random.choice([1, 2])
        c1, c2, c3, c4 = 450 * mult, 600 * mult, 525 * mult, 750 * mult
        dv = 150 * mult
        tong = c1 + c2 + c3 + c4
        pct_tc = (Decimal(c4 * 100) / Decimal(tong)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        bang_latex = (
            '\\begin{center}\n' +
            '\\begin{tabular}{|l|c|c|c|c|}\n' +
            '\\hline\n' +
            '\\textbf{Xã} & Minh Tân & Hòa Bình & Đại Đồng & Thành Công \\\\ \\hline\n' +
            '\\textbf{Số lượng cây (cây)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % (c1, c2, c3, c4) +
            '\\end{tabular}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Bảng thống kê dưới đây ghi lại số lượng cây xanh được trồng mới trong chiến dịch "Tết trồng cây" của bốn xã thuộc một huyện:\n' +
                         bang_latex + '\n' +
                         'a) Nếu muốn biểu diễn bảng số liệu trên bằng biểu đồ tranh sao cho không phải vẽ quá nhiều biểu tượng và chỉ dùng biểu tượng đầy đủ hoặc nửa biểu tượng, em hãy chọn một quy ước giá trị cho mỗi biểu tượng và giải thích cách chọn.\\\n' +
                         'b) Với quy ước vừa chọn, hãy xác định số biểu tượng cần vẽ cho từng xã và tính tỉ lệ phần trăm số cây xã Thành Công trồng được so với tổng số cây của cả bốn xã (làm tròn đến chữ số thập phân thứ nhất).')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Ta thấy ước chung lớn nhất của bốn số liệu $%s, %s, %s, %s$ là $%s$. Để số biểu tượng vẽ ra gọn gàng (từ $3$ đến $5$ biểu tượng mỗi hàng) và chỉ sử dụng biểu tượng đầy đủ hoặc nửa biểu tượng, ta chọn quy ước: $1$ biểu tượng đầy đủ ứng với $%s$ cây (khi đó nửa biểu tượng ứng với $%s$ cây).\n' +
                   '\\item Với quy ước $1$ biểu tượng ứng với $%s$ cây, số biểu tượng cần vẽ cho từng xã là:\\\\' +
                   '- Xã Minh Tân: $%s : %s = 3$ biểu tượng đầy đủ.\\\\' +
                   '- Xã Hòa Bình: $%s : %s = 4$ biểu tượng đầy đủ.\\\\' +
                   '- Xã Đại Đồng: $%s : %s = 3,5$ (tức $3$ biểu tượng đầy đủ và $1$ nửa biểu tượng).\\\\' +
                   '- Xã Thành Công: $%s : %s = 5$ biểu tượng đầy đủ.\\\\' +
                   'Tổng số cây trồng được của cả bốn xã là: $%s + %s + %s + %s = %s$ (cây).\\\\' +
                   'Tỉ lệ phần trăm số cây xã Thành Công trồng được so với cả bốn xã là:\\\\' +
                   '$$\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%.$$\n' +
                   '\\end{enumEX}'
                   ) % (c1, c2, c3, c4, 75 * mult, dv, 75 * mult,
                        dv, c1, dv, c2, dv, c3, dv, c4, dv,
                        c1, c2, c3, c4, tong, c4, tong, fmt_vn(pct_tc))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
