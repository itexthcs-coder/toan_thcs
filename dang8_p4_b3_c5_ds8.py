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

def bt_dang8_p4_b3_c5_ds8(self):
    # Dạng 8: Phân tích bài toán bảo vệ môi trường - Rác thải nhựa qua biểu đồ đoạn thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r21, r23, r25 = random.choice([
            (400, 440, 480),
            (420, 460, 500),
            (440, 480, 520)
        ])
        tc21 = int(r21 * 15 // 100)
        ch21 = r21 - tc21
        
        tc25 = Decimal(r25) * Decimal('37.5') / Decimal(100)
        ch25 = Decimal(r25) - tc25
        
        def fmt_vn(d):
            return str(d).rstrip('0').rstrip('.').replace('.', ',')
            
        bang_latex = (
            '\\begin{center}\n' +
            '\\begin{tabular}{|l|c|c|c|}\n' +
            '\\hline\n' +
            '\\textbf{Năm} & $2021$ & $2023$ & $2025$ \\\\ \\hline\n' +
            '\\textbf{Khối lượng rác phát sinh (tấn/ngày)} & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % (r21, r23, r25) +
            '\\textbf{Tỉ lệ thu gom tái chế ($\\%%$)} & $15\\%%$ & $25\\%%$ & $37,5\\%%$ \\\\ \\hline\n' +
            '\\end{tabular}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Số liệu từ biểu đồ theo dõi khối lượng rác thải nhựa phát sinh trung bình mỗi ngày (đơn vị: tấn/ngày) và tỉ lệ rác thải nhựa được thu gom tái chế ($\\%%$) tại một đô thị ven biển qua các năm được tổng hợp trong bảng sau:\n' +
                         bang_latex + '\n' +
                         'a) Tính khối lượng rác thải nhựa được tái chế mỗi ngày và khối lượng rác thải nhựa chưa được tái chế (phải chôn lấp/xử lí) mỗi ngày tại đô thị đó vào năm $2021$ và năm $2025$.\\\n' +
                         'b) Nhận xét về hiệu quả của chương trình phân loại và tái chế rác thải nhựa tại đô thị này giai đoạn $2021 - 2025$.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item - Vào năm $2021$: Khối lượng rác thải nhựa được tái chế mỗi ngày là $%s \\cdot 15\\%% = %s$ (tấn/ngày); khối lượng chưa được tái chế là $%s - %s = %s$ (tấn/ngày).\\\\' +
                   '- Vào năm $2025$: Khối lượng rác thải nhựa được tái chế mỗi ngày là $%s \\cdot 37,5\\%% = %s$ (tấn/ngày); khối lượng chưa được tái chế là $%s - %s = %s$ (tấn/ngày).\n' +
                   '\\item Nhận xét: Trong giai đoạn $2021 - 2025$, mặc dù tổng lượng rác thải nhựa phát sinh hàng ngày tăng từ $%s$ lên $%s$ tấn/ngày, nhưng nhờ tỉ lệ thu gom tái chế tăng mạnh từ $15\\%%$ lên $37,5\\%%$ nên khối lượng rác tái chế đã tăng từ $%s$ lên $%s$ tấn/ngày và khối lượng rác phải chôn lấp giảm từ $%s$ xuống còn $%s$ tấn/ngày, cho thấy chương trình phân loại và tái chế đạt hiệu quả tích cực.\n' +
                   '\\end{enumEX}'
                   ) % (r21, tc21, r21, tc21, ch21,
                        r25, fmt_vn(tc25), r25, fmt_vn(tc25), fmt_vn(ch25),
                        r21, r25, tc21, fmt_vn(tc25), ch21, fmt_vn(ch25))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
