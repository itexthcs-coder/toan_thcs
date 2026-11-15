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


def bt_dang14_p4_b3_c2_ds9(self):
    tong_tg = random.choice([45, 50, 60])
    calo_di_bo = random.choice([5, 6, 7])
    calo_chay = random.choice([11, 12, 14])

    min_calo = tong_tg * calo_di_bo + 60
    max_calo = tong_tg * calo_chay - 60
    muc_tieu = random.randrange(min_calo, max_calo, 20)

    hieu_calo = calo_chay - calo_di_bo
    vp_moi = muc_tieu - tong_tg * calo_di_bo
    nghiem = Rational(vp_moi, hieu_calo)
    kq = math.ceil(float(nghiem))

    noidungcauhoi = (
        f"Để rèn luyện sức khỏe, anh Nam đặt mục tiêu tiêu hao ít nhất ${muc_tieu}\\text{{ kcal}}$ trong mỗi buổi tập kéo dài đúng ${tong_tg}$ phút. "
        f"Anh kết hợp hai hình thức: đi bộ nhanh (tiêu hao ${calo_di_bo}\\text{{ kcal/phút}}$) và chạy bộ (tiêu hao ${calo_chay}\\text{{ kcal/phút}}$). "
        f"Hỏi trong mỗi buổi tập, anh Nam cần dành ít nhất bao nhiêu phút (làm tròn đến hàng đơn vị) để chạy bộ?"
    )

    loigiai = (
        f"Gọi $x$ (phút) là thời gian anh Nam chạy bộ ($0 \\le x \\le {tong_tg}$), khi đó thời gian đi bộ nhanh là ${tong_tg} - x$ (phút).\\\n"
        f"Tổng lượng calo tiêu hao trong buổi tập là: ${calo_chay}x + {calo_di_bo}({tong_tg} - x)$ (kcal).\\\n"
        f"Để tiêu hao ít nhất ${muc_tieu}\\text{{ kcal}}$, ta có bất phương trình:\\\n"
        f"${calo_chay}x + {calo_di_bo}({tong_tg} - x) \\ge {muc_tieu}$\\\n"
        f"${hieu_calo}x + {tong_tg * calo_di_bo} \\ge {muc_tieu}$\\\n"
        f"${hieu_calo}x \\ge {vp_moi}$\\\n"
        f"$x \\ge {latex(nghiem)}$.\\\n"
        f"Vậy anh Nam cần dành ít nhất ${kq}$ phút để chạy bộ."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
