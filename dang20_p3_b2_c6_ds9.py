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

def bt_dang20_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        von = random.choice([100, 200, 500])
        lai_suat = randint(4, 9)
        tong_tien = Decimal(str(von)) * (Decimal('1') + Decimal(str(lai_suat)) / Decimal('100'))**2
        tong_tien = tong_tien.quantize(Decimal('0.0001')).normalize()
        tong_str = str(tong_tien).replace('.', ',')
        
        he_so_vp = (Decimal('1') + Decimal(str(lai_suat)) / Decimal('100'))**2
        he_so_vp_str = str(he_so_vp).replace('.', ',')
        can_vp = Decimal('1') + Decimal(str(lai_suat)) / Decimal('100')
        can_vp_str = str(can_vp).replace('.', ',')
        kq_str = str(lai_suat)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Bác An gửi tiết kiệm $%s$ triệu đồng vào ngân hàng theo thể thức lãi kép kì hạn $1$ năm (tiền lãi sau năm thứ nhất được nhập vào vốn để tính lãi cho năm thứ hai). Sau $2$ năm, tổng số tiền cả vốn lẫn lãi bác An nhận được là $%s$ triệu đồng. Hỏi lãi suất ngân hàng là bao nhiêu phần trăm một năm?'''
                         %(str(von), tong_str
                         ))

        # Nội dung lời giải
        loigiai = ('''Gọi lãi suất ngân hàng là $x\\%%$ một năm (điều kiện $x > 0$). \\\\
                   Số tiền cả vốn lẫn lãi bác An nhận được sau $1$ năm là: $%s\\left(1 + \\frac{x}{100}\\right)$ (triệu đồng). \\\\
                   Số tiền cả vốn lẫn lãi bác An nhận được sau $2$ năm là: $%s\\left(1 + \\frac{x}{100}\\right)^2$ (triệu đồng). \\\\
                   Theo bài ra, sau $2$ năm tổng số tiền nhận được là $%s$ triệu đồng nên ta có phương trình: \\\\
                   $%s\\left(1 + \\frac{x}{100}\\right)^2 = %s \\Leftrightarrow \\left(1 + \\frac{x}{100}\\right)^2 = %s$. \\\\
                   Khai căn hai vế, ta được $1 + \\frac{x}{100} = %s$ hoặc $1 + \\frac{x}{100} = -%s$. \\\\
                   Do $x > 0$ nên $1 + \\frac{x}{100} > 1$, suy ra $1 + \\frac{x}{100} = %s \\Leftrightarrow \\frac{x}{100} = %s \\Leftrightarrow x = %s$. \\\\
                   Vậy lãi suất ngân hàng là $%s\\%%$ một năm.'''
                   %(str(von),
                     str(von),
                     tong_str,
                     str(von), tong_str, he_so_vp_str,
                     can_vp_str, can_vp_str,
                     can_vp_str, str(Decimal(str(lai_suat)) / Decimal('100')).replace('.', ','), kq_str,
                     kq_str
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
