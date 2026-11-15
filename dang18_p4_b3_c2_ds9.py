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


def bt_dang18_p4_b3_c2_ds9(self):
    luong_cb = random.choice([7, 8, 9, 10])
    moc_ds = random.choice([40, 50, 60])
    hoa_hong = random.choice([4, 5, 8])
    thu_nhap = luong_cb + random.choice([5, 6, 8])

    chenh_luong = thu_nhap - luong_cb
    ty_le_hh = Rational(hoa_hong, 100)
    vuot_muc = chenh_luong / ty_le_hh
    nghiem = moc_ds + vuot_muc

    noidungcauhoi = (
        f"Chị Hoa làm nhân viên kinh doanh với mức lương cơ bản là ${luong_cb}\\,000\\,000$ đồng/tháng. "
        f"Ngoài ra, nếu doanh số bán hàng trong tháng vượt mức ${moc_ds}\\,000\\,000$ đồng thì chị được thưởng thêm hoa hồng bằng ${hoa_hong}\\%$ phần doanh số vượt mức đó. "
        f"Hỏi trong một tháng, chị Hoa cần đạt doanh số tối thiểu bao nhiêu triệu đồng để tổng thu nhập đạt ít nhất ${thu_nhap}\\,000\\,000$ đồng?"
    )

    loigiai = (
        f"Gọi $x$ (triệu đồng) là doanh số bán hàng của chị Hoa trong tháng ($x > {moc_ds}$).\\\n"
        f"Phần doanh số vượt mức quy định là $x - {moc_ds}$ (triệu đồng).\\\n"
        f"Tổng thu nhập trong tháng của chị Hoa là: ${luong_cb} + {hoa_hong}\\%(x - {moc_ds})$ (triệu đồng).\\\n"
        f"Để tổng thu nhập đạt ít nhất ${thu_nhap}$ triệu đồng, ta có bất phương trình:\\\n"
        f"${luong_cb} + \\dfrac{{{hoa_hong}}}{{100}}(x - {moc_ds}) \\ge {thu_nhap}$\\\n"
        f"$\\dfrac{{{hoa_hong}}}{{100}}(x - {moc_ds}) \\ge {chenh_luong}$\\\n"
        f"$x - {moc_ds} \\ge {latex(vuot_muc)}$\\\n"
        f"$x \\ge {latex(nghiem)}$.\\\n"
        f"Vậy chị Hoa cần đạt doanh số tối thiểu là ${latex(nghiem)}$ triệu đồng."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
