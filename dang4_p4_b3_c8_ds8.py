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


def bt_dang4_p4_b3_c8_ds8(self):
    # Dạng 4: Khôi phục bảng thống kê hai chiều bị khuyết dữ liệu (Quản trị nhân sự)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        def fmt_int(n):
            return '{:,}'.format(int(n)).replace(',', '\\,')
        
        def fmt_dec(val, places=None):
            if places is not None:
                d = Decimal(str(val)).quantize(Decimal(places), rounding=ROUND_HALF_UP)
                s = format(d, 'f')
            else:
                s = str(val)
            return s.replace('.', ',')
        
        def round_int(val):
            return int(Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        
        def round_ten(val):
            return int(Decimal(str(val)).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
        nam_b = random.choice([60, 65, 70])
        nu_b = random.choice([50, 55, 60])
        nam_t = random.choice([35, 40, 45])
        nu_t = random.choice([30, 35, 40])
        nam_n = random.choice([70, 75, 80])
        nu_n = random.choice([55, 60, 65])
        
        hl_nam_b = nam_b - random.choice([10, 12, 15])
        hl_nu_b = nu_b - random.choice([9, 11, 12])
        hl_nam_t = nam_t - random.choice([8, 10, 12])
        hl_nu_t = nu_t - random.choice([6, 7, 8])
        hl_nam_n = nam_n - random.choice([12, 14, 15])
        hl_nu_n = nu_n - random.choice([10, 12, 14])
        
        tot_nam = nam_b + nam_t + nam_n
        tot_nu = nu_b + nu_t + nu_n
        tot_hl_nam = hl_nam_b + hl_nam_t + hl_nam_n
        tot_hl_nu = hl_nu_b + hl_nu_t + hl_nu_n
        
        tot_nv = tot_nam + tot_nu
        tot_hl = tot_hl_nam + tot_hl_nu
        
        tot_trung = nam_t + nu_t
        hl_trung = hl_nam_t + hl_nu_t
        khl_trung = tot_trung - hl_trung
        
        frac_e = Fraction(khl_trung, tot_trung)
        p_e_str = fmt_dec(Decimal(khl_trung) / Decimal(tot_trung), '0.001')
        
        n_moi = random.choice([200, 220, 250, 280])
        du_doan_hl = round_int(Decimal(n_moi) * Decimal(tot_hl) / Decimal(tot_nv))
        
        noidungcauhoi = ('''Công ty công nghệ X khảo sát mức độ hài lòng về môi trường làm việc của toàn bộ nhân viên tại 3 chi nhánh Bắc, Trung, Nam. Bảng thống kê dưới đây bị mờ một số ô dữ liệu:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Chi nhánh & Số nhân viên Nam & Số nhân viên Nữ & Số Nam hài lòng & Số Nữ hài lòng \\
\\hline
Miền Bắc & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
Miền Trung & $%s$ & $?$ & $?$ & $%s$ \\
\\hline
Miền Nam & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
Tổng cộng & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
a) Tìm các giá trị còn thiếu trong bảng trên.\\
b) Chọn ngẫu nhiên một nhân viên ở chi nhánh Miền Trung, hãy ước lượng xác suất của biến cố $E$: "Nhân viên được chọn không hài lòng với môi trường làm việc" (làm tròn đến hàng phần nghìn).\\
c) Nếu công ty tuyển dụng thêm $%s$ nhân viên mới theo đúng cơ cấu hiện tại, dự đoán có bao nhiêu nhân viên mới sẽ hài lòng với môi trường làm việc?'''
                         % (nam_b, nu_b, hl_nam_b, hl_nu_b,
                            nam_t, hl_nu_t,
                            nam_n, nu_n, hl_nam_n, hl_nu_n,
                            tot_nam, tot_nu, tot_hl_nam, tot_hl_nu,
                            n_moi))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Số nhân viên Nữ ở chi nhánh Miền Trung là: $%s - (%s + %s) = %s$ (nhân viên).\\
Số nhân viên Nam hài lòng ở chi nhánh Miền Trung là: $%s - (%s + %s) = %s$ (nhân viên).
\\item Tổng số nhân viên ở chi nhánh Miền Trung là: $%s + %s = %s$ (nhân viên).\\
Số nhân viên hài lòng ở chi nhánh Miền Trung là: $%s + %s = %s$ (nhân viên).\\
Suy ra số nhân viên không hài lòng ở chi nhánh Miền Trung là: $%s - %s = %s$ (nhân viên).\\
Xác suất thực nghiệm của biến cố $E$ là $\\dfrac{%s}{%s} \\approx %s$.\\
Vậy xác suất của biến cố $E$ được ước lượng là $%s$.
\\item Tổng số nhân viên hiện tại của công ty là: $%s + %s = %s$ (nhân viên).\\
Tổng số nhân viên hài lòng hiện tại của công ty là: $%s + %s = %s$ (nhân viên).\\
Xác suất một nhân viên bất kì của công ty hài lòng với môi trường làm việc được ước lượng là $\\dfrac{%s}{%s}$.\\
Nếu công ty tuyển dụng thêm $%s$ nhân viên mới, số nhân viên mới dự đoán sẽ hài lòng là: $%s \\cdot \\dfrac{%s}{%s} \\approx %s$ (nhân viên).
\\end{enumEX}'''
                   % (tot_nu, nu_b, nu_n, nu_t,
                      tot_hl_nam, hl_nam_b, hl_nam_n, hl_nam_t,
                      nam_t, nu_t, tot_trung,
                      hl_nam_t, hl_nu_t, hl_trung,
                      tot_trung, hl_trung, khl_trung,
                      khl_trung, tot_trung, p_e_str, p_e_str,
                      tot_nam, tot_nu, tot_nv,
                      tot_hl_nam, tot_hl_nu, tot_hl,
                      tot_hl, tot_nv,
                      n_moi, n_moi, tot_hl, tot_nv, du_doan_hl))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
