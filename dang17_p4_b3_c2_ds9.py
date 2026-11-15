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


def bt_dang17_p4_b3_c2_ds9(self):
    tong_ngay = random.choice([12, 15, 18, 20])
    ngay_dau = random.choice([4, 5, 6])
    ngay_con = tong_ngay - ngay_dau
    nang_suat_dau = random.choice([50, 60, 75, 80])
    tong_sp = ngay_dau * nang_suat_dau + ngay_con * random.randint(85, 130) + random.choice([0, 3, 5])

    sp_con = tong_sp - ngay_dau * nang_suat_dau
    nghiem = Rational(sp_con, ngay_con)
    kq = math.ceil(float(nghiem))

    noidungcauhoi = (
        f"Một phân xưởng nhận hợp đồng sản xuất ${tong_sp}$ sản phẩm trong thời hạn tối đa ${tong_ngay}$ ngày. "
        f"Trong ${ngay_dau}$ ngày đầu tiên, do máy móc chưa vận hành ổn định nên mỗi ngày phân xưởng chỉ làm được ${nang_suat_dau}$ sản phẩm. "
        f"Hỏi trong những ngày còn lại, mỗi ngày phân xưởng phải sản xuất ít nhất bao nhiêu sản phẩm để hoàn thành hợp đồng đúng hạn?"
    )

    loigiai = (
        f"Số ngày làm việc còn lại của phân xưởng là: ${tong_ngay} - {ngay_dau} = {ngay_con}$ (ngày).\\\n"
        f"Gọi $x$ (sản phẩm/ngày) là số sản phẩm phân xưởng làm được mỗi ngày trong thời gian còn lại ($x \\in \\mathbb{{N}}^*$).\\\n"
        f"Để hoàn thành hợp đồng đúng hạn, tổng số sản phẩm làm được phải đạt ít nhất ${tong_sp}$ sản phẩm, ta có bất phương trình:\\\n"
        f"${ngay_dau} \\cdot {nang_suat_dau} + {ngay_con}x \\ge {tong_sp}$\\\n"
        f"${ngay_dau * nang_suat_dau} + {ngay_con}x \\ge {tong_sp}$\\\n"
        f"${ngay_con}x \\ge {sp_con}$\\\n"
        f"$x \\ge {latex(nghiem)}$.\\\n"
        f"Vì $x \\in \\mathbb{{N}}^*$ nên mỗi ngày còn lại phân xưởng phải sản xuất ít nhất ${kq}$ sản phẩm."
    )

    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
