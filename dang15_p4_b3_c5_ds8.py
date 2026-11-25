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

def bt_dang15_p4_b3_c5_ds8(self):
    # Dạng 15: Khôi phục bảng số liệu hoàn chỉnh từ biểu đồ hình quạt tròn bị khuyết thông tin
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p_xd = 35
        p_db = 15
        p_xdd = 2 * p_db # 30
        p_dd = 100 - (p_xd + p_db + p_xdd) # 20
        
        hieu_hs = random.choice([150, 180, 210, 240])
        tong_hs = int(hieu_hs * 100 // p_db)
        
        so_xd = int(tong_hs * p_xd // 100)
        so_xdd = int(tong_hs * p_xdd // 100)
        so_db = int(tong_hs * p_db // 100)
        so_dd = int(tong_hs * p_dd // 100)
        
        def fmt_int(n):
            return f"{n:,}".replace(",", "\\,")
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:126:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (126:1.9) arc (126:234:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (234:1.9) arc (234:288:1.9) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (288:1.9) arc (288:360:1.9) -- cycle;\n' +
            '\\node at (63:1.2) {$35\\%%$};\n' +
            '\\node at (180:1.15) {$x\\%%$};\n' +
            '\\node at (261:1.25) {$15\\%%$};\n' +
            '\\node at (324:1.25) {$y\\%%$};\n' +
            '\\draw[line width=1pt, fill=black!10] (2.6,1.2) rectangle (3.0,1.5) node[right, yshift=-4pt] {Xe đạp thường};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.6,0.4) rectangle (3.0,0.7) node[right, yshift=-4pt] {Xe đạp điện};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,-0.4) rectangle (3.0,-0.1) node[right, yshift=-4pt] {Đi bộ};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-1.2) rectangle (3.0,-0.9) node[right, yshift=-4pt] {Gia đình đưa đón};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một cuộc khảo sát về phương tiện đến trường của toàn thể học sinh một trường THCS được biểu diễn bằng biểu đồ hình quạt tròn dưới đây. Biết rằng số học sinh đi xe đạp điện nhiều gấp đôi số học sinh đi bộ và nhiều hơn số học sinh đi bộ là $%s$ em:\n' % hieu_hs +
                         tikz_code + '\n' +
                         'a) Tìm các giá trị $x$, $y$ và tính tổng số học sinh của trường THCS đó.\\\n' +
                         'b) Lập bảng thống kê số lượng học sinh cụ thể ứng với từng nhóm phương tiện đến trường.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Vì số học sinh đi xe đạp điện nhiều gấp đôi số học sinh đi bộ nên tỉ lệ phần trăm tương ứng cũng gấp đôi: $x = 2 \\cdot 15 = 30$.\\\\' +
                   'Tổng tỉ lệ phần trăm trên biểu đồ hình quạt tròn bằng $100\\%%$ nên:\\\\' +
                   '$$y = 100 - (35 + 30 + 15) = 20.$$\\\\' +
                   'Hiệu tỉ lệ phần trăm giữa nhóm đi xe đạp điện và nhóm đi bộ là $30\\%% - 15\\%% = 15\\%%$ ứng với $%s$ học sinh. Do đó tổng số học sinh của trường là:\\\\' +
                   '$$\\dfrac{%s}{15\\%%} = %s \\text{ (học sinh)}.$$\n' +
                   '\\item Số lượng học sinh từng nhóm phương tiện là:\\\\' +
                   '- Xe đạp thường: $%s \\cdot 35\\%% = %s$ (học sinh).\\\\' +
                   '- Xe đạp điện: $%s \\cdot 30\\%% = %s$ (học sinh).\\\\' +
                   '- Đi bộ: $%s \\cdot 15\\%% = %s$ (học sinh).\\\\' +
                   '- Gia đình đưa đón: $%s \\cdot 20\\%% = %s$ (học sinh).\\\\' +
                   'Bảng thống kê số lượng học sinh:\\\\' +
                   '\\begin{center}\n' +
                   '\\begin{tabular}{|l|c|c|c|c|}\n' +
                   '\\hline\n' +
                   '\\textbf{Phương tiện} & Xe đạp thường & Xe đạp điện & Đi bộ & Gia đình đưa đón \\\\ \\hline\n' +
                   '\\textbf{Số học sinh} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' +
                   '\\end{tabular}\n' +
                   '\\end{center}\n' +
                   '\\end{enumEX}'
                   ) % (hieu_hs, hieu_hs, fmt_int(tong_hs),
                        fmt_int(tong_hs), so_xd, fmt_int(tong_hs), so_xdd,
                        fmt_int(tong_hs), so_db, fmt_int(tong_hs), so_dd,
                        so_xd, so_xdd, so_db, so_dd)

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
