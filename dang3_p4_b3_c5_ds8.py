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

def bt_dang3_p4_b3_c5_ds8(self):
    # Dạng 3: Phản biện và vẽ lại biểu đồ cột bị bóp méo tỉ lệ (Gốc trục đứng khác 0)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g0 = Decimal('12.0')
        d2 = Decimal('0.2')
        k = random.choice([3, 4])
        dt2 = g0 + d2 # 12.2
        dt1 = g0 + Decimal(k) * d2 # 12.6 hoặc 12.8
        
        h2 = int(d2 * 10) # 2 cm
        h1 = int(Decimal(k) * d2 * 10) # 6 cm hoặc 8 cm
        
        ratio_dec = (dt1 / dt2).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Chi nhánh};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,%s) node[left] {Doanh thu (tỉ đồng)};\n' % (k + 0.8) +
            '\\node[left] at (0,0) {$12,0$};\n' +
            '\\draw[line width=1pt, dashed] (0,1) -- (4.2,1); \\node[left] at (0,1) {$%s$};\n' % fmt_vn(dt2) +
            '\\draw[line width=1pt, dashed] (0,%s) -- (4.2,%s); \\node[left] at (0,%s) {$%s$};\n' % (k, k, k, fmt_vn(dt1)) +
            '\\draw[line width=1pt, fill=black!35] (0.8,0) rectangle (1.8,%s);\n' % k +
            '\\node[above] at (1.3,%s) {$%s$}; \\node[below] at (1.3,0) {Chi nhánh $1$};\n' % (k, fmt_vn(dt1)) +
            '\\draw[line width=1pt, fill=black!15] (2.6,0) rectangle (3.6,1);\n' +
            '\\node[above] at (3.1,1) {$%s$}; \\node[below] at (3.1,0) {Chi nhánh $2$};\n' % fmt_vn(dt2) +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Trong báo cáo tổng kết cuối năm, một siêu thị điện máy đưa ra biểu đồ cột so sánh doanh thu bán máy điều hòa của hai chi nhánh: Chi nhánh $1$ đạt $%s$ tỉ đồng, Chi nhánh $2$ đạt $%s$ tỉ đồng. Trên biểu đồ này, gốc của trục đứng được đặt tại $12,0$ tỉ đồng, mỗi $0,1$ tỉ đồng ứng với $1\\text{ cm}$ chiều cao:\n' % (fmt_vn(dt1), fmt_vn(dt2)) +
                         tikz_code + '\n' +
                         'a) Tính chiều cao thực tế của hai cột trên biểu đồ đã vẽ. Từ đó giải thích vì sao nhìn vào biểu đồ này người xem dễ hiểu lầm rằng doanh thu của Chi nhánh $1$ cao gấp $%s$ lần Chi nhánh $2$.\\\n' % k +
                         'b) Tính tỉ số doanh thu thực tế giữa Chi nhánh $1$ và Chi nhánh $2$ (làm tròn đến chữ số thập phân thứ hai) và nêu cách điều chỉnh trục đứng để biểu đồ phản ánh trung thực sự chênh lệch.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Vì gốc của trục đứng đặt tại $12,0$ tỉ đồng và mỗi $0,1$ tỉ đồng ứng với $1\\text{ cm}$ nên:\\\\' +
                   '- Chiều cao cột của Chi nhánh $1$ là: $\\dfrac{%s - 12,0}{0,1} = %s\\text{ (cm)}$.\\\\' +
                   '- Chiều cao cột của Chi nhánh $2$ là: $\\dfrac{%s - 12,0}{0,1} = %s\\text{ (cm)}$.\\\\' +
                   'Trên hình vẽ, cột của Chi nhánh $1$ cao gấp $\\dfrac{%s}{%s} = %s$ lần cột của Chi nhánh $2$, nên người xem dễ ngộ nhận rằng doanh thu thực tế của Chi nhánh $1$ cũng gấp $%s$ lần Chi nhánh $2$.\n' +
                   '\\item Tỉ số doanh thu thực tế giữa Chi nhánh $1$ và Chi nhánh $2$ là:\\\\' +
                   '$$\\dfrac{%s}{%s} \\approx %s \\text{ (lần)}.$$\\\\' +
                   'Để biểu đồ phản ánh trung thực sự chênh lệch doanh thu giữa hai chi nhánh, cần đặt gốc của trục đứng bắt đầu từ $0$ (tỉ đồng) và chia đều các khoảng đơn vị trên trục đứng.\n' +
                   '\\end{enumEX}'
                   ) % (fmt_vn(dt1), h1, fmt_vn(dt2), h2, h1, h2, k, k, fmt_vn(dt1), fmt_vn(dt2), fmt_vn(ratio_dec))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
