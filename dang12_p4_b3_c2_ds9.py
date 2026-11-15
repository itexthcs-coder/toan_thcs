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


def bt_dang12_p4_b3_c2_ds9(self):
    P_cu = random.choice([60, 75, 100])
    P_moi = random.choice([9, 10, 12, 15])
    gia_cu = random.choice([12, 15, 20])
    gia_moi = gia_cu + random.choice([45, 50, 60, 75])
    gia_dien = random.choice([2000, 2500, 3000])

    tien_dien_cu = Rational(P_cu, 1000) * gia_dien
    tien_dien_moi = Rational(P_moi, 1000) * gia_dien
    hieu_tien_dien = tien_dien_cu - tien_dien_moi
    chenh_gia = (gia_moi - gia_cu) * 1000
    nghiem = Rational(chenh_gia, hieu_tien_dien)

    noidungcauhoi = (
        f"Một bóng đèn sợi đốt công suất ${P_cu}\\text{{ W}}$ có giá mua ${gia_cu}\\,000$ đồng, còn một bóng đèn LED có độ sáng tương đương "
        f"nhưng công suất chỉ ${P_moi}\\text{{ W}}$ có giá mua ${gia_moi}\\,000$ đồng. Biết giá điện sinh hoạt là ${gia_dien}$ đồng/kWh ($1\\text{{ kWh}} = 1\\,000\\text{{ Wh}}$). "
        f"Hỏi sau bao nhiêu giờ thắp sáng thì tổng chi phí (tiền mua bóng và tiền điện tiêu thụ) của việc dùng bóng đèn LED bắt đầu rẻ hơn bóng đèn sợi đốt?"
    )

    loigiai = (
        f"Gọi $x$ (giờ) là thời gian thắp sáng bóng đèn ($x > 0$).\\\n"
        f"Tiền điện tiêu thụ mỗi giờ của bóng đèn sợi đốt là: $\\dfrac{{{P_cu}}}{{1\\,000}} \\cdot {gia_dien} = {latex(tien_dien_cu)}$ (đồng).\\\n"
        f"Tiền điện tiêu thụ mỗi giờ của bóng đèn LED là: $\\dfrac{{{P_moi}}}{{1\\,000}} \\cdot {gia_dien} = {latex(tien_dien_moi)}$ (đồng).\\\n"
        f"Để tổng chi phí dùng bóng đèn LED rẻ hơn bóng đèn sợi đốt, ta có bất phương trình:\\\n"
        f"${gia_moi * 1000} + {latex(tien_dien_moi)}x < {gia_cu * 1000} + {latex(tien_dien_cu)}x$\\\n"
        f"${latex(hieu_tien_dien)}x > {chenh_gia}$\\\n"
        f"$x > {latex(nghiem)}$.\\\n"
        f"Vậy sau hơn ${latex(nghiem)}$ giờ thắp sáng thì dùng bóng đèn LED bắt đầu tiết kiệm hơn."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
