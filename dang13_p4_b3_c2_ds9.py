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


def bt_dang13_p4_b3_c2_ds9(self):
    chi_phi_cd = random.choice([15, 18, 20, 24])
    gia_von = random.choice([10, 12, 14, 15])
    gia_ban = gia_von + random.choice([15, 18, 20])
    loi_nhuan = random.choice([10, 12, 15, 18])

    lai_moi_ly = gia_ban - gia_von
    tong_can_bu = (chi_phi_cd + loi_nhuan) * 1000
    nghiem = Rational(tong_can_bu, lai_moi_ly)
    kq = math.ceil(float(nghiem))

    noidungcauhoi = (
        f"Một cửa hàng trà sữa có chi phí cố định (thuê mặt bằng, nhân viên, điện nước) là ${chi_phi_cd}\\,000\\,000$ đồng/tháng. "
        f"Chi phí nguyên liệu để pha chế một ly trà sữa là ${gia_von}\\,000$ đồng và giá bán mỗi ly là ${gia_ban}\\,000$ đồng. "
        f"Hỏi trong một tháng, cửa hàng cần bán ít nhất bao nhiêu ly trà sữa để đạt mức lợi nhuận từ ${loi_nhuan}\\,000\\,000$ đồng trở lên?"
    )

    loigiai = (
        f"Gọi $x$ (ly) là số ly trà sữa cửa hàng bán được trong tháng ($x \\in \\mathbb{{N}}^*$).\\\n"
        f"Lợi nhuận thu được từ việc bán $x$ ly trà sữa sau khi trừ chi phí cố định là:\\\n"
        f"$({gia_ban} - {gia_von})x - {chi_phi_cd * 1000} = {lai_moi_ly}x - {chi_phi_cd * 1000}$ (nghìn đồng).\\\n"
        f"Để đạt mức lợi nhuận từ ${loi_nhuan}\\,000\\,000$ đồng trở lên, ta có bất phương trình:\\\n"
        f"${lai_moi_ly}x - {chi_phi_cd * 1000} \\ge {loi_nhuan * 1000}$\\\n"
        f"${lai_moi_ly}x \\ge {tong_can_bu}$\\\n"
        f"$x \\ge {latex(nghiem)} \\approx {round(float(nghiem), 2)}$.\\\n"
        f"Vì $x \\in \\mathbb{{N}}^*$ nên cửa hàng cần bán ít nhất ${kq}$ ly trà sữa."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
