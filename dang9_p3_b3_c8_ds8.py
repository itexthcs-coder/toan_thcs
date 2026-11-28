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


def bt_dang9_p3_b3_c8_ds8(self):
    # Dạng 9: Dự báo tỉ lệ hạt nảy mầm và tính lượng hạt giống cần gieo trồng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_gieo = random.choice([400, 500, 600, 800])
        p_chon = random.choice([0.85, 0.88, 0.9, 0.92, 0.95])
        k_nay = int(Decimal(str(p_chon)) * Decimal(n_gieo))
        he_so = random.choice([8, 10, 12, 15])
        n_can = n_gieo * he_so
        k_cay_con = k_nay * he_so
        kq_str = str(n_can)
        p_str = str(Decimal(str(p_chon))).replace('.', ',')

        noidungcauhoi = ('''Viện nghiên cứu nông nghiệp gieo thử nghiệm $%s$ hạt giống ngô lai mới thì thấy có $%s$ hạt nảy mầm. Một nông trại muốn thu được khoảng $%s$ cây ngô con khỏe mạnh thì cần gieo khoảng bao nhiêu hạt giống loại này?'''
                         % (n_gieo, k_nay, k_cay_con))

        loigiai = ('''Xác suất thực nghiệm của biến cố $E$: ``Hạt giống ngô nảy mầm'' là $\\dfrac{%s}{%s} = %s$.\\
Ước lượng xác suất nảy mầm của hạt giống là $P(E) \\approx %s$.\\
Gọi $N$ là số hạt giống cần gieo để thu được khoảng $%s$ cây ngô con.\\
Ta có $P(E) \\approx \\dfrac{%s}{N}$, suy ra $\\dfrac{%s}{N} \\approx %s \\Rightarrow N \\approx \\dfrac{%s}{%s} = %s$.\\
Vậy nông trại cần gieo khoảng $%s$ hạt giống loại này.'''
                   % (k_nay, n_gieo, p_str, p_str, k_cay_con, k_cay_con, k_cay_con, p_str, k_cay_con, p_str, kq_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
