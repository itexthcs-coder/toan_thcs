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


def bt_dang3_p3_b3_c8_ds8(self):
    # Dạng 3: Tìm số lượng mẫu cần thiết để đạt kỳ vọng số lần xuất hiện biến cố
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_mau = random.choice([250, 400, 500, 800])
        k_loi = random.choice([10, 16, 20, 25])
        while (n_mau * 50) % k_loi != 0:
            k_loi = random.choice([10, 16, 20, 25])
        k_ky_vong = random.choice([30, 40, 50, 60])
        while (n_mau * k_ky_vong) % k_loi != 0:
            k_ky_vong = random.choice([20, 40, 50, 80])
        n_can = (n_mau * k_ky_vong) // k_loi
        kq_str = str(n_can)

        p_dec = (Decimal(k_loi) / Decimal(n_mau)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        p_str = str(p_dec).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Thống kê tại một trạm thu phí tự động cho thấy trong $%s$ lượt xe đi qua, có $%s$ lượt xe gặp sự cố đọc thẻ. Để thu được dữ liệu của khoảng $%s$ lượt xe gặp sự cố nhằm nâng cấp hệ thống, trạm cần theo dõi khoảng bao nhiêu lượt xe đi qua?'''
                         % (n_mau, k_loi, k_ky_vong))

        loigiai = ('''Xác suất thực nghiệm của biến cố $E$: ``Xe đi qua trạm gặp sự cố đọc thẻ'' là $\\dfrac{%s}{%s} = %s$.\\
Ước lượng xác suất của biến cố $E$ là $P(E) \\approx %s$.\\
Gọi $N$ là số lượt xe cần theo dõi để có khoảng $%s$ lượt xe gặp sự cố.\\
Ta có $P(E) \\approx \\dfrac{%s}{N}$, suy ra $\\dfrac{%s}{N} \\approx %s \\Rightarrow N \\approx \\dfrac{%s}{%s} = %s$.\\
Vậy trạm cần theo dõi khoảng $%s$ lượt xe đi qua.'''
                   % (k_loi, n_mau, p_str, p_str, k_ky_vong, k_ky_vong, k_ky_vong, p_str, k_ky_vong, p_str, kq_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
