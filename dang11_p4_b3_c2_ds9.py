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


def bt_dang11_p4_b3_c2_ds9(self):
    phi_A = random.choice([40, 50, 60, 70])
    don_gia = random.choice([2, 3, 4, 5])
    while True:
        phi_B = phi_A + random.randint(40, 90)
        if (phi_B - phi_A) % don_gia != 0:
            break

    nghiem = Rational(phi_B - phi_A, don_gia)
    kq = math.floor(float(nghiem)) + 1

    noidungcauhoi = (
        f"Một nhà mạng cung cấp hai gói cước dữ liệu di động hàng tháng: Gói A có phí thuê bao cố định ${phi_A}\\,000$ đồng "
        f"và tính thêm ${don_gia}\\,000$ đồng cho mỗi GB sử dụng; Gói B trọn gói không giới hạn dung lượng với giá ${phi_B}\\,000$ đồng/tháng. "
        f"Hỏi trong một tháng, khách hàng sử dụng tối thiểu bao nhiêu GB dữ liệu (làm tròn đến hàng đơn vị) thì chọn Gói B sẽ tiết kiệm chi phí hơn Gói A?"
    )

    loigiai = (
        f"Gọi $x$ (GB) là dung lượng dữ liệu khách hàng sử dụng trong một tháng ($x > 0$).\\\n"
        f"Chi phí khi sử dụng Gói A là: ${phi_A} + {don_gia}x$ (nghìn đồng).\\\n"
        f"Để chọn Gói B tiết kiệm chi phí hơn Gói A thì chi phí Gói B phải nhỏ hơn chi phí Gói A, ta có bất phương trình:\\\n"
        f"${phi_B} < {phi_A} + {don_gia}x$\\\n"
        f"${don_gia}x > {phi_B - phi_A}$\\\n"
        f"$x > {latex(nghiem)} \\approx {round(float(nghiem), 2)}$.\\\n"
        f"Vậy khách hàng cần sử dụng tối thiểu ${kq}\\text{{ GB}}$ dữ liệu trong tháng."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
