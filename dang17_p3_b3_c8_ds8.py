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


def bt_dang17_p3_b3_c8_ds8(self):
    # Dạng 17: Bài toán rút thẻ/bốc thăm mô phỏng thực nghiệm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_luot = random.choice([250, 300, 400])
        g1 = random.randint(int(0.06 * n_luot), int(0.1 * n_luot))
        g2 = random.randint(int(0.18 * n_luot), int(0.25 * n_luot))
        g3 = n_luot - g1 - g2
        k_trung = g1 + g2
        n_tiep = random.choice([450, 550, 650, 750])

        val_raw = Decimal(n_tiep * k_trung) / Decimal(n_luot)
        kq = val_raw.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq)
        val_raw_str = str(val_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Trong một sự kiện tri ân khách hàng, ban tổ chức chuẩn bị thùng phiếu bốc thăm trúng thưởng. Sau $%s$ lượt khách hàng đầu tiên bốc thăm ngẫu nhiên, kết quả thống kê được ghi trong bảng sau:\\
\begin{center}
\begin{tabular}{|l|c|c|c|}
\hline
Loại phiếu & Giải Nhất & Giải Khuyến khích & Chúc may mắn \\
\hline
Số lượt khách & $%s$ & $%s$ & $%s$ \\
\hline
\end{tabular}
\end{center}
Dự đoán trong $%s$ lượt khách tiếp theo, có khoảng bao nhiêu lượt khách trúng giải (gồm giải Nhất hoặc giải Khuyến khích, làm tròn kết quả đến hàng đơn vị)?'''
                         % (n_luot, g1, g2, g3, n_tiep))

        loigiai = ('''Trong $%s$ lượt khách đầu tiên, số lượt khách trúng giải (gồm giải Nhất hoặc giải Khuyến khích) là: $%s + %s = %s$ (lượt).\\
Xác suất thực nghiệm của biến cố $E$: ``Khách hàng bốc thăm trúng giải'' là $\\dfrac{%s}{%s}$.\\
Gọi $k$ là số lượt khách trúng giải trong $%s$ lượt khách tiếp theo.\\
Ta có $\\dfrac{k}{%s} \\approx \\dfrac{%s}{%s}$, suy ra $k \\approx %s \\cdot \\dfrac{%s}{%s} = %s \\approx %s$.\\
Vậy dự đoán có khoảng $%s$ lượt khách trúng giải.'''
                   % (n_luot, g1, g2, k_trung, k_trung, n_luot, n_tiep, n_tiep, k_trung, n_luot, n_tiep, k_trung, n_luot, val_raw_str, kq_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
