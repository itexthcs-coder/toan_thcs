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


def bt_dang11_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_tiep = random.choice([200, 300])
        du_doan = int(n_tiep * 35 / 100)

        noidungcauhoi = (
            'Một tấm bìa hình tròn được chia thành ba hình quạt có diện tích khác nhau với ba màu: Đỏ, Vàng, Xanh. Thực hiện quay tấm bìa $120$ lần, ghi lại màu hình quạt mà mũi tên chỉ vào khi dừng lại thu được kết quả: Đỏ ($54$ lần), Vàng ($42$ lần), Xanh ($24$ lần).\\\\ '
            'a) Lập bảng tần số tương đối cho kết quả thực nghiệm trên.\\\\ '
            'b) Ước lượng xác suất để mũi tên chỉ vào hình quạt màu Đỏ hoặc màu Xanh.\\\\ '
            'c) Nếu tiếp tục quay tấm bìa đó thêm $%s$ lần nữa thì dự đoán mũi tên sẽ chỉ vào hình quạt màu Vàng khoảng bao nhiêu lần?'
        ) % (n_tiep)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Tần số tương đối của các màu Đỏ, Vàng, Xanh lần lượt là: $\\frac{54}{120} \\cdot 100\\%% = 45\\%%$; $\\frac{42}{120} \\cdot 100\\%% = 35\\%%$; $\\frac{24}{120} \\cdot 100\\%% = 20\\%%$.\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|}\n'
            '\\hline\n'
            'Màu sắc & Đỏ & Vàng & Xanh \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $45\\%%$ & $35\\%%$ & $20\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Xác suất ước lượng để mũi tên chỉ vào hình quạt màu Đỏ hoặc màu Xanh là: $45\\%% + 20\\%% = 65\\%%$.\n'
            '\\item Vì xác suất ước lượng chỉ vào màu Vàng là $35\\%%$ nên trong $%s$ lần quay tiếp theo, dự đoán mũi tên chỉ vào hình quạt màu Vàng khoảng: $%s \\cdot 35\\%% = %s$ (lần).\n'
            '\\end{enumEX}'
        ) % (n_tiep, n_tiep, du_doan)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
