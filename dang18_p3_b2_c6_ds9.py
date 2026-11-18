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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang18_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = randint(1, 2)
        n0 = 20 * k
        x_ans = randint(4, 10)
        tong_khach = n0 + x_ans
        doanh_thu = Rational(tong_khach * (40 - x_ans), 20)
        
        dt_dec = Decimal(str(float(doanh_thu))).quantize(Decimal('0.01')).normalize()
        dt_str = str(dt_dec).replace('.', ',')
        kq_str = str(tong_khach)
        
        giam_n0 = Decimal(str(0.05 * n0)).quantize(Decimal('0.01')).normalize()
        giam_n0_str = str(giam_n0).replace('.', ',')
        
        hs_x = Decimal(str(2 - 0.05 * n0)).quantize(Decimal('0.01')).normalize()
        hs_x_str = str(hs_x).replace('.', ',')
        
        chenh_dt = Decimal(str(2 * n0 - float(doanh_thu))).quantize(Decimal('0.01')).normalize()
        chenh_dt_str = str(chenh_dt).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một công ty lữ hành tổ chức tour tham quan trọn gói cho một nhóm khách. Giá vé ban đầu là $2$ triệu đồng/người nếu đoàn có từ $%s$ người trở xuống. Nếu đoàn có nhiều hơn $%s$ người thì cứ thêm $1$ người, giá vé cho toàn bộ đoàn sẽ giảm $50$ nghìn đồng/người. Biết tổng doanh thu của công ty từ đoàn khách đó là $%s$ triệu đồng và số khách vượt quá $%s$ người (nhưng không quá $%s$ người). Hỏi đoàn khách đó có bao nhiêu người?'''
                         %(str(n0), str(n0), dt_str, str(n0), str(n0 + 10)
                         ))

        # Nội dung lời giải
        loigiai = ('''Đổi $50$ nghìn đồng $= 0,05$ triệu đồng. \\\\
                   Gọi số người tăng thêm so với mức $%s$ người là $x$ (người, $x \\in \\mathbb{N}^*$, $0 < x \\le 10$). \\\\
                   Khi đó tổng số khách của đoàn là $%s + x$ (người) và giá vé mỗi người là $2 - 0,05x$ (triệu đồng). \\\\
                   Theo bài ra, tổng doanh thu đạt $%s$ triệu đồng nên ta có phương trình: \\\\
                   $(%s + x)(2 - 0,05x) = %s$ \\\\
                   $\\Leftrightarrow %s - %sx + 2x - 0,05x^2 = %s$ \\\\
                   $\\Leftrightarrow 0,05x^2 - %sx - %s = 0 \\Leftrightarrow x^2 - %sx - %s = 0$. \\\\
                   Giải phương trình trên ta tìm được hai nghiệm $x_1 = %s$ (thỏa mãn $0 < x \\le 10$) và $x_2 = %s$ (loại). \\\\
                   Vậy đoàn khách đó có tất cả $%s + %s = %s$ người.'''
                   %(str(n0),
                     str(n0),
                     dt_str,
                     str(n0), dt_str,
                     str(2*n0), giam_n0_str, dt_str,
                     hs_x_str, chenh_dt_str,
                     str(40 - n0), str(int(20*(float(doanh_thu) - 2*n0))),
                     str(x_ans), str(40 - n0 - x_ans),
                     str(n0), str(x_ans), kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
