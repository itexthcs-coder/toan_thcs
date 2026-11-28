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


def bt_dang11_p3_b3_c8_ds8(self):
    # Dạng 11: Dự báo lưu lượng giao thông và sự cố đô thị theo khung giờ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_ngay = random.choice([100, 120, 150])
        v0 = random.randint(int(0.25 * n_ngay), int(0.32 * n_ngay))
        v1 = random.randint(int(0.33 * n_ngay), int(0.4 * n_ngay))
        v2 = random.randint(int(0.18 * n_ngay), int(0.24 * n_ngay))
        v3 = n_ngay - (v0 + v1 + v2)
        n_toi = random.choice([60, 90, 120])

        nhom_it = v0 + v1
        nhom_nhieu = v2 + v3
        val_raw = Decimal(n_toi * (nhom_it - nhom_nhieu)) / Decimal(n_ngay)
        kq = val_raw.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)
        val_raw_str = str(val_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Hệ thống camera AI giám sát một ngã tư trong $%s$ ngày ghi nhận số vụ vi phạm vượt đèn đỏ mỗi ngày như bảng sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Số vụ vi phạm & $0$ & $1$ & $2$ & $\\ge 3$ \\
\\hline
Số ngày & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
Dự đoán trong $%s$ ngày tới, số ngày có không quá $1$ vụ vi phạm nhiều hơn số ngày có từ $2$ vụ vi phạm trở lên là khoảng bao nhiêu ngày (làm tròn kết quả đến hàng đơn vị)?'''
                         % (n_ngay, v0, v1, v2, v3, n_toi))

        loigiai = ('''Trong $%s$ ngày giám sát, số ngày có không quá $1$ vụ vi phạm là $%s + %s = %s$ (ngày); số ngày có từ $2$ vụ vi phạm trở lên là $%s + %s = %s$ (ngày).\\
Xác suất thực nghiệm ngày có không quá $1$ vụ vi phạm là $\\dfrac{%s}{%s}$; xác suất thực nghiệm ngày có từ $2$ vụ vi phạm trở lên là $\\dfrac{%s}{%s}$.\\
Chênh lệch số ngày dự đoán trong $%s$ ngày tới là: $%s \\cdot \\dfrac{%s}{%s} - %s \\cdot \\dfrac{%s}{%s} = %s \\cdot \\dfrac{%s}{%s} = %s \\approx %s$ (ngày).'''
                   % (n_ngay, v0, v1, nhom_it, v2, v3, nhom_nhieu, nhom_it, n_ngay, nhom_nhieu, n_ngay,
                      n_toi, n_toi, nhom_it, n_ngay, n_toi, nhom_nhieu, n_ngay, n_toi, nhom_it - nhom_nhieu, n_ngay, val_raw_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \\end{minipage} \n\n')
    return content
