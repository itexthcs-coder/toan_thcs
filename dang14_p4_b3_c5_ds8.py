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

def bt_dang14_p4_b3_c5_ds8(self):
    # Dạng 14: Phân tích biểu đồ đoạn thẳng nhiệt độ và lượng mưa (Biểu đồ khí hậu liên môn Địa lí)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t_max = Decimal('29.5')
        t_min = Decimal('16.5')
        bien_do = t_max - t_min # 13.0
        
        m_mua = random.choice([1400, 1420, 1450])
        m_kho = random.choice([250, 260, 280])
        tong_m = m_mua + m_kho
        pct_mua = (Decimal(m_mua * 100) / Decimal(tong_m)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        
        def fmt_vn(d):
            return str(d).rstrip('0').rstrip('.').replace('.', ',')
            
        noidungcauhoi = ('Quan sát biểu đồ khí hậu của một địa phương nhiệt đới gió mùa ở Việt Nam người ta thu được các số liệu đặc trưng sau:\n' +
                         '- Nhiệt độ trung bình tháng cao nhất rơi vào Tháng $6$ ($29,5^\\circ\\text{C}$), thấp nhất rơi vào Tháng $1$ ($16,5^\\circ\\text{C}$).\n' +
                         '- Lượng mưa trung bình tháng vượt trên $100\\text{ mm}$ kéo dài từ Tháng $5$ đến Tháng $10$ (tổng lượng mưa $6$ tháng này đạt $%s\\text{ mm}$), trong khi tổng lượng mưa $6$ tháng còn lại trong năm chỉ đạt $%s\\text{ mm}$.\n' % (m_mua, m_kho) +
                         'a) Tính biên độ nhiệt năm (hiệu giữa nhiệt độ trung bình tháng cao nhất và tháng thấp nhất) và tổng lượng mưa cả năm của địa phương này.\\\n' +
                         'b) Tính tỉ lệ phần trăm lượng mưa của mùa mưa (từ Tháng $5$ đến Tháng $10$) so với tổng lượng mưa cả năm (làm tròn đến chữ số thập phân thứ nhất) và nhận xét về sự phân mùa khí hậu của địa phương.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Biên độ nhiệt năm của địa phương là: $29,5 - 16,5 = %s^\\circ\\text{C}$.\\\\' +
                   'Tổng lượng mưa cả năm của địa phương là: $%s + %s = %s\\text{ (mm)}$.\n' +
                   '\\item Tỉ lệ phần trăm lượng mưa của mùa mưa so với tổng lượng mưa cả năm là:\\\\' +
                   '$$\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%.$$\\\\' +
                   'Nhận xét: Khí hậu của địa phương có sự phân hóa theo mùa rõ rệt: mùa hạ nóng ẩm, mưa nhiều (chiếm tới $%s\\%%$ tổng lượng mưa cả năm) và mùa đông lạnh, ít mưa (khô hanh).\n' +
                   '\\end{enumEX}'
                   ) % (fmt_vn(bien_do), m_mua, m_kho, tong_m, m_mua, tong_m, fmt_vn(pct_mua), fmt_vn(pct_mua))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
